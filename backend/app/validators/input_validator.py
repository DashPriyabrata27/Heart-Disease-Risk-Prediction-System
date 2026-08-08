"""
==========================================================
input_validator.py

Project:
--------
Heart Disease Prediction

Description:
------------
Validates and normalizes the raw user input
received from the prediction form.

Responsibilities
----------------
✓ Convert raw form values
✓ Validate numerical fields
✓ Validate categorical fields
✓ Validate binary fields
✓ Return validated data
==========================================================
"""

import sys

from src.logger import logger
from src.exception import ProjectException

from src.constants import (
    MIN_AGE,
    MIN_HEIGHT,
    MAX_HEIGHT,
    MIN_WEIGHT,
    MAX_WEIGHT,
    MIN_SYSTOLIC_BP,
    MIN_DIASTOLIC_BP,
    VALID_GENDERS,
    VALID_BINARY_VALUES,
    VALID_CHOLESTEROL_LEVELS,
    VALID_GLUCOSE_LEVELS
)


# ==========================================================
# Validate Prediction Input
# ==========================================================

def validate_prediction_input(
    form_data: dict[str, str]
) -> dict[str, int | float]:
    """
    Validate and normalize prediction input.

    Parameters
    ----------
    form_data : dict[str, str]
        Raw form values received from Flask.

    Returns
    -------
    dict[str, int | float]
        Validated patient information.
    """

    try:

        logger.info(
            "Validating prediction input."
        )

        # ==================================================
        # Type Conversion
        # ==================================================

        validated_data = {

            "age": int(form_data["age"]),

            "gender": int(form_data["gender"]),

            "height": int(form_data["height"]),

            "weight": float(form_data["weight"]),

            "ap_hi": int(form_data["ap_hi"]),

            "ap_lo": int(form_data["ap_lo"]),

            "cholesterol": int(form_data["cholesterol"]),

            "gluc": int(form_data["gluc"]),

            "smoke": int(form_data["smoke"]),

            "alco": int(form_data["alco"]),

            "active": int(form_data["active"])

        }

        # ==================================================
        # Numerical Validation
        # ==================================================

        validate_age(
            validated_data["age"]
        )

        validate_height(
            validated_data["height"]
        )

        validate_weight(
            validated_data["weight"]
        )

        validate_blood_pressure(
            validated_data["ap_hi"],
            validated_data["ap_lo"]
        )

        # ==================================================
        # Categorical Validation
        # ==================================================

        validate_gender(
            validated_data["gender"]
        )

        validate_categorical(
            validated_data["cholesterol"],
            VALID_CHOLESTEROL_LEVELS,
            "Cholesterol"
        )

        validate_categorical(
            validated_data["gluc"],
            VALID_GLUCOSE_LEVELS,
            "Glucose"
        )

        # ==================================================
        # Binary Validation
        # ==================================================

        validate_binary(
            validated_data,
            [
                "smoke",
                "alco",
                "active"
            ]
        )

        logger.info(
            "Prediction input validated successfully."
        )

        return validated_data

    except Exception as error:

        logger.exception(
            "Prediction input validation failed."
        )

        raise ProjectException(
            error,
            sys
        ) from error


# ==========================================================
# Validate Age
# ==========================================================

def validate_age(age: int) -> None:
    """
    Validate patient age.
    """

    if age < MIN_AGE:

        raise ValueError(
            f"Age must be at least {MIN_AGE}."
        )


# ==========================================================
# Validate Height
# ==========================================================

def validate_height(height: int) -> None:
    """
    Validate patient height.
    """

    if not (
        MIN_HEIGHT <= height <= MAX_HEIGHT
    ):

        raise ValueError(
            f"Height must be between "
            f"{MIN_HEIGHT} and {MAX_HEIGHT} cm."
        )


# ==========================================================
# Validate Weight
# ==========================================================

def validate_weight(weight: float) -> None:
    """
    Validate patient weight.
    """

    if not (
        MIN_WEIGHT <= weight <= MAX_WEIGHT
    ):

        raise ValueError(
            f"Weight must be between "
            f"{MIN_WEIGHT} and {MAX_WEIGHT} kg."
        )


# ==========================================================
# Validate Blood Pressure
# ==========================================================

def validate_blood_pressure(
    systolic: int,
    diastolic: int
) -> None:
    """
    Validate blood pressure values.
    """

    if systolic < MIN_SYSTOLIC_BP:

        raise ValueError(
            f"Systolic blood pressure must be at least "
            f"{MIN_SYSTOLIC_BP} mmHg."
        )

    if diastolic < MIN_DIASTOLIC_BP:

        raise ValueError(
            f"Diastolic blood pressure must be at least "
            f"{MIN_DIASTOLIC_BP} mmHg."
        )

    if systolic <= diastolic:

        raise ValueError(
            "Systolic blood pressure must be greater "
            "than diastolic blood pressure."
        )


# ==========================================================
# Validate Gender
# ==========================================================

def validate_gender(gender: int) -> None:
    """
    Validate patient gender.
    """

    if gender not in VALID_GENDERS:

        raise ValueError(
            "Invalid gender value."
        )


# ==========================================================
# Validate Categorical Field
# ==========================================================

def validate_categorical(
    value: int,
    valid_values: set[int] | list[int] | tuple[int, ...],
    field_name: str
) -> None:
    """
    Validate categorical field.
    """

    if value not in valid_values:

        raise ValueError(
            f"Invalid {field_name.lower()} value."
        )


# ==========================================================
# Validate Binary Fields
# ==========================================================

def validate_binary(
    validated_data: dict[str, int | float],
    fields: list[str]
) -> None:
    """
    Validate binary fields.
    """

    for field in fields:

        if validated_data[field] not in VALID_BINARY_VALUES:

            raise ValueError(
                f"Invalid value for '{field}'."
            )