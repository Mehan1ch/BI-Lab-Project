# %% tags=["parameters"]
upstream = ['clean_disease']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.transform.utils.utils import save_to_csv, load_csv


def create_prognosis_table(disease: DataFrame) -> DataFrame:
    # Extract unique names from the disease_df
    unique_names = disease['prognosis'].unique()

    # Create the prognosis table
    prognosis_table = [{"id": idx + 1, "name": name} for idx, name in enumerate(unique_names)]

    # Convert to DataFrame
    prognosis_df = DataFrame(prognosis_table)
    return prognosis_df


disease_path = transform_path + "/clean/disease.csv"
disease_df = load_csv(disease_path)
df: DataFrame = create_prognosis_table(disease_df)
save_to_csv(df, product['data'])
