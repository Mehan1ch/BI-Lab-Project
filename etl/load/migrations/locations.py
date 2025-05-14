# %% tags=["parameters"]

upstream = ['create_locations', 'load_timezones', 'load_countries']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.countries import Country
from etl.load.models.locations import Location
from etl.load.models.timezones import Timezone
from etl.utils.utils import insert_data_from_csv

Timezone.__table__.create(bind=engine, checkfirst=True)
Country.__table__.create(bind=engine, checkfirst=True)
Location.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/locations.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(Location, csv_file_path, session)
