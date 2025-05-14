# %% tags=["parameters"]

upstream = ['create_wind_levels']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.wind_levels import WindLevel
from etl.utils.utils import insert_data_from_csv

WindLevel.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/wind_levels.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(WindLevel, csv_file_path, session)
