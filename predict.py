import joblib

# Load the saved model
loaded_model = joblib.load('trained_model.joblib')

# New input data for prediction
new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.8, 4.8, 1.8], [5.8, 2.7, 4.1, 1.0], [0.0, 0.0, 0.0, 0.0]]

# Make predictions using the loaded model
predictions = loaded_model.predict(new_data)

# Print the predictions
for data, prediction in zip(new_data, predictions):
    print(f"Input: {data}, Predicted class: {prediction}")
