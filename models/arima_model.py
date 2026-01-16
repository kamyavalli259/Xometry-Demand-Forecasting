from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_arima(train_series):
    model = SARIMAX(
        train_series,
        order=(1,1,1),
        seasonal_order=(1,1,1,7)
    )
    return model.fit(disp=False)

def forecast(model, steps):
    return model.forecast(steps)
