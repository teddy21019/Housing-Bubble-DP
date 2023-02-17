import pandas as pd


def jst_dataset_loader(file_path:str):
    df = pd.read_excel(file_path, engine='openpyxl', sheet_name='Data')

    return df