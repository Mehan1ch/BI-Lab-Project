# %% tags=["parameters"]
upstream = None
product: list[str] | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.transform.utils.utils import save_to_csv


def create_temperature_categories_table() -> DataFrame:
    # Define the temperature categories
    temperature_categories = [
        {"id": 1, "name": "Very Cold", "range_start": None, "range_end": 10},
        {"id": 2, "name": "Cold", "range_start": 10, "range_end": 20},
        {"id": 3, "name": "Good", "range_start": 20, "range_end": 27},
        {"id": 4, "name": "Hot", "range_start": 27, "range_end": 35},
        {"id": 5, "name": "Very Hot", "Range Start": 35, "range_end": None},
    ]

    # Convert the list of dictionaries to a DataFrame
    temperature_categories_df = DataFrame(temperature_categories)
    return temperature_categories_df


df: DataFrame = create_temperature_categories_table()
save_to_csv(df, product['data'])
