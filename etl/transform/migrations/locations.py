# %% tags=["parameters"]
from typing import List

upstream = ['extract', 'create_countries', 'create_timezones']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, save_to_csv


def create_locations_table(weather: DataFrame, timezones: DataFrame, countries: DataFrame) -> DataFrame:
    # Use a set to ensure unique locations
    unique_locations = set()
    locations_data = []

    for idx, row in weather.iterrows():
        country_id = countries[countries['name'] == row['country']]['id'].values[0]
        timezone_id = timezones[timezones['timezone'] == row['timezone']]['id'].values[0]
        location_tuple = (row['location_name'], row['latitude'], row['longitude'], timezone_id, country_id)

        if location_tuple not in unique_locations:
            unique_locations.add(location_tuple)
            locations_data.append({
                "id": len(locations_data) + 1,
                "location_name": row['location_name'],
                "latitude": row['latitude'],
                "longitude": row['longitude'],
                "timezone_id": timezone_id,
                "country_id": country_id
            })

    # Create a DataFrame for the Locations table
    locations_df = DataFrame(locations_data)
    return locations_df


weather_path = transform_path + "/clean/clean_weather.csv"
timezones_path = transform_path + "/migrations/timezones.csv"
countries_path = transform_path + "/migrations/countries.csv"
weather_df: DataFrame = load_csv(weather_path)
timezones_df: DataFrame = load_csv(timezones_path)
countries_df: DataFrame = load_csv(countries_path)
df: DataFrame = create_locations_table(weather=weather_df, timezones=timezones_df, countries=countries_df)
save_to_csv(df, product['data'])
