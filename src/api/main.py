from fastapi import FastAPI
import joblib

app = FastAPI()

# load model
model = joblib.load("models/fraud_model.pkl")


@app.get("/")
def home():
    return {"message": "API is running"}
