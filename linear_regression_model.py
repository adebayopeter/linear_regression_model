import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import joblib

# Import dataset
df = pd.read_excel('data/data.xlsx')

# Independent, dependent features
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Creating the training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building and training the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Inference
y_pred = model.predict(X_test)
print(y_pred)
# Making the prediction a single data point with AT = 15, V = 40, AP = 1000, RH = 75
print(model.predict([[15, 40, 1000, 75]]))

# Evaluating the model
# R-Squared
r2 = r2_score(y_test, y_pred)
print(r2)

# Adjusted R-Squared
k = X_test.shape[1]
n = X_test.shape[0]

adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)
print(adj_r2)

# Scatter Plot of Actual vs. Predicted Values
plt.figure(figsize=(8, 6))
# Plot actual vs. predicted
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.show()

# Save the trained model to a .pkl file
joblib.dump(model, "model/model.pkl")
