from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("models/fraud_model.pkl")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/predict")
def predict(amount: float, avg_last_5_amount: float, num_prev_transactions: int):

    sample = [[amount, avg_last_5_amount, num_prev_transactions]]

    prediction = model.predict(sample)[0]

    return {"prediction": int(prediction)}
