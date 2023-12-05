# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import OneClassSVM
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score

# Load the malicious dataset
malicious_file_path = "l2-malicious.csv"
df_malicious = pd.read_csv(malicious_file_path, nrows=10000)
df_malicious['Label'] = 1  # Set label for malicious traffic

# Load the DoH dataset
doh_file_path = "l1-doh.csv"
df_doh = pd.read_csv(doh_file_path, nrows=10000)
df_doh['Label'] = 0  # Set label for DoH traffic

# Concatenate the datasets
df_combined = pd.concat([df_malicious, df_doh], ignore_index=True)

#Shuffle the DataFrame
df_combined_shuffled = shuffle(df_combined, random_state=42)  # Set a random_state for reproducibility

# Separate features and target variable
accuracies = {}
for i in range(5, 30):
    selected_columns = [i]  # Select the columns to be used as features
    X = df_combined_shuffled.iloc[: , selected_columns]
    y = df_combined_shuffled['Label']

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
    model = OneClassSVM(nu=0.5, kernel='rbf', gamma='auto')  # Adjust hyperparameters as needed
    model.fit(X_train)

    # Predictions on the test set
    y_pred = model.predict(X_test)

    # Convert predictions to 0 (DoH) and 1 (malicious)
    y_pred[y_pred == 1] = 0  # DoH
    y_pred[y_pred == -1] = 1  # Malicious

    # Evaluate the model
    #print({X.columns[0]})
    #print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    #report = classification_report(y_test, y_pred)
    report = accuracy_score(y_test, y_pred)
    print("\nClassification Report:\n", report)
    accuracies[X.columns[0]] = report
print(accuracies)
