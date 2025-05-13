# %% tags=["parameters"]
from typing import List

upstream = ['clean_weather', 'create_locations', 'create_temperature_categories', 'create_weather_conditions',
            'create_wind_levels', 'create_wind_directions', 'create_humidity_levels', 'create_moon_phases']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, save_to_csv


def create_weather_table(weather: DataFrame, location: DataFrame, temperature_category: DataFrame,
                         weather_condition: DataFrame, wind_level: DataFrame, wind_direction: DataFrame,
                         humidity_level: DataFrame, moon_phase: DataFrame) -> DataFrame:
    # Map location_id using the correct column name
    weather['location_id'] = weather['location_name'].map(
        location.set_index('name')['id']
    )

    # Map weather_condition_id
    weather['weather_condition_id'] = weather['condition_text'].map(
        weather_condition.set_index('condition')['id']
    )

    # Map wind_direction_id
    weather['wind_direction_id'] = weather['wind_direction'].map(
        wind_direction.set_index('direction')['id']
    )

    # Map moon_phase_id
    weather['moon_phase_id'] = weather['moon_phase'].map(
        moon_phase.set_index('phase')['id']
    )

    # Calculate temperature_category_id
    weather['temperature_category_id'] = weather.apply(
        lambda row: temperature_category_df.loc[
            (temperature_category_df['range_start'] < row['temperature_celsius']) &
            (row['temperature_celsius'] <= temperature_category_df['range_end']), 'id'
        ].iloc[0] if not temperature_category_df.loc[
            (temperature_category_df['range_start'] < row['temperature_celsius']) &
            (row['temperature_celsius'] <= temperature_category_df['range_end'])
            ].empty else None,
        axis=1
    )

    # Calculate wind_level_id
    weather['wind_level_id'] = weather.apply(
        lambda row: wind_level_df.loc[
            (wind_level_df['range_start'] < row['wind_kph']) &
            (row['wind_kph'] <= wind_level_df['range_end']), 'id'
        ].iloc[0] if not wind_level_df.loc[
            (wind_level_df['range_start'] < row['wind_kph']) &
            (row['wind_kph'] <= wind_level_df['range_end'])
            ].empty else None,
        axis=1
    )

    # Calculate humidity_level_id
    weather['humidity_level_id'] = weather.apply(
        lambda row: humidity_level_df.loc[
            (humidity_level_df['range_start'] < row['humidity']) &
            (row['humidity'] <= humidity_level_df['range_end']), 'id'
        ].iloc[0] if not humidity_level_df.loc[
            (humidity_level_df['range_start'] < row['humidity']) &
            (row['humidity'] <= humidity_level_df['range_end'])
            ].empty else None,
        axis=1
    )

    # Ensure 'id' column exists in the weather DataFrame
    if 'id' not in weather.columns:
        weather['id'] = range(1, len(weather) + 1)

    # Select and rename columns for the Weather table
    weather_table = weather[[
        'id', 'location_id', 'last_updated_epoch', 'last_updated', 'temperature_celsius',
        'temperature_category_id', 'weather_condition_id', 'wind_kph', 'wind_level_id',
        'wind_degree', 'wind_direction_id', 'pressure_mb', 'precip_mm', 'humidity',
        'humidity_level_id', 'cloud', 'feels_like_celsius', 'visibility_km', 'uv_index',
        'gust_kph', 'air_quality_us_epa_index', 'air_quality_gb_defra_index', 'sunrise',
        'sunset', 'moonrise', 'moonset', 'moon_phase_id', 'moon_illumination'
    ]].copy()

    return weather_table


weather_path = transform_path + "/clean/weather.csv"
location_path = transform_path + "/migrations/locations.csv"
temperature_category_path = transform_path + "/migrations/temperature_categories.csv"
weather_condition_path = transform_path + "/migrations/weather_conditions.csv"
wind_level_path = transform_path + "/migrations/wind_levels.csv"
wind_direction_path = transform_path + "/migrations/wind_directions.csv"
humidity_level_path = transform_path + "/migrations/humidity_levels.csv"
moon_phase_path = transform_path + "/migrations/moon_phases.csv"
weather_df: DataFrame = load_csv(weather_path)
location_df: DataFrame = load_csv(location_path)
temperature_category_df: DataFrame = load_csv(temperature_category_path)
weather_condition_df: DataFrame = load_csv(weather_condition_path)
wind_level_df: DataFrame = load_csv(wind_level_path)
wind_direction_df: DataFrame = load_csv(wind_direction_path)
humidity_level_df: DataFrame = load_csv(humidity_level_path)
moon_phase_df: DataFrame = load_csv(moon_phase_path)
df = create_weather_table(weather=weather_df, location=location_df,
                          temperature_category=temperature_category_df,
                          weather_condition=weather_condition_df,
                          wind_level=wind_level_df, wind_direction=wind_direction_df,
                          humidity_level=humidity_level_df, moon_phase=moon_phase_df)
save_to_csv(df, product['data'])
