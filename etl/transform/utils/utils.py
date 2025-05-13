from typing import List

import pandas
from pandas import DataFrame


def remove_unnecessary_columns(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    dataframe.drop(columns=columns, inplace=True)
    return dataframe


def save_to_csv(dataframe: DataFrame, output_path: str) -> None:
    dataframe.to_csv(output_path, index=False)


def rename_columns(dataframe: DataFrame, columns: {str: str}) -> DataFrame:
    return dataframe.rename(columns=columns)


def load_csv(input_path: str) -> DataFrame:
    return pandas.read_csv(input_path)


def fix_column_names(dataframe: DataFrame, column: str, replacements: dict) -> DataFrame:
    dataframe[column] = dataframe[column].replace(replacements)
    return dataframe


def remove_quotes_from_columns(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    for column in columns:
        if column in dataframe.columns:
            dataframe[column] = dataframe[column].str.replace('"', '', regex=False)
    return dataframe
