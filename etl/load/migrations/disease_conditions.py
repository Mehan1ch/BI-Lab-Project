# %% tags=["parameters"]
upstream = ['create_disease_conditions']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from etl.load.db import SessionLocal, engine
from etl.load.models.disease_conditions import DiseaseCondition
from etl.utils.utils import insert_data_from_csv

DiseaseCondition.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/disease_conditions.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(DiseaseCondition, csv_file_path, session)
