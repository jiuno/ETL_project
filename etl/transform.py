import pandas as pd

def clean_dates(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def enrich_sales(df_sales: pd.DataFrame, df_products: pd.DataFrame) -> pd.DataFrame:
    return df_sales.merge(df_products[['id_producto', 'nombre']], on='id_producto', how='left')
