import pandas as pd

def read_excel(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def read_all_excels() -> dict:
    return {
        "ventas": read_excel("data/raw/ventas.xlsx"),
        "productos": read_excel("data/raw/productos.xlsx"),
        "sucursales": read_excel("data/raw/sucursales.xlsx"),
    }
