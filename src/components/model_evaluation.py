"""
==========================================================
model_evaluation.py

Project
-------
Heart Disease Prediction

Description
-----------
Evaluates the trained machine learning model on the
testing dataset and generates the evaluation artifacts
required for the project.

Responsibilities
----------------
1. Load the trained model.
2. Generate predictions on the testing dataset.
3. Calculate classification metrics.
4. Generate classification report.
5. Generate confusion matrix.
6. Generate ROC-AUC evaluation.
7. Save evaluation results to artifacts.
==========================================================
"""

import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
    roc_curve
)

from src.logger import logger

from src.exception import ProjectException

from src.utils import (
    load_object,
    save_json
)

from src.constants import (
    BEST_MODEL_PATH,
    METRICS_PATH,
    CLASSIFICATION_REPORT_PATH,
    CONFUSION_MATRIX_JSON_PATH,
    CONFUSION_MATRIX_PATH,
    ROC_CURVE_PATH
)


# ==========================================================
# Model Evaluation Component
# ==========================================================

class ModelEvaluation:
    """
    Model Evaluation Component.

    Responsible for evaluating the trained model
    and generating the required evaluation artifacts.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the Model Evaluation component.
        """

        logger.info(
            "Initializing Model Evaluation Component."
        )

        self.model = self.load_model()

        logger.info(
            "Model Evaluation Component initialized successfully."
        )

    # ======================================================
    # Load Trained Model
    # ======================================================

    def load_model(self):
        """
        Load the trained best model.

        Returns
        -------
        Any
            Trained machine learning model.
        """

        try:

            logger.info(
                "Loading trained model for evaluation."
            )

            model = load_object(

                BEST_MODEL_PATH

            )

            logger.info(
                "Trained model loaded successfully."
            )

            return model

        except Exception as error:

            logger.exception(
                "Failed to load trained model."
            )

            raise ProjectException(

                error,

                sys

            ) from error

        # ======================================================
    # Evaluate Model
    # ======================================================

    def evaluate_model(
        self,
        X_test,
        y_test
    ) -> dict:
        """
        Evaluate the trained model on the testing dataset.

        Parameters
        ----------
        X_test
            Testing feature matrix.

        y_test
            Testing target values.

        Returns
        -------
        dict
            Complete model evaluation results.
        """

        try:

            logger.info(
                "=" * 70
            )

            logger.info(
                "MODEL EVALUATION STARTED"
            )

            logger.info(
                "=" * 70
            )

            # ==================================================
            # Generate Predictions
            # ==================================================

            logger.info(
                "Generating predictions on testing dataset."
            )

            predictions = self.model.predict(

                X_test

            )

            # ==================================================
            # Generate Prediction Probabilities
            # ==================================================

            logger.info(
                "Generating prediction probabilities."
            )

            if hasattr(
                self.model,
                "predict_proba"
            ):

                probabilities = (
                    self.model.predict_proba(
                        X_test
                    )[:, 1]
                )

            elif hasattr(
                self.model,
                "decision_function"
            ):

                probabilities = (
                    self.model.decision_function(
                        X_test
                    )
                )

            else:

                probabilities = None

            # ==================================================
            # Calculate Accuracy
            # ==================================================

            accuracy = accuracy_score(

                y_test,

                predictions

            )

            # ==================================================
            # Calculate Precision
            # ==================================================

            precision = precision_score(

                y_test,

                predictions,

                zero_division=0

            )

            # ==================================================
            # Calculate Recall
            # ==================================================

            recall = recall_score(

                y_test,

                predictions,

                zero_division=0

            )

            # ==================================================
            # Calculate F1 Score
            # ==================================================

            f1 = f1_score(

                y_test,

                predictions,

                zero_division=0

            )

            # ==================================================
            # Calculate ROC-AUC
            # ==================================================

            if probabilities is not None:

                roc_auc = roc_auc_score(

                    y_test,

                    probabilities

                )

            else:

                roc_auc = None

            # ==================================================
            # Classification Report
            # ==================================================

            report = classification_report(

                y_test,

                predictions,

                output_dict=True,

                zero_division=0

            )

            # ==================================================
            # Confusion Matrix
            # ==================================================

            matrix = confusion_matrix(

                y_test,

                predictions

            )

            confusion_matrix_data = {

                "true_negative": int(
                    matrix[0, 0]
                ),

                "false_positive": int(
                    matrix[0, 1]
                ),

                "false_negative": int(
                    matrix[1, 0]
                ),

                "true_positive": int(
                    matrix[1, 1]
                )

            }

            # ==================================================
            # Evaluation Results
            # ==================================================

            metrics = {

                "accuracy": round(
                    float(accuracy),
                    4
                ),

                "precision": round(
                    float(precision),
                    4
                ),

                "recall": round(
                    float(recall),
                    4
                ),

                "f1_score": round(
                    float(f1),
                    4
                ),

                "roc_auc": (

                    round(
                        float(roc_auc),
                        4
                    )

                    if roc_auc is not None

                    else None

                )

            }

            logger.info(
                f"Accuracy  : {metrics['accuracy']}"
            )

            logger.info(
                f"Precision : {metrics['precision']}"
            )

            logger.info(
                f"Recall    : {metrics['recall']}"
            )

            logger.info(
                f"F1 Score  : {metrics['f1_score']}"
            )

            logger.info(
                f"ROC-AUC   : {metrics['roc_auc']}"
            )

            logger.info(
                "Model evaluation completed successfully."
            )

            return {

                "metrics": metrics,

                "classification_report": report,

                "confusion_matrix": (
                    confusion_matrix_data
                ),

                "predictions": predictions,

                "probabilities": probabilities

            }

        except Exception as error:

            logger.exception(
                "Model evaluation failed."
            )

            raise ProjectException(

                error,

                sys

            ) from error

        # ======================================================
    # Save Evaluation Metrics
    # ======================================================

    def save_metrics(
        self,
        metrics: dict
    ) -> None:
        """
        Save model evaluation metrics to JSON.

        Parameters
        ----------
        metrics : dict
            Evaluation metrics.
        """

        try:

            logger.info(
                "Saving model evaluation metrics."
            )

            save_json(

                METRICS_PATH,

                metrics

            )

            logger.info(
                f"Model metrics saved successfully at: "
                f"{METRICS_PATH}"
            )

        except Exception as error:

            logger.exception(
                "Failed to save model evaluation metrics."
            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Save Classification Report
    # ======================================================

    def save_classification_report(
        self,
        report: dict
    ) -> None:
        """
        Save classification report to JSON.

        Parameters
        ----------
        report : dict
            Classification report generated
            by sklearn.
        """

        try:

            logger.info(
                "Saving classification report."
            )

            save_json(

                CLASSIFICATION_REPORT_PATH,

                report

            )

            logger.info(
                "Classification report saved successfully."
            )

        except Exception as error:

            logger.exception(
                "Failed to save classification report."
            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Save Confusion Matrix Data
    # ======================================================

    def save_confusion_matrix_data(
        self,
        confusion_matrix_data: dict
    ) -> None:
        """
        Save confusion matrix values to JSON.

        Parameters
        ----------
        confusion_matrix_data : dict
            Confusion matrix values.
        """

        try:

            logger.info(
                "Saving confusion matrix data."
            )

            save_json(

                CONFUSION_MATRIX_JSON_PATH,

                confusion_matrix_data

            )

            logger.info(
                "Confusion matrix data saved successfully."
            )

        except Exception as error:

            logger.exception(
                "Failed to save confusion matrix data."
            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Generate Confusion Matrix Image
    # ======================================================

    def save_confusion_matrix_plot(
        self,
        y_test,
        predictions
    ) -> None:
        """
        Generate and save the confusion matrix plot.

        Parameters
        ----------
        y_test
            Actual target values.

        predictions
            Predicted target values.
        """

        try:

            logger.info(
                "Generating confusion matrix plot."
            )

            matrix = confusion_matrix(

                y_test,

                predictions

            )

            figure, axis = plt.subplots(

                figsize=(7, 6)

            )

            image = axis.imshow(

                matrix,

                interpolation="nearest"

            )

            axis.figure.colorbar(

                image,

                ax=axis

            )

            axis.set(

                xticks=[0, 1],

                yticks=[0, 1],

                xticklabels=[
                    "No Heart Disease",
                    "Heart Disease"
                ],

                yticklabels=[
                    "No Heart Disease",
                    "Heart Disease"
                ],

                ylabel="Actual",

                xlabel="Predicted",

                title="Confusion Matrix"

            )

            threshold = (
                matrix.max() / 2.0
            )

            for row_index in range(
                matrix.shape[0]
            ):

                for column_index in range(
                    matrix.shape[1]
                ):

                    axis.text(

                        column_index,

                        row_index,

                        format(
                            matrix[
                                row_index,
                                column_index
                            ],
                            "d"
                        ),

                        ha="center",

                        va="center",

                        color=(
                            "white"
                            if matrix[
                                row_index,
                                column_index
                            ] > threshold
                            else "black"
                        )

                    )

            figure.tight_layout()

            figure.savefig(

                CONFUSION_MATRIX_PATH,

                dpi=300,

                bbox_inches="tight"

            )

            plt.close(

                figure

            )

            logger.info(
                f"Confusion matrix plot saved at: "
                f"{CONFUSION_MATRIX_PATH}"
            )

        except Exception as error:

            logger.exception(
                "Failed to generate confusion matrix plot."
            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Generate ROC Curve
    # ======================================================

    def save_roc_curve(
        self,
        y_test,
        probabilities
    ) -> None:
        """
        Generate and save the ROC curve.

        Parameters
        ----------
        y_test
            Actual target values.

        probabilities
            Prediction scores or probabilities.
        """

        try:

            if probabilities is None:

                logger.warning(
                    "ROC curve cannot be generated because "
                    "the model does not provide prediction "
                    "scores or probabilities."
                )

                return

            logger.info(
                "Generating ROC curve."
            )

            false_positive_rate, true_positive_rate, _ = (
                roc_curve(
                    y_test,
                    probabilities
                )
            )

            roc_auc = roc_auc_score(

                y_test,

                probabilities

            )

            figure, axis = plt.subplots(

                figsize=(8, 6)

            )

            axis.plot(

                false_positive_rate,

                true_positive_rate,

                label=f"ROC-AUC = {roc_auc:.4f}"

            )

            axis.plot(

                [0, 1],

                [0, 1],

                linestyle="--",

                label="Random Classifier"

            )

            axis.set(

                xlabel="False Positive Rate",

                ylabel="True Positive Rate",

                title="Receiver Operating Characteristic Curve"

            )

            axis.legend()

            figure.tight_layout()

            figure.savefig(

                ROC_CURVE_PATH,

                dpi=300,

                bbox_inches="tight"

            )

            plt.close(

                figure

            )

            logger.info(
                f"ROC curve saved at: "
                f"{ROC_CURVE_PATH}"
            )

        except Exception as error:

            logger.exception(
                "Failed to generate ROC curve."
            )

            raise ProjectException(

                error,

                sys

            ) from error


    # ======================================================
    # Model Evaluation Pipeline
    # ======================================================

    def initiate_model_evaluation(
        self,
        X_test,
        y_test
    ) -> dict:
        """
        Execute the complete model evaluation pipeline.

        Parameters
        ----------
        X_test
            Testing feature matrix.

        y_test
            Testing target values.

        Returns
        -------
        dict
            Complete model evaluation results.
        """

        try:

            logger.info("=" * 70)

            logger.info(
                "MODEL EVALUATION PIPELINE STARTED"
            )

            logger.info("=" * 70)

            # ==================================================
            # Evaluate Model
            # ==================================================

            evaluation_output = (
                self.evaluate_model(
                    X_test,
                    y_test
                )
            )

            # ==================================================
            # Extract Evaluation Results
            # ==================================================

            metrics = evaluation_output[
                "metrics"
            ]

            report = evaluation_output[
                "classification_report"
            ]

            confusion_matrix_data = (
                evaluation_output[
                    "confusion_matrix"
                ]
            )

            predictions = (
                evaluation_output[
                    "predictions"
                ]
            )

            probabilities = (
                evaluation_output[
                    "probabilities"
                ]
            )

            # ==================================================
            # Save JSON Artifacts
            # ==================================================

            self.save_metrics(

                metrics

            )

            self.save_classification_report(

                report

            )

            self.save_confusion_matrix_data(

                confusion_matrix_data

            )

            # ==================================================
            # Save Visualization Artifacts
            # ==================================================

            self.save_confusion_matrix_plot(

                y_test,

                predictions

            )

            self.save_roc_curve(

                y_test,

                probabilities

            )

            # ==================================================
            # Pipeline Completed
            # ==================================================

            logger.info("=" * 70)

            logger.info(
                "MODEL EVALUATION PIPELINE COMPLETED"
            )

            logger.info("=" * 70)

            return {

                "metrics": metrics,

                "classification_report": report,

                "confusion_matrix": (
                    confusion_matrix_data
                ),

                "confusion_matrix_path": (
                    str(
                        CONFUSION_MATRIX_PATH
                    )
                ),

                "roc_curve_path": (
                    str(
                        ROC_CURVE_PATH
                    )
                )

            }

        except Exception as error:

            logger.exception(
                "Model Evaluation Pipeline Failed."
            )

            raise ProjectException(

                error,

                sys

            ) from error