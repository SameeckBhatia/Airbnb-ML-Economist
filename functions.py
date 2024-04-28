import pandas as pd


def merge_past_data(df: pd.DataFrame) -> pd.DataFrame:
    base_url = "http://data.insideairbnb.com/united-states/ca/los-angeles"

    df1 = pd.read_csv(f"{base_url}/2023-09-03/visualisations/listings.csv")
    df2 = pd.read_csv(f"{base_url}/2023-06-06/visualisations/listings.csv")
    df3 = pd.read_csv(f"{base_url}/2023-03-07/visualisations/listings.csv")

    df["quarter"] = 4
    df1["quarter"] = 3
    df2["quarter"] = 2
    df3["quarter"] = 1

    df = pd.concat([df, df1, df2, df3])
    df.drop_duplicates(subset=["id"], keep="first", inplace=True)

    return df
