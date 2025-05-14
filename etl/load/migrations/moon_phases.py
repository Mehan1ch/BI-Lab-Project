# %% tags=["parameters"]
upstream = ['create_moon_phases']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.moon_phases import MoonPhase
from etl.utils.utils import insert_data_from_csv

MoonPhase.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/moon_phases.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(MoonPhase, csv_file_path, session)
