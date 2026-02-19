from src.database.load_data import load_transactions
from sklearn.ensemble import RandomForestClassifier
import joblib


if __name__ == "__main__":

    # load data from MySQL
    df = load_transactions()

    # features and target
    X = df[["amount", "avg_last_5_amount", "num_prev_transactions"]]
    y = df["is_fraud"]

    # train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # save model
    joblib.dump(model, "models/fraud_model.pkl")

    print("MODEL TRAINED AND SAVED")
