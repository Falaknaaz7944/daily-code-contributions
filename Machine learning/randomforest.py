# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# 1. Load the dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 2. Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Create a Random Forest classifier object
# n_estimators is the number of decision trees in the forest (100 is a common default)
# random_state ensures reproducible results
rfc = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. Train the model using the training data
rfc.fit(X_train, y_train)

# 5. Make predictions on the test data
y_pred = rfc.predict(X_test)

# 6. Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

# Optional: View feature importance
feature_importances = pd.Series(rfc.feature_importances_, index=feature_names).sort_values(ascending=False)
print("\nFeature Importances:")
print(feature_importances)
