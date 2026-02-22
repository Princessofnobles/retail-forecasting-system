import pandas as pd
from config import DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df

def basic_cleaning(df):
    df = df.dropna()
    return df

if __name__ == "__main__":
    df = load_data()
    df = basic_cleaning(df)
    print("Data Loaded Successfully")
    print(df.head())