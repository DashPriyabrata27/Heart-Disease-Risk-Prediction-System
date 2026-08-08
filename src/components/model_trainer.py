"""
==========================================================
model_trainer.py

Project
-------
Heart Disease Prediction

Description
-----------
Builds the preprocessing pipeline, preprocesses the
feature datasets, trains multiple machine learning models,
compares their performance, and identifies the best
baseline model.

Research-Aligned Methodology
----------------------------
1. Receive the selected training and testing features.
2. Convert categorical feature values into numerical values.
3. Keep numerical features only.
4. Standardize features using StandardScaler.
5. Train multiple machine learning classification models.
6. Compare model performance.
7. Select the best baseline model.
8. Save the best model.
9. Save the baseline SVM for hyperparameter tuning.

Responsibilities
----------------
✓ Build preprocessing pipeline
✓ Preprocess training and testing datasets
✓ Train multiple machine learning models
✓ Compare model performance
✓ Select the best baseline model
✓ Save best model
✓ Save baseline SVM
==========================================================
"""

import sys

import numpy as np

import pandas as pd

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import GaussianNB

from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from xgboost import XGBClassifier

from src.logger import logger

from src.exception import ProjectException

from src.utils import save_object

from src.constants import (
    PREPROCESSOR_PATH,
    BASELINE_MODEL_PATH,
    BEST_MODEL_PATH,
    RANDOM_STATE,
    TARGET_COLUMN
)


# ==========================================================
# Model Trainer Component
# ==========================================================

