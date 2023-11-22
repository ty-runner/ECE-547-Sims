# Import necessary libraries
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your actual dataset)
data = pd.read_csv('your_dataset.csv')

# Assume the target variable is 'congestion_level' and features are all other columns
X = data.drop('congestion_level', axis=1)
y = data['congestion_level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate an AdaBoost regressor with DecisionTreeRegressor as the base estimator
# You can use DecisionTreeClassifier for classification problems
base_estimator = None  # Use DecisionTreeRegressor as the default base estimator
model = AdaBoostRegressor(base_estimator=base_estimator, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
