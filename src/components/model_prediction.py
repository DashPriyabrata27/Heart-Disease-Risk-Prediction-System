"""
==========================================================
model_prediction.py

Project
-------
Heart Disease Prediction

Description
-----------
Loads the trained machine learning model and
preprocessing pipeline required for making
predictions on new patient data.

Responsibilities
----------------
✓ Load trained model
✓ Load preprocessing pipeline
✓ Prepare prediction component
✓ Provide model and preprocessor for inference
==========================================================
"""

import sys

import pandas as pd

from src.logger import logger

from src.exception import ProjectException

from src.utils import load_object

from src.constants import (
    BEST_MODEL_PATH,
    PREPROCESSOR_PATH
)


# ==========================================================
# Model Prediction Component
# ==========================================================

class ModelPrediction:
    """
    Handles model loading, preprocessing, and
    prediction for new patient data.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the Model Prediction component.

        The trained model and preprocessing
        pipeline are loaded once during
        component initialization.
        """

        logger.info(
            "Initializing Model Prediction component."
        )

        self.model = self.load_model()

        self.preprocessor = self.load_preprocessor()

        logger.info(
            "Model Prediction component initialized successfully."
        )

    # ======================================================
    # Load Trained Model
    # ======================================================

    def load_model(self):
        """
        Load the trained machine learning model.

        Returns
        -------
        object
            Trained machine learning model.
        """

        try:

            logger.info(
                "Loading trained machine learning model."
            )

            model = load_object(

                BEST_MODEL_PATH

            )

            logger.info(
                "Trained machine learning model "
                "loaded successfully."
            )

            return model

        except Exception as error:

            logger.exception(
                "Failed to load trained machine learning model."
            )

            raise ProjectException(

                error,

                sys

            ) from error

    # ======================================================
    # Load Preprocessing Pipeline
    # ======================================================

    def load_preprocessor(self):
        """
        Load the trained preprocessing pipeline.

        Returns
        -------
        object
            Trained preprocessing pipeline.
        """

        try:

            logger.info(
                "Loading preprocessing pipeline."
            )

            preprocessor = load_object(

                PREPROCESSOR_PATH

            )

            logger.info(
                "Preprocessing pipeline "
                "loaded successfully."
            )

            return preprocessor

        except Exception as error:

            logger.exception(
                "Failed to load preprocessing pipeline."
            )

            raise ProjectException(

                error,

                sys

            ) from error
            # ======================================================
    # Generate Prediction
    # ======================================================

    def predict(
        self,
        input_data: pd.DataFrame | dict
    ) -> dict:
        """
        Generate a heart disease prediction
        for new patient data.

        Parameters
        ----------
        input_data : pd.DataFrame | dict
            Patient feature data.

        Returns
        -------
        dict
            Prediction result containing the
            predicted class and probabilities.
        """

        try:

            logger.info(

                "=" * 70

            )

            logger.info(

                "MODEL PREDICTION STARTED"

            )

            logger.info(

                "=" * 70

            )

            # ==================================================
            # Convert Input to DataFrame
            # ==================================================

            if not isinstance(

                input_data,

                pd.DataFrame

            ):

                input_data = pd.DataFrame(

                    [input_data]

                )

            logger.info(

                "Prediction input converted to DataFrame."

            )

            # ==================================================
            # Apply Preprocessing Pipeline
            # ==================================================

            logger.info(

                "Applying preprocessing pipeline."

            )

            transformed_data = (

                self.preprocessor.transform(

                    input_data

                )

            )

            logger.info(

                "Prediction input preprocessed successfully."

            )

            # ==================================================
            # Generate Prediction
            # ==================================================

            logger.info(

                "Generating heart disease prediction."

            )

            prediction = self.model.predict(

                transformed_data

            )[0]

            # ==================================================
            # Generate Prediction Probability
            # ==================================================

            logger.info(

                "Generating prediction probabilities."

            )

            probabilities = self.model.predict_proba(

                transformed_data

            )[0]

            probability_no = probabilities[0]

            probability_yes = probabilities[1]

            logger.info(

                "Prediction probabilities generated successfully."

            )

            # ==================================================
            # Prepare Prediction Result
            # ==================================================

            prediction_result = {

                "prediction": int(

                    prediction

                ),

                "prediction_label": (

                    "Heart Disease"

                    if prediction == 1

                    else

                    "No Heart Disease"

                ),

                "probability": {

                    "No Heart Disease": round(

                        float(

                            probability_no * 100

                        ),

                        2

                    ),

                    "Heart Disease": round(

                        float(

                            probability_yes * 100

                        ),

                        2

                    )

                }

            }

            logger.info(

                "Heart disease prediction generated successfully."

            )

            return prediction_result

        except Exception as error:

            logger.exception(

                "Model prediction failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error
        