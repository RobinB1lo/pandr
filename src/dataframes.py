import pandas as pd 
from get import Get

class Dataframes:
    def create_dataframe(data_dir: str) -> pd.DataFrame:
        dicts = Get.get_data(data_dir)

        pop_dict = dicts[0]
        rent_dict = dicts[1]

        df = pd.DataFrame({
            'population': pop_dict,
            'rent': rent_dict
        })

        df.index = pd.to_datetime(df.index + '-10-01')

        df = df.sort_index()
        return df

    def create_percentage_change_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
        df_pct = dataframe.pct_change() * 100
        df_pct = df_pct.dropna()

        return df_pct 
