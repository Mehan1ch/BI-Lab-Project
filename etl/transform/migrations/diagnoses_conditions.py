# %% tags=["parameters"]
upstream = ['clean_disease', 'create_disease_conditions', 'create_diagnoses']
product: list[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame

from etl.utils.utils import load_csv, save_to_csv


def create_diagnoses_conditions_table(disease: DataFrame, disease_conditions: DataFrame,
                                      diagnoses: DataFrame) -> DataFrame:
    # Preprocess condition names: lowercase and replace spaces with underscores
    disease_conditions['name'] = disease_conditions['name'].str.lower().str.replace(' ', '_')

    # Create a mapping of disease condition names to their IDs
    condition_name_to_id = disease_conditions.set_index('name')['id'].to_dict()

    # Prepare the output data
    diagnoses_conditions_data = []

    # Iterate through each diagnosis
    for _, diagnosis_row in diagnoses.iterrows():
        diagnosis_id = diagnosis_row['id']

        # Find the corresponding row in the disease DataFrame
        disease_row = disease.loc[diagnosis_id - 1]  # Assuming the rows are aligned by index

        # Check each disease condition
        for condition_name, condition_id in condition_name_to_id.items():
            if disease_row[condition_name] == 1:
                diagnoses_conditions_data.append({
                    "diagnosis_id": diagnosis_id,
                    "disease_condition_id": condition_id
                })

    # Create a DataFrame for the Diagnoses Conditions table
    diagnoses_conditions_df = DataFrame(diagnoses_conditions_data)
    return diagnoses_conditions_df


disease_path = transform_path + "/clean/disease.csv"
disease_conditions_path = transform_path + "/migrations/disease_conditions.csv"
diagnoses_path = transform_path + "/migrations/diagnoses.csv"
disease_df: DataFrame = load_csv(disease_path)
disease_conditions_df: DataFrame = load_csv(disease_conditions_path)
diagnoses_df: DataFrame = load_csv(diagnoses_path)
df: DataFrame = create_diagnoses_conditions_table(disease=disease_df, disease_conditions=disease_conditions_df,
                                                  diagnoses=diagnoses_df)
save_to_csv(df, product['data'])
