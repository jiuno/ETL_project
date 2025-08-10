import os
import pandas as pd
from prefect import flow, task

@task
def extract_from_csv(filename):
    """Lee un csv y devuelve un DataFrame."""
    filepath = os.path.join("erp_flow/files/", filename)
    df = pd.read_csv(filepath)
    return df

@task
def print_df(df):
    return df.head().to_string()

@flow
def my_first_flow():
    df = extract_from_csv('CUST_AZ12.csv')
    str = print_df(df)
    #print(str)

if __name__ == "__main__":
    my_first_flow()