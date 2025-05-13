from dataframes import Dataframes 
from get import Get
from plotter import Plotter 
from predictions import Predictions

dir = "/Users/robinbilodeau/Desktop/repos/pandr/data"

def main(data_dir: str) -> None:

    df = Dataframes.create_dataframe(data_dir)
    df_pct = Dataframes.create_percentage_change_dataframe(Dataframes.create_dataframe(data_dir))

    Plotter.plot(df, kind='levels')
    Plotter.plot(df_pct, 'pct')
    Plotter.plot(df_pct, 'fit')
    Plotter.plot(df_pct, 'predict')

    


if __name__ == "__main__":
    print(main(dir))

