import xgboost as xgb
import mlflow
import mlflow.xgboost

def train_xgb(X_train, y_train):
    with mlflow.start_run():
        model = xgb.XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8
        )
        model.fit(X_train, y_train)

        # Log model and params
        mlflow.log_params(model.get_params())
        mlflow.xgboost.log_model(model, "xgboost_model")

    return model

def predict(model, X_test):
    return model.predict(X_test)
