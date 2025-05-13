# %% tags=["parameters"]
from typing import List

upstream = ['extract']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, remove_unnecessary_columns, save_to_csv


def fix_country_names(weather_df: DataFrame, replacements: dict) -> DataFrame:
    """
    Replace country names in the DataFrame based on a dictionary of replacements.

    Args:
        weather_df (DataFrame): The DataFrame containing a 'country' column.
        replacements (dict): A dictionary where keys are old names and values are new names.

    Returns:
        DataFrame: The updated DataFrame with replaced country names.
    """
    weather_df['country'] = weather_df['country'].replace(replacements)
    return weather_df


def remove_quotes_from_columns(weather_df: DataFrame, columns: List[str]) -> DataFrame:
    for column in columns:
        if column in weather_df.columns:
            weather_df[column] = weather_df[column].str.replace('"', '', regex=False)
    return weather_df


columns_to_remove = [
    "temperature_fahrenheit",
    "wind_mph",
    "pressure_in",
    "precip_in",
    "feels_like_fahrenheit",
    "visibility_miles",
    "gust_mph",
    "air_quality_Carbon_Monoxide",
    "air_quality_Ozone",
    "air_quality_Nitrogen_dioxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM2.5",
    "air_quality_PM10",
]

# Dictionary to map country names to their replacements, not the prettiest but fuzzy searching didn't work
country_names_to_replace = {
    "Brunei Darussalam": "Brunei",
    "Bélgica": "Belgium",
    "Czech Republic": "Czechia",
    "Estonie": "Estonia",
    "Fiji Islands": "Fiji",
    "Inde": "India",
    "Jemen": "Yemen",
    "Komoren": "Comoros",
    "Kyrghyzstan": "Kyrgyzstan",
    "Lao People's Democratic Republic": "Laos",
    "Letonia": "Latvia",
    "Macedonia": "North Macedonia",
    "Malásia": "Malaysia",
    "Marrocos": "Morocco",
    "Mexique": "Mexico",
    "Micronesia": "Micronesia (country)",
    "Polônia": "Poland",
    "Saint-Vincent-et-les-Grenadines": "Saint Vincent and the Grenadines",
    "Saudi Arabien": "Saudi Arabia",
    "Seychelles Islands": "Seychelles",
    "Swaziland": "Eswatini",
    "Südkorea": "South Korea",
    "Timor-Leste": "Timor",
    "Turkménistan": "Turkmenistan",
    "USA United States of America": "United States",
    "United States of America": "United States",
    "Гватемала": "Guatemala",
    "Польша": "Poland",
    "Турция": "Turkey",
    "كولومبيا": "Colombia",
    "火鸡": "Turkey",
}

weather_path = extract_path + '/weather/weather.csv'
population_path = extract_path + '/population/population.csv'
population_df = load_csv(population_path)
df: DataFrame = load_csv(weather_path)
df = remove_unnecessary_columns(df, columns_to_remove)
df = remove_quotes_from_columns(df, ["country"])
df = fix_country_names(df, country_names_to_replace)
save_to_csv(df, product['data'])
