# %% tags=["parameters"]
from typing import List

upstream = ['create_age_groups', 'create_countries']
product: List[str] | None = None
extract_path: str | None = None
transform_path: str | None = None

# %%
from pandas import DataFrame
from etl.transform.utils.utils import load_csv, save_to_csv


def create_country_populations_table(population: DataFrame, age_groups: DataFrame, countries: DataFrame) -> DataFrame:
    # Map country names to their IDs
    country_id_map = countries.set_index('name')['id'].to_dict()

    # Create a mapping of age group names to population column names
    age_group_to_column = {
        "Elders": "65+",
        "Adults": "25-64 years",
        "Teens": "15-24 years",
        "Kids": "5-14 years",
        "Toddlers": "0-4 years"
    }

    # Prepare the output data
    country_populations_data = []

    # Iterate through each country in the population DataFrame
    for _, country_row in population.iterrows():
        country_name = country_row['Country']
        country_id = country_id_map.get(country_name)

        # Skip if the country is not found in the mapping
        if country_id is None:
            continue

        # Iterate through each age group
        for _, age_group_row in age_groups.iterrows():
            age_group_id = age_group_row['id']
            age_group_name = age_group_row['name']
            age_column = age_group_to_column.get(age_group_name)

            # Ensure the age column exists in the population DataFrame
            if age_column not in population.columns:
                continue

            # Get the population amount for the age group
            amount = country_row.get(age_column, 0)

            # Append the row to the output data
            country_populations_data.append({
                "Country_id": country_id,
                "Age_group_id": age_group_id,
                "Amount": amount
            })

    # Create a DataFrame for the country populations table
    country_populations_df = DataFrame(country_populations_data)
    return country_populations_df


population_path = extract_path + "/population/population.csv"
age_groups_path = transform_path + "/migrations/age_groups.csv"
countries_path = transform_path + "/migrations/countries.csv"
population_df: DataFrame = load_csv(population_path)
age_groups_df: DataFrame = load_csv(age_groups_path)
countries_df: DataFrame = load_csv(countries_path)
df: DataFrame = create_country_populations_table(population=population_df, age_groups=age_groups_df,
                                                 countries=countries_df)
save_to_csv(df, product['data'])
