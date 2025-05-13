# %% tags=["parameters"]
upstream = ['extract']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.transform.utils.utils import save_to_csv, load_csv


def create_disease_conditions_table(disease: DataFrame) -> DataFrame:
    # Extract column names after the first five columns
    conditions_columns = disease.columns[5:]
    # Sort the column names
    sorted_conditions_columns = sorted(conditions_columns)

    # Format each column name: capitalize the first word and replace underscores with spaces
    formatted_conditions = [
        col.replace('_', ' ').capitalize() for col in conditions_columns
    ]

    # Create the Disease Conditions table
    disease_conditions_table = [{"id": idx + 1, "name": col} for idx, col in enumerate(formatted_conditions)]

    # Convert to DataFrame
    disease_conditions_df = DataFrame(disease_conditions_table)
    return disease_conditions_df


disease_path = transform_path + "/clean/disease.csv"
disease_df = load_csv(disease_path)
df: DataFrame = create_disease_conditions_table(disease_df)
save_to_csv(df, product['data'])
