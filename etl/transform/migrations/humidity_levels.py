# %% tags=["parameters"]
upstream = None
product: list[str] | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.utils.utils import save_to_csv


def create_humidity_levels_table() -> DataFrame:
    # Define the temperature categories
    humidity_levels = [
        {"id": 1, "name": "Too Dry", "range_start": 0, "range_end": 30},
        {"id": 2, "name": "Dry", "range_start": 30, "range_end": 40},
        {"id": 3, "name": "Ideal", "range_start": 40, "range_end": 60},
        {"id": 4, "name": "Slightly humid", "range_start": 60, "range_end": 70},
        {"id": 5, "name": "Humid", "range_start": 70, "range_end": 80},
        {"id": 5, "name": "Excessively Humid", "range_start": 80, "range_end": 100},
    ]

    # Convert the list of dictionaries to a DataFrame
    humidity_levels_df = DataFrame(humidity_levels)
    return humidity_levels_df


df: DataFrame = create_humidity_levels_table()
save_to_csv(df, product['data'])
