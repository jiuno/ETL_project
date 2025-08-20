import os
from time import sleep
import pandas as pd
from prefect import flow, task

@task
def extract_from_csv(path):
    df = pd.read_csv(path)
    print(f"Extracted df with shape {df.shape}")
    return df

@task
def reading_df(df):
    print(f"Received df of type {type(df)}")
    return df

@task
def write_csv(df):
    print(f"Writing df with shape {df.shape}")
    df.to_csv('output.csv', index=False)
    sleep(1) #Por alguna razon si es muy rapida la task se rompe al intentar actualizar la bd de prefect por concurrencia.
    

@flow
def my_first_flow(path):
    df = extract_from_csv(path)
    df = reading_df(df)
    write_csv(df)
    print('finish')
    
if __name__ == "__main__":
    my_first_flow(path='erp_flow/files/CUST_AZ12.csv')