import os
import pandas as pd


def extract_from_csv(path):
    """Lee un csv y devuelve un DataFrame."""
    if path == '':
        filepath = os.path.join("erp_flow/files/", path)
        df = pd.read_csv(filepath)
        return df
    else:
        df = pd.read_csv(path)
        return df 

def print_df(df):
    print(df)


def my_first_pipeline():
    df = extract_from_csv('CUST_AZ12.csv')
    print_df(df)


if __name__ == "__main__":
    my_first_pipeline()