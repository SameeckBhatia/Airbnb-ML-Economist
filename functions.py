import pandas as pd
import numpy as np
import requests
import scipy.stats as stats
from sklearn.metrics import r2_score as r2, mean_squared_error as mse


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


def bin_interval(lower: int, upper: int, width: int) -> range:
    return range(lower, upper + width, width)


def collect_census() -> None:
    # Setup
    base_url = "https://api.census.gov/data/2022/acs/acs5"
    variables = {"B01001_001E": "population", "B19013_001E": "median_income",
                 "B15003_022E": "num_bachelors", "B15003_023E": "num_masters",
                 "B15003_025E": "num_doctorate", "B02001_002E": "num_white"}

    params = {"get": ",".join(list(variables.keys())),
              "for": "zip code tabulation area:*",
              "key": "38a7c19fc2f81ffacb02b5373a7af82a5ed2cd21"}

    response = requests.get(base_url, params=params).json()

    # Extraction
    header = list(variables.values())
    header.append("zip_code")
    row_list = [i for i in response[1:]]

    census_df = pd.DataFrame(columns=header, data=row_list)

    # Transformation
    columns = census_df.columns.tolist()
    columns = [columns[-1]] + columns[:-1]
    census_df = census_df[columns]

    for i in list(census_df.columns)[1:]:
        census_df[i] = pd.to_numeric(census_df[i])

    sum_tertiary = np.sum(
        census_df[["num_bachelors", "num_masters", "num_doctorate"]], axis=1)

    census_df["pct_tertiary"] = sum_tertiary / census_df["population"]
    census_df["pct_white"] = census_df["num_white"] / census_df["population"]
    census_df["pct_tertiary"] = 100 * round(census_df["pct_tertiary"], 3)
    census_df["pct_white"] = 100 * round(census_df["pct_white"], 3)

    census_df = census_df[census_df["median_income"] > 0]

    # Export
    census_df.to_csv("supplemental_data/census.csv", index=False)


def view_metrics(names: list, models: list, X: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:
    r2s = [r2(y, model.predict(X)) for model in models]
    mses = [mse(y, model.predict(X)) for model in models]
    
    table = pd.DataFrame({"Model Name": names, "R^2": r2s, "MSE": mses}).set_index("Model Name")
    
    return table
