import matplotlib.pyplot as plt
import pandas as pd
from dataframes import Dataframes
from predictions import Predictions

class Plotter:
    @staticmethod
    def plot(df: pd.DataFrame, kind: str = "levels, pct, fit, or predict") -> None:
        
        if kind == "levels":
            fig, axes = plt.subplots(1, 2, figsize=(10, 5))
            x1 = df['population']
            x2 = df['rent']
            axes[0].plot(x1)
            axes[0].set_title('Population increase in Ottawa')
            axes[1].plot(x2)
            axes[1].set_title('Rent price increase in Ottawa')
            axes[0].set_xlabel("Year")
            axes[0].grid(alpha=0.3)
            axes[1].set_xlabel("Year")
            axes[1].grid(alpha=0.3)
            plt.tight_layout()
            plt.show()
        elif kind == "pct":
            ax = df.plot(marker='o', figsize=(8, 5))
            ax.set_xlabel("Year")
            ax.grid(alpha=0.3)
            ax.set_title("Year-over-Year % Change in Population & Rent")
            ax.set_ylabel("Percent Change (%)")
            plt.tight_layout()
            plt.show()
        elif kind == "fit":
            rent_pct, pop_pct = df['rent'], df['population']
            fit = Predictions.fit_arimax(endog=rent_pct, exog=pop_pct, order=(1,1,1))
            fitted = fit.fittedvalues
            fig, ax = plt.subplots(figsize=(8,5))
            ax.plot(rent_pct.index, rent_pct,    label='Observed', marker='o')
            ax.plot(fitted.index,    fitted,     label='Fitted',   linestyle='--')
            ax.set_title('ARIMAX Fit: Rent Δ% with Population Δ% exog')
            ax.set_ylabel('Yearly % Change')
            ax.legend()
            plt.show()
        elif kind == "predict":
            pop_pct, rent_pct = df['population'], df['rent'], 
            fit = Predictions.fit_arimax(endog=rent_pct, exog=pop_pct, order=(1,0,1))
            future_years = pd.date_range(start=df.index[-1] + pd.offsets.YearBegin(), periods=5,freq='YS')
            last = pop_pct.iloc[-1]          
            projections = [last-0.1*i for i in range(5)]
            future_pop_pct = pd.Series(projections, index=future_years, name='population')
            future_exog = pd.DataFrame({'population': future_pop_pct})
            forecast_rent_pct = Predictions.predict(fit=fit, steps=5, future_exog=future_exog)
            print(forecast_rent_pct) 

        else:
            raise ValueError(f"Unknown plot kind: {kind!r}")
        
        
