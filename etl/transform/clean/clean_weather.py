# %% tags=["parameters"]
from typing import List

upstream = ['extract']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, remove_unnecessary_columns, save_to_csv

columns_to_remove = [
    "temperature_fahrenheit",
    "wind_mph",
    "pressure_in",
    "precip_in",
    "feels_like_fahrenheit",
    "visibility_miles",
    "gust_mph",
    "air_quality_Carbon_Monoxide",
    "air_quality_Ozone",
    "air_quality_Nitrogen_dioxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM2.5",
    "air_quality_PM10",
]
file_path = extract_path + '/weather/weather.csv'

df: DataFrame = load_csv(file_path)
df = remove_unnecessary_columns(df, columns_to_remove)
save_to_csv(df, product['data'])
