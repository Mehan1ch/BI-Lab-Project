# %% tags=["parameters"]


upstream = ['create_weather',
            'load_locations', 'load_temperature_categories', 'load_weather_conditions',
            'load_wind_levels', 'load_wind_directions', 'load_humidity_levels',
            'load_moon_phases']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.humidity_levels import HumidityLevel
from etl.load.models.locations import Location
from etl.load.models.moon_phases import MoonPhase
from etl.load.models.temperature_categories import TemperatureCategory
from etl.load.models.weather import Weather
from etl.load.models.weather_conditions import WeatherCondition
from etl.load.models.wind_directions import WindDirection
from etl.load.models.wind_levels import WindLevel
from etl.utils.utils import insert_data_from_csv

HumidityLevel.__table__.create(bind=engine, checkfirst=True)
TemperatureCategory.__table__.create(bind=engine, checkfirst=True)
WindLevel.__table__.create(bind=engine, checkfirst=True)
WindDirection.__table__.create(bind=engine, checkfirst=True)
WeatherCondition.__table__.create(bind=engine, checkfirst=True)
MoonPhase.__table__.create(bind=engine, checkfirst=True)
Location.__table__.create(bind=engine, checkfirst=True)
Weather.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/weather.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(Weather, csv_file_path, session)
