# %% tags=["parameters"]

upstream = ['create_countries']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.countries import Country
from etl.utils.utils import insert_data_from_csv

Country.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/countries.csv"

# Open a database session
session = SessionLocal()

# Insert data into the AgeGroup table
insert_data_from_csv(Country, csv_file_path, session)
