# %% tags=["parameters"]

upstream = ['create_country_populations', 'load_age_groups', 'load_countries']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from etl.load.db import SessionLocal, engine
from etl.load.models.age_groups import AgeGroup
from etl.load.models.countries import Country
from etl.load.models.country_populations import CountryPopulation
from etl.utils.utils import insert_data_from_csv

AgeGroup.__table__.create(bind=engine, checkfirst=True)
Country.__table__.create(bind=engine, checkfirst=True)
CountryPopulation.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/country_populations.csv"

# Open a database session
session = SessionLocal()

insert_data_from_csv(CountryPopulation, csv_file_path, session)
