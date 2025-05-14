# %% tags=["parameters"]
upstream = ['create_prognosis']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from etl.load.db import SessionLocal, engine
from etl.load.models.prognosis import Prognosis
from etl.utils.utils import insert_data_from_csv

Prognosis.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/prognosis.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(Prognosis, csv_file_path, session)
