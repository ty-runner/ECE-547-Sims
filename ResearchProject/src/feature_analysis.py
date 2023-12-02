# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import OneClassSVM
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
file_path = "l1-doh.csv"
df = pd.read_csv(file_path)

# Exclude the first 5 columns (assuming they are 0-indexed)
df = df.iloc[:, 5:]

# Separate features and target variable
X = df.drop('Label', axis=1)
y = df['Label']

# Handle missing values (simple imputation)
imputer = SimpleImputer(strategy='mean')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.2, random_state=42)

# Data preprocessing: Standardization
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# One-Class SVM model
model = OneClassSVM(nu=0.05, kernel='rbf', gamma='auto')  # Adjust hyperparameters as needed
model.fit(X_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Convert predictions to 0 (normal) and 1 (anomalous)
y_pred[y_pred == 1] = 0  # Normal
y_pred[y_pred == -1] = 1  # Anomalous

# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
