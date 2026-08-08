"""
==========================================================
hyperparameter_tuning.py


Project
-------
Heart Disease Prediction


Description
-----------
Performs hyperparameter optimization of the baseline
Support Vector Machine (SVM) model using RandomizedSearchCV.

The implementation follows the research configuration:

    n_iter = 4
    cv = 5
    scoring = "accuracy"
    random_state = 42
    n_jobs = -1
    verbose = 2

A stratified tuning subset is used for hyperparameter
optimization to keep the tuning process computationally
efficient while preserving class distribution.

Responsibilities
----------------
1. Load the baseline SVM model.
2. Define the SVM hyperparameter search space.
3. Create the tuning subset.
4. Perform RandomizedSearchCV.
5. Identify the optimized SVM model.
6. Calibrate the optimized SVM model.
7. Save the calibrated optimized model.
==========================================================
"""

import sys

import numpy as np

from sklearn.model_selection import (
    RandomizedSearchCV,
    train_test_split
)

from sklearn.svm import SVC

from sklearn.calibration import (
    CalibratedClassifierCV
)

from src.logger import logger

from src.exception import ProjectException

from src.utils import (
    load_object,
    save_object
)

from src.constants import (
    BASELINE_MODEL_PATH,
    BEST_MODEL_PATH,
    RANDOM_STATE,
    CV_FOLDS,
    SCORING_METRIC
)


# ==========================================================
# Hyperparameter Tuning Component
# ==========================================================

