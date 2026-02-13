# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Create simple dataset (House Size vs Price)
X = np.array([[500], [1000], [1500], [2000], [2500]])  # size in sq ft
y = np.array([100000, 200000, 300000, 400000, 500000])  # price

# Step 2: Split into training & testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create model
model = LinearRegression()

# Step 4: Train model
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate model
print("Predicted:", y_pred)
print("Actual:", y_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Step 7: Predict new value
new_size = np.array([[1800]])
predicted_price = model.predict(new_size)
print("Predicted price for 1800 sq ft:", predicted_price[0])
