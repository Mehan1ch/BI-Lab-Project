from typing import List

import pandas


def remove_unnecessary_columns(dataframe: pandas.DataFrame, columns: List[str]) -> pandas.DataFrame:
    dataframe.drop(columns=columns, inplace=True)
    return dataframe


def save_to_csv(dataframe: pandas.DataFrame, output_path: str) -> None:
    dataframe.to_csv(output_path, index=False)


def rename_columns(dataframe: pandas.DataFrame, columns: {str: str}) -> pandas.DataFrame:
    return dataframe.rename(columns=columns)


def load_csv(input_path: str) -> pandas.DataFrame:
    return pandas.read_csv(input_path)
