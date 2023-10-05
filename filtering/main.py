import pandas as pd

def filtering(data:pd.DataFrame, columns:list)->pd.DataFrame:
    df = pd.read_csv(data)
    df = df_cities[[columns]]
    return df


#df_cities = df_cities[["city","elevation", "wind","avg_annual_precip","koppen"]]
