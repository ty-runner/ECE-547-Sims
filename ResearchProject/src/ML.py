import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load your data
data = pd.read_csv('output.csv')

# Data preprocessing and feature engineering (adjust as needed)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='s')  # Convert to datetime
data['Timestamp'] = data['Timestamp'].astype('int64') // 10**9  # Convert to Unix timestamp in seconds

#data['Hour'] = data['Timestamp'].dt.hour  # Extract hour

# Label encode 'Source IP', 'Destination IP', and 'Protocol'
le_ip = LabelEncoder()
data['Source IP'] = le_ip.fit_transform(data['Source IP'])

# Save the label encoder for 'Source IP' for later use in the test set
source_ip_encoder = le_ip

le_dest_ip = LabelEncoder()
data['Destination IP'] = le_dest_ip.fit_transform(data['Destination IP'])

# Save the label encoder for 'Destination IP' for later use in the test set
dest_ip_encoder = le_dest_ip

le_protocol = LabelEncoder()
data['Protocol'] = le_protocol.fit_transform(data['Protocol'])

# Convert 'Length' to a numeric data type
data['Length'] = pd.to_numeric(data['Length'], errors='coerce')

# Define excess packets threshold (adjust as needed)
threshold = 200

# Create target variable (1 for excess, 0 for normal)
data['ExcessPackets'] = (data['Length'] > threshold).astype(int)

# Features and target variable
X = data.drop(['ExcessPackets'], axis=1)
y = data['ExcessPackets']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions))