class HyperparameterTuning:
    """
    Performs hyperparameter optimization for the
    baseline Support Vector Machine model.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the Hyperparameter Tuning component.
        """

        logger.info(
            "Hyperparameter Tuning Component Initialized."
        )

    # ======================================================
    # Load Baseline Model
    # ======================================================

    def load_baseline_model(
        self
    ) -> SVC:
        """
        Load the baseline SVM model.

        Returns
        -------
        SVC
            Trained baseline SVM model.
        """

        try:

            logger.info(
                "Loading baseline SVM model."
            )

            baseline_model = load_object(
                BASELINE_MODEL_PATH
            )

            if not isinstance(
                baseline_model,
                SVC
            ):

                raise TypeError(
                    "The baseline model is not an SVC "
                    "model."
                )

            logger.info(
                "Baseline SVM model loaded successfully."
            )

            return baseline_model

        except Exception as error:

            logger.exception(
                "Failed to load baseline SVM model."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Define Search Space
    # ======================================================

    def define_search_space(
        self
    ) -> dict:
        """
        Define the SVM hyperparameter search space.

        Returns
        -------
        dict
            Hyperparameter distributions used by
            RandomizedSearchCV.
        """

        try:

            logger.info(
                "Defining SVM hyperparameter search space."
            )

            param_distributions = {

                "C": np.logspace(
                    -2,
                    2,
                    20
                ),

                "gamma": np.logspace(
                    -4,
                    1,
                    20
                ),

                "kernel": [
                    "rbf",
                    "linear"
                ]

            }

            logger.info(
                f"Hyperparameter search space: "
                f"{param_distributions}"
            )

            return param_distributions

        except Exception as error:

            logger.exception(
                "Failed to define hyperparameter search space."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Create Tuning Dataset
    # ======================================================

    def create_tuning_dataset(
        self,
        X_train,
        y_train
    ):
        """
        Create a stratified subset of the training dataset
        for hyperparameter tuning.

        The subset preserves the class distribution of the
        original training data.

        Parameters
        ----------
        X_train
            Preprocessed training features.

        y_train
            Training target labels.

        Returns
        -------
        tuple
            X_tune and y_tune.
        """

        try:

            logger.info(
                "Creating stratified tuning dataset."
            )

            X_tune, _, y_tune, _ = train_test_split(

                X_train,

                y_train,

                test_size=0.90,

                stratify=y_train,

                random_state=RANDOM_STATE

            )

            logger.info(
                f"Original training samples: "
                f"{len(X_train)}"
            )

            logger.info(
                f"Tuning samples: "
                f"{len(X_tune)}"
            )

            logger.info(
                "Stratified tuning dataset created successfully."
            )

            return (
                X_tune,
                y_tune
            )

        except Exception as error:

            logger.exception(
                "Failed to create tuning dataset."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Tune Model
    # ======================================================

    def tune_model(
        self,
        baseline_model: SVC,
        X_tune,
        y_tune
    ) -> tuple:
        """
        Perform SVM hyperparameter optimization using
        RandomizedSearchCV.

        Research configuration
        ----------------------
        n_iter = 4
        cv = 5
        scoring = accuracy
        random_state = 42
        n_jobs = -1
        verbose = 2

        Parameters
        ----------
        baseline_model : SVC
            Baseline SVM model.

        X_tune
            Tuning feature dataset.

        y_tune
            Tuning target labels.

        Returns
        -------
        tuple
            Calibrated optimized SVM model,
            best parameters,
            best cross-validation score.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "SVM HYPERPARAMETER TUNING STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Search Space
            # ==================================================

            param_distributions = (
                self.define_search_space()
            )

            # ==================================================
            # Research Configuration
            # ==================================================

            n_iter = 4

            logger.info(
                f"RandomizedSearchCV iterations: "
                f"{n_iter}"
            )

            logger.info(
                f"Cross-validation folds: "
                f"{CV_FOLDS}"
            )

            logger.info(
                f"Scoring metric: "
                f"{SCORING_METRIC}"
            )

            logger.info(
                f"Tuning dataset shape: "
                f"{X_tune.shape}"
            )

            # ==================================================
            # Randomized Search
            # ==================================================

            random_search = RandomizedSearchCV(

                estimator=baseline_model,

                param_distributions=(
                    param_distributions
                ),

                n_iter=n_iter,

                cv=CV_FOLDS,

                scoring=SCORING_METRIC,

                random_state=RANDOM_STATE,

                n_jobs=-1,

                verbose=2

            )

            logger.info(
                "Training RandomizedSearchCV."
            )

            # ==================================================
            # Fit Search
            # ==================================================

            random_search.fit(

                X_tune,

                y_tune

            )

            # ==================================================
            # Best Results
            # ==================================================

            best_model = (
                random_search.best_estimator_
            )

            best_parameters = (
                random_search.best_params_
            )

            best_score = (
                random_search.best_score_
            )

            logger.info(
                "Best SVM model identified successfully."
            )

            # ==================================================
            # Calibrate Optimized SVM
            # ==================================================

            logger.info(
                "Calibrating optimized SVM model."
            )

            calibrated_model = CalibratedClassifierCV(

                estimator=best_model,

                cv=CV_FOLDS,

                ensemble=False

            )

            calibrated_model.fit(

                X_tune,

                y_tune

            )

            logger.info(
                "Optimized SVM model calibrated successfully."
            )

            # ==================================================
            # Tuning Completed
            # ==================================================

            logger.info("=" * 70)

            logger.info(
                "SVM HYPERPARAMETER TUNING COMPLETED"
            )

            logger.info(
                f"Best CV Score: "
                f"{best_score:.4f}"
            )

            logger.info(
                f"Best Parameters: "
                f"{best_parameters}"
            )

            logger.info("=" * 70)

            return (

                calibrated_model,

                best_parameters,

                best_score

            )

        except Exception as error:

            logger.exception(
                "SVM hyperparameter tuning failed."
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
        Save the optimized calibrated SVM model.

        Parameters
        ----------
        best_model
            Calibrated optimized SVM model.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "SAVING OPTIMIZED SVM MODEL"
            )

            logger.info("=" * 70)

            save_object(

                file_path=BEST_MODEL_PATH,

                obj=best_model

            )

            logger.info(
                f"Optimized SVM model saved at: "
                f"{BEST_MODEL_PATH}"
            )

            logger.info("=" * 70)

        except Exception as error:

            logger.exception(
                "Failed to save optimized SVM model."
            )

            raise ProjectException(
                error,
                sys
            ) from error

    # ======================================================
    # Execute Hyperparameter Tuning Pipeline
    # ======================================================

    def initiate_hyperparameter_tuning(
        self,
        X_train,
        y_train
    ) -> dict:
        """
        Execute the complete SVM hyperparameter tuning
        pipeline.

        Parameters
        ----------
        X_train
            Preprocessed training feature matrix.

        y_train
            Training target labels.

        Returns
        -------
        dict
            Optimized calibrated model, best parameters,
            and best cross-validation score.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "HYPERPARAMETER TUNING PIPELINE STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Load Baseline SVM
            # ==================================================

            baseline_model = (
                self.load_baseline_model()
            )

            # ==================================================
            # Create Research Tuning Dataset
            # ==================================================

            X_tune, y_tune = (
                self.create_tuning_dataset(
                    X_train,
                    y_train
                )
            )

            # ==================================================
            # Tune SVM
            # ==================================================

            (
                best_model,
                best_parameters,
                best_score

            ) = self.tune_model(

                baseline_model,

                X_tune,

                y_tune

            )

            # ==================================================
            # Save Optimized Model
            # ==================================================

            self.save_best_model(

                best_model

            )

            # ==================================================
            # Pipeline Completed
            # ==================================================

            logger.info("=" * 70)

            logger.info(
                "HYPERPARAMETER TUNING PIPELINE COMPLETED"
            )

            logger.info("=" * 70)

            return {

                "best_model":
                    best_model,

                "best_parameters":
                    best_parameters,

                "best_score":
                    best_score

            }

        except Exception as error:

            logger.exception(
                "Hyperparameter tuning pipeline failed."
            )

            raise ProjectException(
                error,
                sys
            ) from error