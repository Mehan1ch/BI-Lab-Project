# %% tags=["parameters"]

upstream = ['create_diagnoses_conditions', 'load_diagnoses', 'load_disease_conditions']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.diagnoses import Diagnosis
from etl.load.models.diagnoses_conditions import DiagnosisCondition
from etl.load.models.disease_conditions import DiseaseCondition
from etl.utils.utils import insert_data_from_csv

DiseaseCondition.__table__.create(bind=engine, checkfirst=True)
Diagnosis.__table__.create(bind=engine, checkfirst=True)
DiagnosisCondition.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/diagnoses_conditions.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(DiagnosisCondition, csv_file_path, session)
