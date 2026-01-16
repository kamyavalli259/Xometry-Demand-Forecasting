import pandas as pd
from features.feature_engineering import build_features
from models.xgboost_model import train_xgb, predict
from evaluation.metrics import rmse

df = pd.read_parquet("data/processed/daily_demand")

df = df.sort_values("order_date")
df = build_features(df)

train = df[:-30]
test = df[-30:]

X_train = train.drop(columns=["daily_demand", "order_date"])
y_train = train["daily_demand"]

X_test = test.drop(columns=["daily_demand", "order_date"])
y_test = test["daily_demand"]

model = train_xgb(X_train, y_train)
preds = predict(model, X_test)

print("RMSE:", rmse(y_test, preds))
