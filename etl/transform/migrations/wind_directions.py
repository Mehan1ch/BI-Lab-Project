# %% tags=["parameters"]
upstream = ['clean_weather']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.transform.utils.utils import save_to_csv, load_csv


def create_wind_directions_table(weather: DataFrame) -> DataFrame:
    # Extract unique names from the disease_df
    unique_names = weather['wind_direction'].unique()
    unique_names.sort()

    # Create the prognosis table
    prognosis_table = [{"id": idx + 1, "direction": direction} for idx, direction in enumerate(unique_names)]

    # Convert to DataFrame
    prognosis_df = DataFrame(prognosis_table)
    return prognosis_df


weather_path = transform_path + "/clean/clean_weather.csv"
weather_df = load_csv(weather_path)
df: DataFrame = create_wind_directions_table(weather_df)
save_to_csv(df, product['data'])
