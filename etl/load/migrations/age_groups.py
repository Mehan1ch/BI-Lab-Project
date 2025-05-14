# %% tags=["parameters"]
upstream = ['create_age_groups']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%

import pandas

from etl.load.db import SessionLocal, engine
from etl.load.models.age_groups import AgeGroup
from etl.utils.utils import load_csv

# Ensure the tables are created in the database
AgeGroup.__table__.create(bind=engine, checkfirst=True)

# Path to the CSV file
csv_file_path = transform_path + "/migrations/age_groups.csv"

# Open a database session
session = SessionLocal()

try:
    # Load the CSV file using the utility method
    age_groups_df = load_csv(csv_file_path)

    # Iterate through each row in the DataFrame
    for _, row in age_groups_df.iterrows():
        # Create an AgeGroup instance
        age_group = AgeGroup(
            id=int(row['id']),
            name=row['name'],
            range_start=float(row['range_start']) if not pandas.isna(row['range_start']) else None,
            range_end=float(row['range_end']) if not pandas.isna(row['range_end']) else None
        )

        # Add the instance to the session
        session.add(age_group)

    # Commit the transaction
    session.commit()
    print("Data successfully inserted into the database.")
except Exception as e:
    # Rollback in case of an error
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the session
    session.close()
