"""
==========================================================
utils.py

Project
-------
Heart Disease Prediction

Description
-----------
Provides reusable utility functions used
throughout the project.

Responsibilities
----------------
✓ Create directories
✓ Read CSV files
✓ Save CSV files
✓ Save Python objects
✓ Load Python objects
✓ Save JSON files
✓ Load JSON files
✓ Create DataFrames
==========================================================
"""

import json

import pickle

import sys

from pathlib import Path

from typing import Any

import pandas as pd

from src.exception import ProjectException


# ==========================================================
# Create Directory
# ==========================================================

def create_directory(
    directory: Path
) -> None:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    directory : Path
        Directory path to create.
    """

    try:

        directory.mkdir(

            parents=True,

            exist_ok=True

        )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error


# ==========================================================
# Read CSV File
# ==========================================================

def read_csv(
    file_path: Path
) -> pd.DataFrame:
    """
    Read a CSV file into a DataFrame.

    Parameters
    ----------
    file_path : Path
        Path of the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.
    """

    try:

        return pd.read_csv(

            file_path

        )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error


# ==========================================================
# Save CSV File
# ==========================================================

def save_csv(
    dataframe: pd.DataFrame,
    file_path: Path
) -> None:
    """
    Save a DataFrame as a CSV file.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame to save.

    file_path : Path
        Destination CSV file path.
    """

    try:

        create_directory(

            file_path.parent

        )

        dataframe.to_csv(

            file_path,

            index=False

        )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error

# ==========================================================
# Save Python Object
# ==========================================================

def save_object(
    file_path: Path,
    obj: Any
) -> None:
    """
    Save a Python object using Pickle.

    Parameters
    ----------
    file_path : Path
        Destination file path.

    obj : Any
        Python object to save.
    """

    try:

        create_directory(

            file_path.parent

        )

        with open(

            file_path,

            "wb"

        ) as file:

            pickle.dump(

                obj,

                file

            )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error


# ==========================================================
# Load Python Object
# ==========================================================

def load_object(
    file_path: Path
) -> Any:
    """
    Load a Python object from a Pickle file.

    Parameters
    ----------
    file_path : Path
        Path of the Pickle file.

    Returns
    -------
    Any
        Loaded Python object.
    """

    try:

        with open(

            file_path,

            "rb"

        ) as file:

            return pickle.load(

                file

            )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error

# ==========================================================
# Save JSON File
# ==========================================================

def save_json(
    file_path: Path,
    data: dict
) -> None:
    """
    Save dictionary data as a JSON file.

    Parameters
    ----------
    file_path : Path
        Destination JSON file path.

    data : dict
        Dictionary data to save.
    """

    try:

        create_directory(

            file_path.parent

        )

        with open(

            file_path,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

                ensure_ascii=False

            )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error


# ==========================================================
# Load JSON File
# ==========================================================

def load_json(
    file_path: Path
) -> dict:
    """
    Load data from a JSON file.

    Parameters
    ----------
    file_path : Path
        Path of the JSON file.

    Returns
    -------
    dict
        Loaded JSON data.
    """

    try:

        with open(

            file_path,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(

                file

            )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error


# ==========================================================
# Create DataFrame
# ==========================================================

def create_dataframe(
    data: dict
) -> pd.DataFrame:
    """
    Convert a dictionary into a single-row DataFrame.

    Parameters
    ----------
    data : dict
        Dictionary containing feature values.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the provided data.
    """

    try:

        return pd.DataFrame(

            [data]

        )

    except Exception as error:

        raise ProjectException(

            error,

            sys

        ) from error