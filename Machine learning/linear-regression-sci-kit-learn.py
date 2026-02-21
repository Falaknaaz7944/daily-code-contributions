import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])   # Features (2D array required)
y = np.array([2, 4, 6, 8, 10])            # Target

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Print results
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression")
plt.show()