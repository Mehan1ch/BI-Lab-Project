# %% tags=["parameters"]
upstream = ['extract']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.utils.utils import load_csv, remove_unnecessary_columns, save_to_csv, rename_columns, \
    remove_quotes_from_columns, replace_column_content, convert_column_to_time

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

condition_replacements = {
    "Partly Cloudy": "Partly cloudy",
}

moonrise_replacements = {
    "No moonrise": "",
}

moonset_replacements = {
    "No moonset": "",
}

sunrise_replacements = {
    "No sunrise": "",
}
sunset_replacements = {
    "No sunset": "",
}

location_replacements = {
    "Addis Abeba": "Addis Ababa",
    "Beijing Shi": "Beijing",
    "Kuwait City": "Kuwait",
}

columns_to_rename = {
    'air_quality_us-epa-index': 'air_quality_us_epa_index',
    'air_quality_gb-defra-index': 'air_quality_gb_defra_index',
}

weather_path = extract_path + '/weather/weather.csv'
population_path = extract_path + '/population/population.csv'
population_df = load_csv(population_path)
df: DataFrame = load_csv(weather_path)
df = remove_unnecessary_columns(df, columns_to_remove)
df = remove_quotes_from_columns(df, ["country"])
df = rename_columns(df, columns_to_rename)
df = replace_column_content(df, 'country', country_names_to_replace)
df = replace_column_content(df, 'condition_text', condition_replacements)
df = replace_column_content(df, 'location_name', location_replacements)
df = replace_column_content(df, 'sunrise', sunrise_replacements)
df = replace_column_content(df, 'sunset', sunset_replacements)
df = replace_column_content(df, 'moonrise', moonrise_replacements)
df = replace_column_content(df, 'moonset', moonset_replacements)
df = convert_column_to_time(df, 'sunrise')
df = convert_column_to_time(df, 'sunset')
df = convert_column_to_time(df, 'moonrise')
df = convert_column_to_time(df, 'moonset')
save_to_csv(df, product['data'])
