import pandas as pd
import scipy.stats as stats


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


def outliers(frame: pd.DataFrame, col: str, remove: bool) -> pd.DataFrame:
    z = stats.zscore(frame[col])
    upper = 2
    lower = -2

    if remove:
        return frame[(lower <= z) & (z <= upper)]
    return frame[(z <= lower) | (upper <= z)]
