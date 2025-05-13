# %% tags=["parameters"]
upstream = ['extract', 'create_countries', 'create_timezones']
product: list[str] | None = None
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
                "name": row['location_name'],
                "latitude": row['latitude'],
                "longitude": row['longitude'],
                "timezone_id": timezone_id,
                "country_id": country_id
            })

    # Create a DataFrame for the Locations table
    locations_df = DataFrame(locations_data)

    # Remove duplicates based on 'name', keeping the first occurrence
    locations_df = locations_df.drop_duplicates(subset=['name'], keep='first')

    # Sort by 'name'
    locations_df = locations_df.sort_values(by='name').reset_index(drop=True)

    # Adjust the index to start from 1
    locations_df.index = locations_df.index + 1

    # Reset the index as a column named 'id'
    locations_df.reset_index(inplace=True)
    locations_df.rename(columns={'index': 'id'}, inplace=True)

    return locations_df


weather_path = transform_path + "/clean/clean_weather.csv"
timezones_path = transform_path + "/migrations/timezones.csv"
countries_path = transform_path + "/migrations/countries.csv"
weather_df: DataFrame = load_csv(weather_path)
timezones_df: DataFrame = load_csv(timezones_path)
countries_df: DataFrame = load_csv(countries_path)
df: DataFrame = create_locations_table(weather=weather_df, timezones=timezones_df, countries=countries_df)
save_to_csv(df, product['data'])
