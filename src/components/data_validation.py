"""
==========================================================
data_validation.py

Project
-------
Heart Disease Prediction

Description
-----------
Validates the training and testing datasets before
data preprocessing.

Responsibilities
----------------
1. Verify dataset existence.
2. Load training and testing datasets.
3. Validate required columns.
4. Check missing values.
5. Check duplicate records.
6. Validate target column.
7. Validate feature data types.
8. Execute the complete validation workflow.
==========================================================
"""

import sys

from pathlib import Path

import pandas as pd

from src.logger import logger

from src.exception import ProjectException

from src.constants import (
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    TARGET_COLUMN,
    REQUIRED_COLUMNS
)


# ==========================================================
# Data Validation Component
# ==========================================================

class DataValidation:
    """
    Data Validation Component.

    Responsible for validating the training and testing
    datasets before they enter the preprocessing stage.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the Data Validation component.
        """

        logger.info(
            "Data Validation Component Initialized."
        )

    # ======================================================
    # Validate Dataset Existence
    # ======================================================

    def validate_dataset_exists(
        self
    ) -> None:
        """
        Verify that training and testing datasets exist.

        Raises
        ------
        FileNotFoundError
            If either dataset does not exist.
        """

        try:

            logger.info(
                "Checking dataset existence."
            )

            if not Path(
                TRAIN_DATA_PATH
            ).exists():

                raise FileNotFoundError(
                    f"Training dataset not found: "
                    f"{TRAIN_DATA_PATH}"
                )

            if not Path(
                TEST_DATA_PATH
            ).exists():

                raise FileNotFoundError(
                    f"Testing dataset not found: "
                    f"{TEST_DATA_PATH}"
                )

            logger.info(
                "Dataset existence validation completed."
            )

        except Exception as error:

            logger.exception(
                "Dataset existence validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Load Dataset
    # ======================================================

    def load_data(
        self
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load training and testing datasets.

        Returns
        -------
        tuple[pd.DataFrame, pd.DataFrame]
            Training and testing DataFrames.
        """

        try:

            logger.info(
                "Loading training dataset."
            )

            train_df = pd.read_csv(
                TRAIN_DATA_PATH
            )

            logger.info(
                f"Training dataset loaded. "
                f"Shape: {train_df.shape}"
            )

            logger.info(
                "Loading testing dataset."
            )

            test_df = pd.read_csv(
                TEST_DATA_PATH
            )

            logger.info(
                f"Testing dataset loaded. "
                f"Shape: {test_df.shape}"
            )

            return (
                train_df,
                test_df
            )

        except Exception as error:

            logger.exception(
                "Failed to load training and testing datasets."
            )

            raise ProjectException(
                error,
                sys
            ) from error

        # ======================================================
    # Validate Required Columns
    # ======================================================

    def validate_columns(
        self,
        dataframe: pd.DataFrame
    ) -> None:
        """
        Validate that all required dataset columns exist.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Dataset to validate.
        """

        try:

            logger.info(
                "Validating required columns."
            )

            missing_columns = (
                set(REQUIRED_COLUMNS)
                - set(dataframe.columns)
            )

            if missing_columns:

                raise ValueError(
                    "Missing required columns: "
                    f"{sorted(missing_columns)}"
                )

            logger.info(
                "Required column validation completed."
            )

        except Exception as error:

            logger.exception(
                "Required column validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Validate Missing Values
    # ======================================================

    def validate_missing_values(
        self,
        dataframe: pd.DataFrame
    ) -> None:
        """
        Check the dataset for missing values.

        Missing values are reported as warnings because
        missing-value handling is performed later by the
        preprocessing component.
        """

        try:

            logger.info(
                "Checking missing values."
            )

            missing_values = int(
                dataframe.isnull()
                .sum()
                .sum()
            )

            if missing_values > 0:

                logger.warning(
                    f"Missing values found: "
                    f"{missing_values}"
                )

            else:

                logger.info(
                    "No missing values found."
                )

        except Exception as error:

            logger.exception(
                "Missing value validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Validate Duplicate Records
    # ======================================================

    def validate_duplicates(
        self,
        dataframe: pd.DataFrame
    ) -> None:
        """
        Check the dataset for duplicate records.

        Duplicate records are reported as warnings because
        duplicate removal is handled by preprocessing.
        """

        try:

            logger.info(
                "Checking duplicate records."
            )

            duplicate_records = int(
                dataframe.duplicated()
                .sum()
            )

            if duplicate_records > 0:

                logger.warning(
                    f"Duplicate records found: "
                    f"{duplicate_records}"
                )

            else:

                logger.info(
                    "No duplicate records found."
                )

        except Exception as error:

            logger.exception(
                "Duplicate record validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Validate Target Column
    # ======================================================

    def validate_target_column(
        self,
        dataframe: pd.DataFrame
    ) -> None:
        """
        Validate the presence of the target column.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Dataset to validate.
        """

        try:

            logger.info(
                "Validating target column."
            )

            if TARGET_COLUMN not in dataframe.columns:

                raise ValueError(
                    f"Target column "
                    f"'{TARGET_COLUMN}' "
                    f"not found."
                )

            logger.info(
                f"Target column '{TARGET_COLUMN}' "
                f"validation completed."
            )

        except Exception as error:

            logger.exception(
                "Target column validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Validate Data Types
    # ======================================================

    def validate_data_types(
        self,
        dataframe: pd.DataFrame
    ) -> None:
        """
        Log the data types of dataset columns.

        Detailed type correction is performed later
        by the preprocessing component.
        """

        try:

            logger.info(
                "Validating feature data types."
            )

            logger.info(
                "\n%s",
                dataframe.dtypes
            )

            logger.info(
                "Feature data type validation completed."
            )

        except Exception as error:

            logger.exception(
                "Feature data type validation failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error

        # ======================================================
    # Execute Data Validation Pipeline
    # ======================================================

    def initiate_data_validation(
        self
    ) -> bool:
        """
        Execute the complete data validation workflow.

        Returns
        -------
        bool
            True when validation completes successfully.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "DATA VALIDATION PIPELINE STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Dataset Existence
            # ==================================================

            self.validate_dataset_exists()

            # ==================================================
            # Load Datasets
            # ==================================================

            train_df, test_df = self.load_data()

            # ==================================================
            # Training Dataset Validation
            # ==================================================

            logger.info(
                "Validating training dataset."
            )

            self.validate_columns(
                train_df
            )

            self.validate_missing_values(
                train_df
            )

            self.validate_duplicates(
                train_df
            )

            self.validate_target_column(
                train_df
            )

            self.validate_data_types(
                train_df
            )

            logger.info(
                "Training dataset validation completed."
            )

            # ==================================================
            # Testing Dataset Validation
            # ==================================================

            logger.info(
                "Validating testing dataset."
            )

            self.validate_columns(
                test_df
            )

            self.validate_missing_values(
                test_df
            )

            self.validate_duplicates(
                test_df
            )

            self.validate_target_column(
                test_df
            )

            self.validate_data_types(
                test_df
            )

            logger.info(
                "Testing dataset validation completed."
            )

            # ==================================================
            # Validation Completed
            # ==================================================

            logger.info("=" * 70)

            logger.info(
                "DATA VALIDATION PIPELINE COMPLETED"
            )

            logger.info("=" * 70)

            return True

        except Exception as error:

            logger.exception(
                "Data Validation Pipeline Failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error