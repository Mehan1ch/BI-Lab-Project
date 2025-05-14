# %% tags=["parameters"]
upstream = ['create_age_groups']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.age_groups import AgeGroup
from etl.utils.utils import insert_data_from_csv

AgeGroup.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/age_groups.csv"

# Open a database session
session = SessionLocal()

# Insert data into the AgeGroup table
insert_data_from_csv(AgeGroup, csv_file_path, session)
