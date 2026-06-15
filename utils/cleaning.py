import pandas as pd

def clean_data(df):

    df.drop_duplicates(inplace=True)

    df.fillna(0, inplace=True)

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    return df