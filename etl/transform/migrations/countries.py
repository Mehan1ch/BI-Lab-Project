# %% tags=["parameters"]
from typing import List

upstream = ['extract', 'clean_weather']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, save_to_csv


def create_countries_table(population: DataFrame, weather: DataFrame) -> DataFrame:
    population_countries = population['Country'].unique()
    weather_countries = weather['country'].unique()
    countries = sorted(set(population_countries) | set(weather_countries))
    countries_data = []
    for idx, country in enumerate(countries, start=1):
        countries_data.append({
            "id": idx,
            "name": country,
            "total_population": population[population['Country'] == country][
                'Total'].sum() if country in population_countries else 0,
        })
    countries_df = DataFrame(countries_data)
    return countries_df


population_path = extract_path + "/population/population.csv"
weather_path = transform_path + "/clean/clean_weather.csv"
population_df: DataFrame = load_csv(population_path)
weather_df: DataFrame = load_csv(weather_path)
df: DataFrame = create_countries_table(population_df, weather_df)
save_to_csv(df, product['data'])