class ModelTrainer:
    """
    Builds the preprocessing pipeline,
    trains multiple machine learning
    models, and selects the best
    baseline model.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(
        self
    ) -> None:
        """
        Initialize the Model Trainer.
        """

        logger.info(
            "Model Trainer Component Initialized."
        )

        self.preprocessor = (
            self.build_preprocessor()
        )

        # --------------------------------------------------
        # Stores the baseline SVM model.
        #
        # This model is required by the
        # Hyperparameter Tuning component.
        # --------------------------------------------------

        self.baseline_svm = None

    # ======================================================
    # Build Preprocessing Pipeline
    # ======================================================

    def build_preprocessor(
        self
    ) -> Pipeline:
        """
        Build the preprocessing pipeline.

        StandardScaler is used according
        to the research methodology.

        Returns
        -------
        Pipeline
            Configured preprocessing pipeline.
        """

        try:

            logger.info(
                "Building preprocessing pipeline."
            )

            preprocessor = Pipeline(

                steps=[

                    (
                        "scaler",

                        StandardScaler()

                    )

                ]

            )

            logger.info(
                "Preprocessing pipeline built successfully."
            )

            return preprocessor

        except Exception as error:

            logger.exception(
                "Failed to build preprocessing pipeline."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Preprocess Dataset
    # ======================================================

    def preprocess_data(
        self,
        X_train: pd.DataFrame,
        X_test: pd.DataFrame
    ) -> tuple:
        """
        Preprocess training and testing
        feature datasets.

        Research methodology
        --------------------
        • Factorize categorical features.
        • Keep numerical features.
        • Fit StandardScaler only on training data.
        • Transform testing data using the same scaler.

        Parameters
        ----------
        X_train : pd.DataFrame
            Training feature dataset.

        X_test : pd.DataFrame
            Testing feature dataset.

        Returns
        -------
        tuple
            Preprocessed training and
            testing feature datasets.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "PREPROCESSING FEATURE DATASETS"
            )

            logger.info("=" * 70)

            # ==================================================
            # Copy Input Data
            # ==================================================

            X_train = X_train.copy()

            X_test = X_test.copy()

            # ==================================================
            # Categorical Features
            # ==================================================

            categorical_features = [

                "bp_category",

                "bp_category_encoded"

            ]

            # ==================================================
            # Factorize Categorical Features
            # ==================================================

            for feature in categorical_features:

                if feature not in X_train.columns:

                    continue

                logger.info(
                    f"Factorizing categorical feature: "
                    f"{feature}"
                )

                # ----------------------------------------------
                # Training Values
                # ----------------------------------------------

                train_values = (

                    X_train[feature]
                    .astype(str)

                )

                # ----------------------------------------------
                # IMPORTANT
                #
                # pd.factorize() returns:
                #
                #     codes, uniques
                #
                # ----------------------------------------------

                train_codes, categories = (

                    pd.factorize(
                        train_values
                    )

                )

                # ----------------------------------------------
                # Assign Training Codes
                # ----------------------------------------------

                X_train[feature] = (

                    train_codes

                )

                # ----------------------------------------------
                # Create Mapping
                # ----------------------------------------------

                category_mapping = {

                    category: index

                    for index, category
                    in enumerate(categories)

                }

                # ----------------------------------------------
                # Transform Test Data Using
                # Training Mapping
                # ----------------------------------------------

                if feature in X_test.columns:

                    test_values = (

                        X_test[feature]
                        .astype(str)

                    )

                    X_test[feature] = (

                        test_values
                        .map(category_mapping)
                        .fillna(-1)
                        .astype(int)

                    )

            # ==================================================
            # Keep Numerical Columns
            # ==================================================

            X_train = X_train.select_dtypes(

                include=[np.number]

            )

            X_test = X_test.select_dtypes(

                include=[np.number]

            )

            # ==================================================
            # Remove Target Column If Present
            # ==================================================

            if TARGET_COLUMN in X_train.columns:

                X_train = X_train.drop(

                    columns=[TARGET_COLUMN]

                )

            if TARGET_COLUMN in X_test.columns:

                X_test = X_test.drop(

                    columns=[TARGET_COLUMN]

                )

            # ==================================================
            # Align Test Columns
            # ==================================================

            X_test = X_test.reindex(

                columns=X_train.columns,

                fill_value=0

            )

            # ==================================================
            # Log Shapes
            # ==================================================

            logger.info(

                f"Training features before scaling: "
                f"{X_train.shape}"

            )

            logger.info(

                f"Testing features before scaling: "
                f"{X_test.shape}"

            )

            # ==================================================
            # Fit Scaler on Training Data
            # ==================================================

            logger.info(

                "Fitting StandardScaler on training data."

            )

            X_train_processed = (

                self.preprocessor.fit_transform(

                    X_train

                )

            )

            logger.info(

                "Training data scaled successfully."

            )

            # ==================================================
            # Transform Testing Data
            # ==================================================

            logger.info(

                "Transforming testing data."

            )

            X_test_processed = (

                self.preprocessor.transform(

                    X_test

                )

            )

            logger.info(

                "Testing data scaled successfully."

            )

            # ==================================================
            # Save Preprocessor
            # ==================================================

            save_object(

                file_path=PREPROCESSOR_PATH,

                obj=self.preprocessor

            )

            logger.info(

                f"Preprocessor saved successfully at: "
                f"{PREPROCESSOR_PATH}"

            )

            logger.info(

                f"Scaled training shape: "
                f"{X_train_processed.shape}"

            )

            logger.info(

                f"Scaled testing shape: "
                f"{X_test_processed.shape}"

            )

            logger.info("=" * 70)

            return (

                X_train_processed,

                X_test_processed

            )

        except Exception as error:

            logger.exception(

                "Dataset preprocessing failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error

    # ======================================================
    # Train and Evaluate Models
    # ======================================================

    def train_and_evaluate_models(
        self,
        X_train,
        X_test,
        y_train: pd.Series,
        y_test: pd.Series
    ) -> tuple:
        """
        Train multiple machine learning
        models and identify the best
        baseline model.

        Models
        ------
        • Logistic Regression
        • Decision Tree
        • Random Forest
        • Support Vector Machine
        • K-Nearest Neighbors
        • Naive Bayes
        • XGBoost

        Returns
        -------
        tuple
            Best model name,
            best model object,
            model evaluation results.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "MODEL TRAINING STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Initialize Models
            # ==================================================

            models = {

                "Logistic Regression":

                    LogisticRegression(

                        random_state=RANDOM_STATE,

                        max_iter=1000

                    ),

                "Decision Tree":

                    DecisionTreeClassifier(

                        random_state=RANDOM_STATE

                    ),

                "Random Forest":

                    RandomForestClassifier(

                        random_state=RANDOM_STATE

                    ),

                "Support Vector Machine":

                    SVC(

                        random_state=RANDOM_STATE,

                    ),
                    
                "K-Nearest Neighbors":

                    KNeighborsClassifier(),

                "Naive Bayes":

                    GaussianNB(),

                "XGBoost":

                    XGBClassifier(

                        random_state=RANDOM_STATE,

                        eval_metric="logloss"

                    )

            }

            # ==================================================
            # Results
            # ==================================================

            model_results = {}

            best_model = None

            best_model_name = None

            best_accuracy = -1.0

            # ==================================================
            # Train Models
            # ==================================================

            for model_name, model in models.items():

                logger.info(
                    f"Training {model_name}."
                )

                # ----------------------------------------------
                # Train Model
                # ----------------------------------------------

                model.fit(

                    X_train,

                    y_train

                )

                # ----------------------------------------------
                # Store Baseline SVM
                # ----------------------------------------------

                if model_name == (
                    "Support Vector Machine"
                ):

                    self.baseline_svm = model

                    logger.info(

                        "Baseline SVM model stored "
                        "for hyperparameter tuning."

                    )

                # ----------------------------------------------
                # Generate Predictions
                # ----------------------------------------------

                predictions = model.predict(

                    X_test

                )

                # ----------------------------------------------
                # Calculate Metrics
                # ----------------------------------------------

                accuracy = accuracy_score(

                    y_test,

                    predictions

                )

                precision = precision_score(

                    y_test,

                    predictions,

                    zero_division=0

                )

                recall = recall_score(

                    y_test,

                    predictions,

                    zero_division=0

                )

                f1 = f1_score(

                    y_test,

                    predictions,

                    zero_division=0

                )

                # ----------------------------------------------
                # Store Results
                # ----------------------------------------------

                model_results[model_name] = {

                    "Accuracy": accuracy,

                    "Precision": precision,

                    "Recall": recall,

                    "F1 Score": f1

                }

                # ----------------------------------------------
                # Log Results
                # ----------------------------------------------

                logger.info(

                    f"{model_name} | "

                    f"Accuracy: {accuracy:.4f} | "

                    f"Precision: {precision:.4f} | "

                    f"Recall: {recall:.4f} | "

                    f"F1 Score: {f1:.4f}"

                )

                # ----------------------------------------------
                # Select Best Model
                # ----------------------------------------------

                if accuracy > best_accuracy:

                    best_accuracy = accuracy

                    best_model = model

                    best_model_name = model_name

            # ==================================================
            # Validate Models
            # ==================================================

            if best_model is None:

                raise RuntimeError(

                    "No machine learning model "
                    "was successfully trained."

                )

            if self.baseline_svm is None:

                raise RuntimeError(

                    "Baseline SVM model was not trained."

                )

            # ==================================================
            # Best Model Information
            # ==================================================

            logger.info("=" * 70)

            logger.info(

                f"Best Baseline Model: "
                f"{best_model_name}"

            )

            logger.info(

                f"Best Baseline Accuracy: "
                f"{best_accuracy:.4f}"

            )

            logger.info("=" * 70)

            return (

                best_model_name,

                best_model,

                model_results

            )

        except Exception as error:

            logger.exception(

                "Model training failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error

    # ======================================================
    # Save Best Model
    # ======================================================

    def save_best_model(
        self,
        best_model
    ) -> None:
        """
        Save the best baseline model and
        the baseline SVM model.

        The baseline SVM is saved separately
        because the Hyperparameter Tuning
        component loads it using
        BASELINE_MODEL_PATH.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "SAVING BASELINE MODELS"
            )

            logger.info("=" * 70)

            # ==================================================
            # Save Best Overall Model
            # ==================================================

            save_object(

                file_path=BEST_MODEL_PATH,

                obj=best_model

            )

            logger.info(

                f"Best model saved successfully at: "
                f"{BEST_MODEL_PATH}"

            )

            # ==================================================
            # Validate Baseline SVM
            # ==================================================

            if self.baseline_svm is None:

                raise RuntimeError(

                    "Baseline SVM is not available "
                    "for saving."

                )

            # ==================================================
            # Save Baseline SVM
            # ==================================================

            save_object(

                file_path=BASELINE_MODEL_PATH,

                obj=self.baseline_svm

            )

            logger.info(

                f"Baseline SVM saved successfully at: "
                f"{BASELINE_MODEL_PATH}"

            )

            logger.info("=" * 70)

        except Exception as error:

            logger.exception(

                "Failed to save baseline models."

            )

            raise ProjectException(

                error,

                sys

            ) from error

    # ======================================================
    # Execute Model Training Pipeline
    # ======================================================

    def initiate_model_trainer(
        self,
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series
    ) -> dict:
        """
        Execute the complete model training
        pipeline.

        Parameters
        ----------
        X_train : pd.DataFrame
            Training feature dataset.

        X_test : pd.DataFrame
            Testing feature dataset.

        y_train : pd.Series
            Training target.

        y_test : pd.Series
            Testing target.

        Returns
        -------
        dict
            Dictionary containing the best model,
            evaluation results, and processed datasets.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "MODEL TRAINING PIPELINE STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Preprocess Datasets
            # ==================================================

            (
                X_train_processed,

                X_test_processed

            ) = self.preprocess_data(

                X_train,

                X_test

            )

            # ==================================================
            # Train and Evaluate Models
            # ==================================================

            (
                best_model_name,

                best_model,

                model_results

            ) = self.train_and_evaluate_models(

                X_train_processed,

                X_test_processed,

                y_train,

                y_test

            )

            # ==================================================
            # Save Models
            # ==================================================

            self.save_best_model(

                best_model

            )

            # ==================================================
            # Pipeline Completed
            # ==================================================

            logger.info("=" * 70)

            logger.info(
                "MODEL TRAINING PIPELINE COMPLETED"
            )

            logger.info("=" * 70)

            return {

                "best_model_name":
                    best_model_name,

                "best_model":
                    best_model,

                "model_results":
                    model_results,

                "X_train":
                    X_train_processed,

                "X_test":
                    X_test_processed,

                "y_train":
                    y_train,

                "y_test":
                    y_test

            }

        except Exception as error:

            logger.exception(

                "Model training pipeline failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error