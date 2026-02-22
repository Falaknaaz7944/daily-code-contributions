# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample Data (Years of Experience)
X = np.array([[1], [2], [3], [4], [5]])

# Target Data (Salary)
y = np.array([30000, 40000, 50000, 60000, 70000])

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Salary for 6 Years Experience
prediction = model.predict([[6]])

print("Predicted Salary:", prediction[0])