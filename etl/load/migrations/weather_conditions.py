# %% tags=["parameters"]
upstream = ['create_weather_conditions']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.weather_conditions import WeatherCondition
from etl.utils.utils import insert_data_from_csv

WeatherCondition.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/weather_conditions.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(WeatherCondition, csv_file_path, session)
