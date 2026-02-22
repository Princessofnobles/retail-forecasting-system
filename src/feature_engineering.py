import pandas as pd

def create_lag_features(df, target_col="demand"):
    df["lag_1"] = df[target_col].shift(1)
    df["lag_7"] = df[target_col].shift(7)
    return df

def create_rolling_features(df, target_col="demand"):
    df["rolling_mean_7"] = df[target_col].rolling(7).mean()
    return df

def create_time_features(df):
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month
    return df

def feature_engineering_pipeline(df):
    df = create_lag_features(df)
    df = create_rolling_features(df)
    df = create_time_features(df)
    df = df.dropna()
    return df