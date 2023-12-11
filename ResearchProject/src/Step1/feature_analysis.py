# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import OneClassSVM
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.covariance import EllipticEnvelope
from sklearn.cluster import KMeans
from sklearn.svm import OneClassSVM
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier


# Load the malicious dataset
malicious_file_path = "l2-malicious.csv"
df_malicious = pd.read_csv(malicious_file_path, nrows=15000)
df_malicious['Label'] = 1  # Set label for malicious traffic

# Load the DoH dataset
doh_file_path = "l2-benign.csv"
df_doh = pd.read_csv(doh_file_path, nrows=15000)
df_doh['Label'] = 0  # Set label for Benign DoH traffic

# Concatenate the datasets
df_combined = pd.concat([df_malicious, df_doh], ignore_index=True)

#Shuffle the DataFrame
df_combined_shuffled = shuffle(df_combined, random_state=42)  # Set a random_state for reproducibility
# Separate features and target variable
# for i in range(5, 34):
#     selected_columns = [i]  # Select the columns to be used as features
X = df_combined_shuffled.iloc[: , 5:20]
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
accuracies = {}
models = [
    IsolationForest(contamination=0.4, random_state=42),
    LocalOutlierFactor(contamination=0.4, novelty=True),
    EllipticEnvelope(contamination=0.4, random_state=42),
    KMeans(n_clusters=2, n_init=10, random_state=42), #Incorrect
    DecisionTreeClassifier(random_state=42),
    OneClassSVM(nu=0.4, kernel='linear', gamma='auto'),
    RandomForestClassifier(n_estimators=100, random_state=42),
    LogisticRegression(random_state=42, max_iter=1000)
    # XGBClassifier(random_state=42),
    # KNeighborsClassifier(n_neighbors=2),
    # SVC(kernel='linear', C=1.0, random_state=42),
    # GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=42),
    # AdaBoostClassifier(n_estimators=100, random_state=42),
    # GaussianNB(),
    # MLPClassifier(random_state=42, max_iter=1000),
    # BaggingClassifier(random_state=42)
]
for model in models:
    # Train the model
    model.fit(X_train, y_train)

    # Predictions on the test set
    y_pred = model.predict(X_test)

    # Convert predictions to 0 (DoH) and 1 (malicious)
    y_pred[y_pred == 1] = int(0)  # DoH
    y_pred[y_pred == -1] = int(1)  # Malicious

    # Evaluate the model
    print("\nModel:", type(model).__name__)
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    report = classification_report(y_test, y_pred, zero_division=1)
    print("\nClassification Report:\n", report)
    accuracies[type(model).__name__] = accuracy_score(y_test, y_pred)

print(accuracies)