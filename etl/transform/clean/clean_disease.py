# %% tags=["parameters"]

upstream = ['extract']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from etl.utils.utils import load_csv, save_to_csv, rename_columns

columns_to_rename = {
    "Age": "age",
    "Gender": "gender",
    "Temperature (C)": "temperature_celsius",
    "Humidity": "humidity",
    "Wind Speed (km/h)": "wind_kph",
}

disease_path = extract_path + '/disease/disease.csv'
df = load_csv(disease_path)
df = rename_columns(df, columns_to_rename)
save_to_csv(df, product['data'])
