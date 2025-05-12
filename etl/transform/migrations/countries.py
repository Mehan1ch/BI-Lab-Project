# %% tags=["parameters"]
from typing import List

upstream = ['extract']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, save_to_csv


def create_countries_table(population: DataFrame, weather: DataFrame) -> DataFrame:
    # Group by country and calculate total population
    grouped = population.groupby('Country')['Total'].sum().reset_index()

    # Add Id column
    grouped.insert(0, 'Id', range(1, len(grouped) + 1))

    # Rename columns to match the desired format
    grouped.columns = ['id', 'name', 'total_population']

    return grouped


population_path = extract_path + "/population/population.csv"
weather_path = extract_path + "/weather/weather.csv"
population_df: DataFrame = load_csv(population_path)
df: DataFrame = create_countries_table(population_df, population_df)
save_to_csv(df, product['data'])
