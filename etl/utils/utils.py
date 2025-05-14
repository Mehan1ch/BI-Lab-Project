from typing import List

import pandas
from pandas import DataFrame
from sqlalchemy.orm import Session


def remove_unnecessary_columns(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    dataframe.drop(columns=columns, inplace=True)
    return dataframe


def save_to_csv(dataframe: DataFrame, output_path: str) -> None:
    dataframe.to_csv(output_path, index=False)


def rename_columns(dataframe: DataFrame, columns: {str: str}) -> DataFrame:
    return dataframe.rename(columns=columns)


def load_csv(input_path: str) -> DataFrame:
    return pandas.read_csv(input_path)


def replace_column_content(dataframe: DataFrame, column: str, replacements: dict) -> DataFrame:
    dataframe[column] = dataframe[column].replace(replacements)
    return dataframe


def remove_quotes_from_columns(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    for column in columns:
        if column in dataframe.columns:
            dataframe[column] = dataframe[column].str.replace('"', '', regex=False)
    return dataframe


def convert_to_24_hour_format(time_str: str) -> str:
    """
    Converts a 12-hour time format string to a 24-hour format string.

    :param time_str: Time string in 12-hour format (e.g., "02:30 PM")
    :return: Time string in 24-hour format (e.g., "14:30")
    """
    if not time_str:
        return None
    try:
        return pandas.to_datetime(time_str).strftime('%H:%M')
    except ValueError:
        return None


def convert_column_to_time(dataframe: DataFrame, column: str) -> DataFrame:
    """
    Converts a specified column in the DataFrame to a time format.

    :param callable:
    :param dataframe: Input DataFrame
    :param column: Column name to convert
    :return: DataFrame with the specified column converted to time format
    """
    if column in dataframe.columns:
        dataframe[column] = dataframe[column].apply(convert_to_24_hour_format)
    return dataframe


def insert_data_from_csv(model, csv_file_path: str, session: Session):
    """
    Inserts data from a CSV file into the database for a given model.

    :param model: SQLAlchemy model class
    :param csv_file_path: Path to the CSV file
    :param session: SQLAlchemy session
    """
    try:
        # Load the CSV file using the utility method
        data_df = load_csv(csv_file_path)

        # Iterate through each row in the DataFrame
        for _, row in data_df.iterrows():
            # Create a model instance dynamically
            instance = model(**{
                column: (None if pandas.isna(row[column]) else row[column])
                for column in row.index
                if hasattr(model, column)
            })

            # Add the instance to the session
            session.add(instance)

        # Commit the transaction
        session.commit()
        print(f"Data successfully inserted into the {model.__tablename__} table.")
    except Exception as e:
        # Rollback in case of an error
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()
