# %% tags=["parameters"]

upstream = ['create_diagnoses', 'load_age_groups', 'load_temperature_categories',
            'load_humidity_levels', 'load_wind_levels', 'load_prognosis']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

from etl.load.db import SessionLocal, engine
from etl.load.models.age_groups import AgeGroup
from etl.load.models.diagnoses import Diagnosis
from etl.load.models.humidity_levels import HumidityLevel
from etl.load.models.prognosis import Prognosis
from etl.load.models.temperature_categories import TemperatureCategory
from etl.load.models.wind_levels import WindLevel
from etl.utils.utils import insert_data_from_csv

AgeGroup.__table__.create(bind=engine, checkfirst=True)
TemperatureCategory.__table__.create(bind=engine, checkfirst=True)
HumidityLevel.__table__.create(bind=engine, checkfirst=True)
WindLevel.__table__.create(bind=engine, checkfirst=True)
Prognosis.__table__.create(bind=engine, checkfirst=True)
Diagnosis.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/diagnoses.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(Diagnosis, csv_file_path, session)
