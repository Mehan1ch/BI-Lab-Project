# %% tags=["parameters"]
upstream = None
product: list[str] | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.utils.utils import save_to_csv


def create_wind_levels_table() -> DataFrame:
    # Define the wind levels data
    wind_levels = [
        {"id": 1, "name": "Calm", "range_start": 0, "range_end": 1},
        {"id": 2, "name": "Light Air", "range_start": 1, "range_end": 3},
        {"id": 3, "name": "Light Breeze", "range_start": 3, "range_end": 7},
        {"id": 4, "name": "Gentle Breeze", "range_start": 7, "range_end": 12},
        {"id": 5, "name": "Moderate Breeze", "range_start": 12, "range_end": 18},
        {"id": 6, "name": "Fresh Breeze", "range_start": 18, "range_end": 24},
        {"id": 7, "name": "Strong Breeze", "range_start": 24, "range_end": 31},
        {"id": 8, "name": "Near Gale", "range_start": 31, "range_end": 38},
        {"id": 9, "name": "Gale", "range_start": 38, "range_end": 46},
        {"id": 10, "name": "Severe Gale", "range_start": 46, "range_end": 54},
        {"id": 11, "name": "Storm", "range_start": 54, "range_end": 63},
        {"id": 12, "name": "Violent Storm", "range_start": 63, "range_end": 72},
        {"id": 13, "name": "Hurricane", "range_start": 72, "range_end": 83},
    ]

    # Convert the list of dictionaries to a DataFrame
    wind_levels_df = DataFrame(wind_levels)
    return wind_levels_df


df: DataFrame = create_wind_levels_table()
save_to_csv(df, product['data'])
