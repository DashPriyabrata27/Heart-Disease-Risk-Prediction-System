"""
==========================================================
form_parser.py

Project
-------
Heart Disease Prediction

Description
-----------
Parses validated prediction data and constructs the
PredictionInput object required by the prediction pipeline.

Responsibilities
----------------
✓ Parse validated form data
✓ Calculate age in years
✓ Calculate BMI
✓ Encode blood-pressure category
✓ Create PredictionInput object
==========================================================
"""

import sys

from src.logger import logger

from src.exception import ProjectException

from src.models.prediction_input import PredictionInput


# ==========================================================
# Parse Prediction Form
# ==========================================================

def parse_prediction_form(
    validated_data: dict[str, int | float]
) -> PredictionInput:
    """
    Convert validated form data into a
    PredictionInput object.

    Parameters
    ----------
    validated_data : dict[str, int | float]
        Validated patient information.

    Returns
    -------
    PredictionInput
        Prediction input object used by
        the prediction pipeline.
    """

    try:

        logger.info(
            "Parsing validated prediction input."
        )

        # ==================================================
        # Copy Validated Data
        # ==================================================

        prediction_data = validated_data.copy()

        # ==================================================
        # Calculate Age in Years
        # ==================================================

        prediction_data["age_years"] = (
            prediction_data["age"] / 365.25
        )

        # ==================================================
        # Calculate BMI
        # ==================================================

        height = prediction_data["height"]

        weight = prediction_data["weight"]

        height_meters = height / 100

        if height_meters <= 0:

            raise ValueError(
                "Height must be greater than zero."
            )

        prediction_data["bmi"] = (
            weight / (height_meters ** 2)
        )

        # ==================================================
        # Encode Blood Pressure Category
        # ==================================================

        systolic = prediction_data["ap_hi"]

        diastolic = prediction_data["ap_lo"]

        if systolic < 90 or diastolic < 60:

            bp_category_encoded = 0

        elif systolic < 120 and diastolic < 80:

            bp_category_encoded = 1

        elif systolic < 130 and diastolic < 80:

            bp_category_encoded = 2

        elif systolic < 140 or diastolic < 90:

            bp_category_encoded = 3

        else:

            bp_category_encoded = 4

        prediction_data[
            "bp_category_encoded"
        ] = bp_category_encoded

        logger.info(
            "Prediction feature preparation completed."
        )

        # ==================================================
        # Create PredictionInput Object
        # ==================================================

        prediction_input = PredictionInput(
            **prediction_data
        )

        logger.info(
            "PredictionInput object created successfully."
        )

        return prediction_input

    except Exception as error:

        logger.exception(
            "Failed to parse prediction input."
        )

        raise ProjectException(
            error,
            sys
        ) from error