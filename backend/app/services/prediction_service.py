"""
==========================================================
prediction_service.py

Project:
--------
Heart Disease Prediction

Description:
------------
Provides the service responsible for executing
the heart disease prediction workflow.

Responsibilities
----------------
✓ Receive PredictionInput object
✓ Execute Prediction Pipeline
✓ Return prediction result
==========================================================
"""

import sys

from src.logger import logger

from src.exception import ProjectException

from src.models.prediction_input import (

    PredictionInput

)

from src.pipeline.prediction_pipeline import (

    PredictionPipeline

)


# ==========================================================
# Prediction Service
# ==========================================================

class PredictionService:
    """
    Service responsible for executing the
    heart disease prediction pipeline.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self) -> None:
        """
        Initialize the prediction pipeline.
        """

        self.prediction_pipeline = PredictionPipeline()

        # ======================================================
    # Predict
    # ======================================================

    def predict(
        self,
        prediction_input: PredictionInput
    ) -> dict:
        """
        Execute the heart disease prediction pipeline.

        Parameters
        ----------
        prediction_input : PredictionInput
            Structured patient information.

        Returns
        -------
        dict
            Prediction result returned by the
            prediction pipeline.
        """

        try:

            logger.info(

                "Executing prediction pipeline."

            )

            prediction_result = (

                self.prediction_pipeline.predict(

                    prediction_input

                )

            )

            logger.info(

                "Prediction completed successfully."

            )

            return prediction_result

        except Exception as error:

            logger.exception(

                "Prediction pipeline execution failed."

            )

            raise ProjectException(

                error,

                sys

            ) from error