from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import joblib

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X, y)

# Save the trained model to a file
joblib.dump(model, 'trained_model.joblib')