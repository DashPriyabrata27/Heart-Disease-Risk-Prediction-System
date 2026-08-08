"""
==========================================================
data_ingestion.py

Project
-------
Heart Disease Prediction

Description
-----------
Loads the raw dataset, splits it into
training and testing datasets, and saves
the processed datasets for the training
pipeline.

Responsibilities
----------------
✓ Load raw dataset
✓ Split dataset into train and test sets
✓ Save processed datasets
✓ Return dataset locations
==========================================================
"""

import os
import sys

import pandas as pd

from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import ProjectException

from src.constants import (
    RAW_DATA_PATH,
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    TEST_SIZE,
    RANDOM_STATE
)


# ==========================================================
# Data Ingestion Component
# ==========================================================

class DataIngestion:
    """
    Handles loading, splitting, and saving
    datasets used during model training.
    """

    # ======================================================
    # Load Raw Dataset
    # ======================================================

    def load_data(self) -> pd.DataFrame:
        """
        Load the raw dataset.

        Returns
        -------
        pd.DataFrame
            Raw dataset.
        """

        try:

            logger.info(
                "Loading raw dataset."
            )

            dataframe = pd.read_csv(
                RAW_DATA_PATH
            )

            logger.info(
                f"Dataset loaded successfully. "
                f"Shape: {dataframe.shape}"
            )

            return dataframe

        except Exception as error:

            logger.exception(
                "Failed to load raw dataset."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Split Dataset
    # ======================================================

    def split_data(
        self,
        dataframe: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Split dataset into training and
        testing datasets.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Complete dataset.

        Returns
        -------
        tuple[pd.DataFrame, pd.DataFrame]
            Training and testing datasets.
        """

        try:

            logger.info(
                "Splitting dataset."
            )

            train_df, test_df = train_test_split(

                dataframe,

                test_size=TEST_SIZE,

                random_state=RANDOM_STATE,

                shuffle=True

            )

            logger.info(
                f"Training dataset shape : {train_df.shape}"
            )

            logger.info(
                f"Testing dataset shape : {test_df.shape}"
            )

            return train_df, test_df

        except Exception as error:

            logger.exception(
                "Failed to split dataset."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Save Processed Dataset
    # ======================================================

    def save_data(
        self,
        train_df: pd.DataFrame,
        test_df: pd.DataFrame
    ) -> None:
        """
        Save processed datasets.

        Parameters
        ----------
        train_df : pd.DataFrame
            Training dataset.

        test_df : pd.DataFrame
            Testing dataset.
        """

        try:

            logger.info(
                "Saving processed datasets."
            )

            os.makedirs(

                os.path.dirname(
                    TRAIN_DATA_PATH
                ),

                exist_ok=True

            )

            train_df.to_csv(

                TRAIN_DATA_PATH,

                index=False

            )

            test_df.to_csv(

                TEST_DATA_PATH,

                index=False

            )

            logger.info(
                "Processed datasets saved successfully."
            )

            logger.info(
                f"Training Dataset : {TRAIN_DATA_PATH}"
            )

            logger.info(
                f"Testing Dataset  : {TEST_DATA_PATH}"
            )

        except Exception as error:

            logger.exception(
                "Failed to save processed datasets."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Execute Data Ingestion Pipeline
    # ======================================================

    def initiate_data_ingestion(
        self
    ) -> dict[str, str]:
        """
        Execute the complete data ingestion
        pipeline.

        Returns
        -------
        dict[str, str]
            Dictionary containing the
            processed dataset paths.
        """

        try:

            logger.info("=" * 70)
            logger.info(
                "DATA INGESTION PIPELINE STARTED"
            )
            logger.info("=" * 70)

            dataframe = self.load_data()

            train_df, test_df = self.split_data(
                dataframe
            )

            self.save_data(
                train_df,
                test_df
            )

            logger.info("=" * 70)
            logger.info(
                "DATA INGESTION PIPELINE COMPLETED"
            )
            logger.info("=" * 70)

            return {

                "train_data_path": TRAIN_DATA_PATH,

                "test_data_path": TEST_DATA_PATH

            }

        except Exception as error:

            logger.exception(
                "Data ingestion pipeline failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error