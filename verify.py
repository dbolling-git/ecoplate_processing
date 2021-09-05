import pandas as pd


def verify_df(dataframe):
    is_good_df = True
    if len(dataframe) % 8 != 0:
        is_good_df = False
        print('Rows are missing.')
    for col in dataframe.columns:
        if dataframe[col].isnull().any():
            is_good_df = False
            print(f'Column {col} is missing value(s).')
    if is_good_df:
        print(f'Processing {len(dataframe)//8} plates...')
    return is_good_df