# %% tags=["parameters"]
upstream = ['create_timezones']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from etl.load.db import SessionLocal, engine
from etl.load.models.timezones import Timezone
from etl.utils.utils import insert_data_from_csv

Timezone.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/timezones.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(Timezone, csv_file_path, session)
