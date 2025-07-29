## etl/load.py
import sqlite3
import pandas as pd

def save_to_sqlite(df: pd.DataFrame, conn: sqlite3.Connection, table_name: str):
    print(f"💾 Guardando datos en tabla '{table_name}'")
    df.to_sql(table_name, conn, if_exists="replace", index=False)

def export_to_csv(df: pd.DataFrame, path: str):
    print(f"💾 Exportando a CSV en: {path}")
    df.to_csv(path, index=False)



