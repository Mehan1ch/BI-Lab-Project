# %% tags=["parameters"]
upstream = None
product: list[str] | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.transform.utils.utils import save_to_csv


def create_wind_levels_table() -> DataFrame:
    # Define the wind levels data
    wind_levels = [
        {"id": 0, "name": "Calm", "range_start": 0, "range_end": 1},
        {"id": 1, "name": "Light Air", "range_start": 1, "range_end": 3},
        {"id": 2, "name": "Light Breeze", "range_start": 4, "range_end": 7},
        {"id": 3, "name": "Gentle Breeze", "range_start": 8, "range_end": 12},
        {"id": 4, "name": "Moderate Breeze", "range_start": 13, "range_end": 18},
        {"id": 5, "name": "Fresh Breeze", "range_start": 19, "range_end": 24},
        {"id": 6, "name": "Strong Breeze", "range_start": 25, "range_end": 31},
        {"id": 7, "name": "Near Gale", "range_start": 32, "range_end": 38},
        {"id": 8, "name": "Gale", "range_start": 39, "range_end": 46},
        {"id": 9, "name": "Severe Gale", "range_start": 47, "range_end": 54},
        {"id": 10, "name": "Storm", "range_start": 55, "range_end": 63},
        {"id": 11, "name": "Violent Storm", "range_start": 64, "range_end": 72},
        {"id": 12, "name": "Hurricane", "range_start": 72, "range_end": 83},
    ]

    # Convert the list of dictionaries to a DataFrame
    wind_levels_df = DataFrame(wind_levels)
    return wind_levels_df


df: DataFrame = create_wind_levels_table()
save_to_csv(df, product['data'])
