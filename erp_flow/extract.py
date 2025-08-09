import pandas as pd
from settings import EXCEL_PATH
import os

def extract_from_excel(filename):
    """Lee un Excel y devuelve un DataFrame."""
    filepath = os.path.join(EXCEL_PATH, filename)
    df = pd.read_excel(filepath)
    return df
