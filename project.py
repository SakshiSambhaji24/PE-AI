# Simple Linear Regression Example with User Input
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data (X = study hours, y = marks)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([30, 35, 50, 45, 60, 65, 70, 80, 85])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model info
print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# --- 🧮 Take input from user ---
hours = float(input("Enter number of study hours: "))
predicted_marks = model.predict([[hours]])
print(f"Predicted Marks for {hours} study hours = {predicted_marks[0]:.2f}")

# Plot results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(hours, predicted_marks, color='green', label='Predicted Point', s=100)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression Example")
plt.legend()
plt.show()
