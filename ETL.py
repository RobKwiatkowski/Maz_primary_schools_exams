import pandas as pd
import os.path


def read_raw_data(path:str, sheet_number=1) -> pd.DataFrame:
    if os.path.isfile(path):
        data = pd.read_excel(path, sheet_name=sheet_number)
    else:
        raise FileExistsError

    return data


def add_prefix_to_subset(df: pd.DataFrame, prefix: str) -> None:
    col_list = df.columns
    df.columns = col_list.str.replace("\s\((.*)", "", regex=True)
    df.rename({'wynik średni': prefix+'wynik średni',
               'odchylenie standardowe': prefix+'odchylenie standardowe',
               'mediana': prefix+'mediana',
               'modalna': prefix+'modalna'},
              axis=1, inplace=True)
