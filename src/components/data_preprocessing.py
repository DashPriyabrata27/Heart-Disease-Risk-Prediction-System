"""
==========================================================
data_preprocessing.py

Project
-------
Heart Disease Prediction

Description
-----------
Performs data preprocessing before model
training.

Responsibilities
----------------
✓ Handle missing values
✓ Remove duplicate records
✓ Correct feature data types
✓ Validate feature values
==========================================================
"""

import sys

import pandas as pd

from src.logger import logger

from src.exception import ProjectException

from src.constants import (

    MIN_HEIGHT,
    MAX_HEIGHT,
    MIN_WEIGHT,
    MAX_WEIGHT

)


# ==========================================================
# Data Preprocessing Component
# ==========================================================

class DataPreprocessing:
    """
    Performs preprocessing on the training
    and testing datasets before they are
    passed to the next stage of the
    machine learning pipeline.
    """

    # ======================================================
    # Handle Missing Values
    # ======================================================

    def handle_missing_values(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Handle missing values.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataset.

        Returns
        -------
        pd.DataFrame
            Dataset with missing values handled.
        """

        try:

            logger.info(

                "Handling missing values."

            )

            numerical_columns = dataframe.select_dtypes(

                include=[

                    "int64",

                    "float64"

                ]

            ).columns

            categorical_columns = dataframe.select_dtypes(

                include=[

                    "object",

                    "category"

                ]

            ).columns

            # ==============================================
            # Numerical Features
            # ==============================================

            for column in numerical_columns:

                dataframe[column] = dataframe[column].fillna(

                    dataframe[column].median()

                )

            # ==============================================
            # Categorical Features
            # ==============================================

            for column in categorical_columns:

                dataframe[column] = dataframe[column].fillna(

                    dataframe[column].mode()[0]

                )

            logger.info(

                "Missing values handled successfully."

            )

            return dataframe

        except Exception as error:

            logger.exception(

                "Failed while handling missing values."

            )

            raise ProjectException(

                error,

                sys

            ) from error

    # ======================================================
    # Remove Duplicate Records
    # ======================================================

    def remove_duplicates(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Remove duplicate records.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataset.

        Returns
        -------
        pd.DataFrame
            Dataset after duplicate removal.
        """

        try:

            duplicate_count = dataframe.duplicated().sum()

            logger.info(

                f"Duplicate records found: {duplicate_count}"

            )

            dataframe = dataframe.drop_duplicates()

            dataframe.reset_index(

                drop=True,

                inplace=True

            )

            logger.info(

                "Duplicate records removed successfully."

            )

            return dataframe

        except Exception as error:

            logger.exception(

                "Failed while removing duplicate records."

            )

            raise ProjectException(

                error,

                sys

            ) from error
            # ======================================================
    # Correct Data Types
    # ======================================================

    def correct_data_types(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Correct feature data types.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataset.

        Returns
        -------
        pd.DataFrame
            Dataset with corrected data types.
        """

        try:

            logger.info(

                "Correcting feature data types."

            )

            dataframe["age"] = dataframe["age"].astype(

                int

            )

            dataframe["height"] = dataframe["height"].astype(

                int

            )

            dataframe["weight"] = dataframe["weight"].astype(

                float

            )

            dataframe["ap_hi"] = dataframe["ap_hi"].astype(

                int

            )

            dataframe["ap_lo"] = dataframe["ap_lo"].astype(

                int

            )

            logger.info(

                "Feature data types corrected successfully."

            )

            return dataframe

        except Exception as error:

            logger.exception(

                "Failed while correcting feature data types."

            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Validate Feature Values
    # ======================================================

    def validate_feature_values(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Validate feature values.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataset.

        Returns
        -------
        pd.DataFrame
            Dataset after removing invalid records.
        """

        try:

            logger.info(

                "Validating feature values."

            )

            dataframe = dataframe[

                (dataframe["age"] > 0)

                &

                (

                    dataframe["height"].between(

                        MIN_HEIGHT,

                        MAX_HEIGHT

                    )

                )

                &

                (

                    dataframe["weight"].between(

                        MIN_WEIGHT,

                        MAX_WEIGHT

                    )

                )

                &

                (dataframe["ap_hi"] > 0)

                &

                (dataframe["ap_lo"] > 0)

                &

                (

                    dataframe["ap_hi"]

                    >

                    dataframe["ap_lo"]

                )

            ]

            dataframe.reset_index(

                drop=True,

                inplace=True

            )

            logger.info(

                "Feature value validation completed successfully."

            )

            return dataframe

        except Exception as error:

            logger.exception(

                "Failed while validating feature values."

            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Preprocess Single Dataset
    # ======================================================

    def _preprocess_dataframe(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Apply all preprocessing steps to a
        single dataset.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataset.

        Returns
        -------
        pd.DataFrame
            Fully preprocessed dataset.
        """

        try:

            logger.info(

                "Preprocessing dataset."

            )

            dataframe = dataframe.copy()

            dataframe = self.handle_missing_values(

                dataframe

            )

            dataframe = self.remove_duplicates(

                dataframe

            )

            dataframe = self.correct_data_types(

                dataframe

            )

            dataframe = self.validate_feature_values(

                dataframe

            )

            logger.info(

                "Dataset preprocessing completed."

            )

            return dataframe

        except Exception as error:

            logger.exception(

                "Failed while preprocessing dataset."

            )

            raise ProjectException(

                error,

                sys

            ) from error
        
    # ======================================================
    # Execute Data Preprocessing Pipeline
    # ======================================================

    def initiate_data_preprocessing(
        self,
        train_df: pd.DataFrame,
        test_df: pd.DataFrame
    ) -> dict[str, pd.DataFrame]:
        """
        Execute the complete data preprocessing
        pipeline.

        Parameters
        ----------
        train_df : pd.DataFrame
            Training dataset.

        test_df : pd.DataFrame
            Testing dataset.

        Returns
        -------
        dict[str, pd.DataFrame]
            Dictionary containing the
            preprocessed training and
            testing datasets.
        """

        try:

            logger.info(

                "=" * 70

            )

            logger.info(

                "DATA PREPROCESSING PIPELINE STARTED"

            )

            logger.info(

                "=" * 70

            )

            # ==================================================
            # Preprocess Training Dataset
            # ==================================================

            logger.info(

                "Preprocessing training dataset."

            )

            train_df = self._preprocess_dataframe(

                train_df

            )

            logger.info(

                "Training dataset preprocessed successfully."

            )

            # ==================================================
            # Preprocess Testing Dataset
            # ==================================================

            logger.info(

                "Preprocessing testing dataset."

            )

            test_df = self._preprocess_dataframe(

                test_df

            )

            logger.info(

                "Testing dataset preprocessed successfully."

            )

            # ==================================================
            # Data Preprocessing Completed
            # ==================================================

            logger.info(

                "=" * 70

            )

            logger.info(

                "DATA PREPROCESSING PIPELINE COMPLETED"

            )

            logger.info(

                "=" * 70

            )

            return {

                "train_df": train_df,

                "test_df": test_df

            }

        except Exception as error:

            logger.exception(

                "Data preprocessing pipeline failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error