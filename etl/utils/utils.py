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


def fix_column_names(dataframe: DataFrame, column: str, replacements: dict) -> DataFrame:
    dataframe[column] = dataframe[column].replace(replacements)
    return dataframe


def remove_quotes_from_columns(dataframe: DataFrame, columns: List[str]) -> DataFrame:
    for column in columns:
        if column in dataframe.columns:
            dataframe[column] = dataframe[column].str.replace('"', '', regex=False)
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
