import pandas as pd


def add_prefix_to_subset(df: pd.DataFrame, prefix: str):
    col_list = df.columns
    df.columns = col_list.str.replace("\s\((.*)", "", regex=True)
    df.rename({'wynik średni': prefix+'wynik średni',
               'odchylenie standardowe': prefix+'odchylenie standardowe',
               'mediana': prefix+'mediana',
               'modalna': prefix+'modalna'},
              axis=1, inplace=True)
