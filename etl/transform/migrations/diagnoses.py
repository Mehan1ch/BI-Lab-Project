# %% tags=["parameters"]
upstream = ['extract', 'create_age_groups', 'create_temperature_categories', 'create_wind_levels',
            'create_humidity_levels']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.utils.utils import load_csv, save_to_csv


def create_diagnoses_table(diseases: DataFrame, prognosis: DataFrame, age_groups: DataFrame,
                           temperature_categories: DataFrame,
                           wind_levels: DataFrame, humidity_levels: DataFrame) -> DataFrame:
    # Map age_group_id
    diseases['age_group_id'] = diseases['age'].apply(
        lambda age: age_groups.loc[
            (age_groups['range_start'] <= age) & (age <= age_groups['range_end']), 'id'
        ].iloc[0] if not age_groups.loc[
            (age_groups['range_start'] <= age) & (age <= age_groups['range_end'])
            ].empty else None
    )

    # Map temperature_category_id
    diseases['temperature_category_id'] = diseases['temperature_celsius'].apply(
        lambda temp: temperature_categories.loc[
            (temperature_categories['range_start'] < temp) & (temp <= temperature_categories['range_end']), 'id'
        ].iloc[0] if not temperature_categories.loc[
            (temperature_categories['range_start'] < temp) & (temp <= temperature_categories['range_end'])
            ].empty else None
    )

    # Map humidity_level_id
    diseases['humidity_level_id'] = diseases['humidity'].apply(
        lambda hum: humidity_levels.loc[
            (humidity_levels['range_start'] < hum) & (hum <= humidity_levels['range_end']), 'id'
        ].iloc[0] if not humidity_levels.loc[
            (humidity_levels['range_start'] < hum) & (hum <= humidity_levels['range_end'])
            ].empty else None
    )

    # Map wind_level_id
    diseases['wind_level_id'] = diseases['wind_kph'].apply(
        lambda wind: wind_levels.loc[
            (wind_levels['range_start'] < wind) & (wind <= wind_levels['range_end']), 'id'
        ].iloc[0] if not wind_levels.loc[
            (wind_levels['range_start'] < wind) & (wind <= wind_levels['range_end'])
            ].empty else None
    )

    # Map prognosis_id
    diseases['prognosis_id'] = diseases['prognosis'].map(
        prognosis.set_index('name')['id']
    )

    # Ensure 'id' column exists
    if 'id' not in diseases.columns:
        diseases['id'] = range(1, len(diseases) + 1)

    # Select and rename columns for the Diagnoses table
    diagnoses_table = diseases[[
        'id', 'age', 'age_group_id', 'gender', 'temperature_celsius',
        'temperature_category_id', 'humidity', 'humidity_level_id',
        'wind_kph', 'wind_level_id', 'prognosis_id'
    ]].copy()

    return diagnoses_table


diseases_path = transform_path + "/clean/disease.csv"
prognosis_path = transform_path + "/migrations/prognosis.csv"
age_groups_path = transform_path + "/migrations/age_groups.csv"
temperature_categories_path = transform_path + "/migrations/temperature_categories.csv"
wind_levels_path = transform_path + "/migrations/wind_levels.csv"
humidity_levels_path = transform_path + "/migrations/humidity_levels.csv"

disease_df = load_csv(diseases_path)
prognosis_df = load_csv(prognosis_path)
age_groups_df = load_csv(age_groups_path)
temperature_categories_df = load_csv(temperature_categories_path)
humidity_levels_df = load_csv(humidity_levels_path)
wind_levels_df = load_csv(wind_levels_path)

df = create_diagnoses_table(diseases=disease_df, prognosis=prognosis_df,
                            age_groups=age_groups_df,
                            temperature_categories=temperature_categories_df,
                            wind_levels=wind_levels_df, humidity_levels=humidity_levels_df)
save_to_csv(df, product['data'])
