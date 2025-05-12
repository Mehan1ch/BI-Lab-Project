# %% tags=["parameters"]
upstream = None
product = None
extract_path: str | None = None

# %%
import json
import os

from dotenv import load_dotenv

load_dotenv()

# Import kaggle credentials from .env file
KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")

import kaggle

kaggle.api.authenticate()

# Create the directory if it does not exist
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Load dataset information from JSON
with open("datasets.json", "r") as file:
    datasets = json.load(file)

for dataset in datasets:
    dataset_name = dataset["name"]
    dataset_path = os.path.join(extract_path, dataset["path"])
    alias = dataset["alias"]

    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    kaggle.api.dataset_download_files(dataset_name, path=dataset_path, unzip=True)

    for file in os.listdir(dataset_path):
        if file.endswith(".csv"):
            original_file_path = os.path.join(dataset_path, file)
            alias_file_path = os.path.join(dataset_path, alias + ".csv")
            os.rename(original_file_path, alias_file_path)
            break
