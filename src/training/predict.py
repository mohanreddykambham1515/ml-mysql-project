import joblib

# load saved model
model = joblib.load("models/fraud_model.pkl")

# sample input (new transaction)
sample = [[50000, 30000, 5]]

# prediction
prediction = model.predict(sample)

print("PREDICTION:", prediction[0])
