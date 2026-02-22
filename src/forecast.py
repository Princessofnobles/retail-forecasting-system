import joblib
import pandas as pd
from config import MODEL_PATH
from data_pipeline import load_data, basic_cleaning
from feature_engineering import feature_engineering_pipeline

def generate_forecast():
    model = joblib.load(MODEL_PATH)

    df = load_data()
    df = basic_cleaning(df)
    df = feature_engineering_pipeline(df)

    X = df.drop(columns=["demand", "date"])
    df["prediction"] = model.predict(X)

    df[["date", "prediction"]].to_csv("data/future_forecast.csv", index=False)

    print("Forecast Generated Successfully")

if __name__ == "__main__":
    generate_forecast()