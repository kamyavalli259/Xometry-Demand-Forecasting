import pandas as pd

def create_time_features(df):
    df["day_of_week"] = df["order_date"].dt.dayofweek
    df["week"] = df["order_date"].dt.isocalendar().week
    df["month"] = df["order_date"].dt.month
    return df

def create_lag_features(df, lags=[7, 14, 28]):
    for lag in lags:
        df[f"lag_{lag}"] = df["daily_demand"].shift(lag)
    return df

def rolling_features(df):
    df["rolling_7"] = df["daily_demand"].rolling(7).mean()
    df["rolling_14"] = df["daily_demand"].rolling(14).mean()
    return df

def build_features(df):
    df = create_time_features(df)
    df = create_lag_features(df)
    df = rolling_features(df)
    return df.dropna()
