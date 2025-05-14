# %% tags=["parameters"]

upstream = ['create_humidity_levels']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.humidity_levels import HumidityLevel
from etl.utils.utils import insert_data_from_csv

HumidityLevel.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/humidity_levels.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(HumidityLevel, csv_file_path, session)
