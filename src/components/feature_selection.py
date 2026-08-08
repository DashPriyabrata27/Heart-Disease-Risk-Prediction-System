"""
==========================================================
feature_selection.py

Project
-------
Heart Disease Prediction

Description
-----------
Selects the required features from the processed training
and testing datasets and separates the feature variables
from the target variable.

Responsibilities
----------------
1. Select the required feature columns.
2. Keep the target column for supervised learning.
3. Separate features and target.
4. Prepare training and testing datasets.
5. Return the prepared datasets to the next
   machine learning pipeline stage.
==========================================================
"""

import sys

import pandas as pd

from src.logger import logger

from src.exception import ProjectException

from src.constants import (
    FEATURE_COLUMNS,
    TARGET_COLUMN
)


# ==========================================================
# Feature Selection Component
# ==========================================================

class FeatureSelection:
    """
    Feature Selection Component.

    Responsible for selecting the required model features
    and separating the feature matrix from the target
    variable.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the Feature Selection component.
        """

        logger.info(
            "Feature Selection Component Initialized."
        )

    # ======================================================
    # Select Features
    # ======================================================

    def select_features(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Select the required features and target column.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input processed dataset.

        Returns
        -------
        pd.DataFrame
            Dataset containing selected features
            and target column.
        """

        try:

            logger.info(
                "Selecting required feature columns."
            )

            selected_columns = (
                FEATURE_COLUMNS
                + [TARGET_COLUMN]
            )

            missing_columns = [
                column
                for column in selected_columns
                if column not in dataframe.columns
            ]

            if missing_columns:

                raise ValueError(
                    "Required feature columns are missing: "
                    f"{missing_columns}"
                )

            selected_dataframe = dataframe[
                selected_columns
            ].copy()

            logger.info(
                "Feature selection completed successfully."
            )

            logger.info(
                f"Selected feature count: "
                f"{len(FEATURE_COLUMNS)}"
            )

            return selected_dataframe

        except Exception as error:

            logger.exception(
                "Failed while selecting features."
            )

            raise ProjectException(
                error,
                sys
            ) from error

        # ======================================================
    # Split Features and Target
    # ======================================================

    def split_features_target(
        self,
        dataframe: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.Series]:
        """
        Separate feature variables and target variable.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Dataset containing selected features
            and target column.

        Returns
        -------
        tuple[pd.DataFrame, pd.Series]
            Feature matrix X and target vector y.
        """

        try:

            logger.info(
                "Separating features and target."
            )

            X = dataframe.drop(
                columns=[TARGET_COLUMN]
            )

            y = dataframe[
                TARGET_COLUMN
            ]

            logger.info(
                "Feature-target separation completed successfully."
            )

            logger.info(
                f"Feature matrix shape: {X.shape}"
            )

            logger.info(
                f"Target vector shape: {y.shape}"
            )

            return X, y

        except Exception as error:

            logger.exception(
                "Failed while separating features and target."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Prepare Single Dataset
    # ======================================================

    def _prepare_dataset(
        self,
        dataframe: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.Series]:
        """
        Execute the complete feature selection process
        for one dataset.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input processed dataset.

        Returns
        -------
        tuple[pd.DataFrame, pd.Series]
            Prepared feature matrix and target vector.
        """

        try:

            logger.info(
                "Preparing dataset for model training."
            )

            dataframe = dataframe.copy()

            dataframe = self.select_features(
                dataframe
            )

            X, y = self.split_features_target(
                dataframe
            )

            logger.info(
                "Dataset prepared successfully."
            )

            return X, y

        except Exception as error:

            logger.exception(
                "Failed while preparing dataset."
            )

            raise ProjectException(
                error,
                sys
            ) from error

        # ======================================================
    # Feature Selection Pipeline
    # ======================================================

    def initiate_feature_selection(
        self,
        train_df: pd.DataFrame,
        test_df: pd.DataFrame
    ) -> dict:
        """
        Execute the complete feature selection pipeline.

        Parameters
        ----------
        train_df : pd.DataFrame
            Preprocessed training dataset.

        test_df : pd.DataFrame
            Preprocessed testing dataset.

        Returns
        -------
        dict
            Prepared training and testing feature
            matrices and target vectors.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "FEATURE SELECTION PIPELINE STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Training Dataset
            # ==================================================

            logger.info(
                "Preparing training dataset."
            )

            X_train, y_train = (
                self._prepare_dataset(
                    train_df
                )
            )

            logger.info(
                "Training dataset prepared successfully."
            )

            # ==================================================
            # Testing Dataset
            # ==================================================

            logger.info(
                "Preparing testing dataset."
            )

            X_test, y_test = (
                self._prepare_dataset(
                    test_df
                )
            )

            logger.info(
                "Testing dataset prepared successfully."
            )

            # ==================================================
            # Final Information
            # ==================================================

            logger.info(
                f"X_train shape: {X_train.shape}"
            )

            logger.info(
                f"X_test shape: {X_test.shape}"
            )

            logger.info(
                f"y_train shape: {y_train.shape}"
            )

            logger.info(
                f"y_test shape: {y_test.shape}"
            )

            logger.info("=" * 70)

            logger.info(
                "FEATURE SELECTION PIPELINE COMPLETED"
            )

            logger.info("=" * 70)

            return {

                "X_train": X_train,

                "X_test": X_test,

                "y_train": y_train,

                "y_test": y_test

            }

        except Exception as error:

            logger.exception(
                "Feature Selection Pipeline Failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error