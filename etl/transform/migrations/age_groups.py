# %% tags=["parameters"]
from typing import List

upstream = ['extract']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.utils.utils import load_csv, save_to_csv


def create_age_groups_table(population: DataFrame) -> DataFrame:
    # Extract column names after the first two
    age_columns = population.columns[2:]
    age_group_names = ["Elders", "Adults", "Teens", "Kids", "Toddlers"]

    # Prepare the data for the age groups table
    age_groups_data = []
    for idx, (col, name) in enumerate(zip(age_columns, age_group_names), start=1):
        # Parse the column name to extract the range
        if col == "65+":
            range_start, range_end = 65, None
        else:
            range_parts = col.replace(" years", "").split("-")
            range_start = int(range_parts[0])
            range_end = int(range_parts[1]) if len(range_parts) > 1 else None

        # Append the row to the age groups data
        age_groups_data.append({
            "id": idx,
            "name": name,
            "range_start": range_start,
            "range_end": range_end
        })

    # Create a DataFrame for the age groups table
    age_groups_df = DataFrame(age_groups_data)
    return age_groups_df


population_path = extract_path + "/population/population.csv"
population_df: DataFrame = load_csv(population_path)
df: DataFrame = create_age_groups_table(population_df)
save_to_csv(df, product['data'])
