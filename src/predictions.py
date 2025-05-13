import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from dataframes import Dataframes


class Predictions:
    @staticmethod
    def fit_arimax(endog: pd.Series, exog: pd.Series, order=(1,0,1)) -> SARIMAX.fit:
        model = SARIMAX(
            endog=endog,
            exog=exog,
            order=order,
            seasonal_order=(0, 0, 0, 0),  
            enforce_stationarity=False,
            enforce_invertibility=False
        )
        fit = model.fit(disp=False)
        print(fit.summary())
        return fit

    @staticmethod
    def predict(fit, steps: int, future_exog: pd.DataFrame) -> pd.DataFrame:
        forecast = fit.get_forecast(steps=steps, exog=future_exog)

        forecast_mean = forecast.predicted_mean
        forecast_ci   = forecast.conf_int()

        plt.figure(figsize=(10,5))
        plt.plot(forecast_mean.index, forecast_mean, label='Forecast', color='red')
        plt.fill_between(
            forecast_ci.index,
            forecast_ci.iloc[:,0],
            forecast_ci.iloc[:,1],
            color='pink', alpha=0.3
        )
        plt.legend()
        plt.title('Forecast of % change in rent prices in Ottawa')
        plt.show()

        return forecast_mean

