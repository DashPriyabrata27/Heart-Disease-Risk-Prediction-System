"""
==========================================================
prediction_input.py

Project
-------
Heart Disease Prediction

Description
-----------
Defines the validated patient input structure used
by the backend and prediction pipeline.

Responsibilities
----------------
✓ Store patient input
✓ Provide a consistent prediction input structure
✓ Keep input fields aligned with the ML model
==========================================================
"""

from dataclasses import dataclass


# ==========================================================
# Prediction Input Model
# ==========================================================

@dataclass
class PredictionInput:
    """
    Represents validated patient information
    required for heart disease prediction.
    """

    age: float

    gender: int

    height: float

    weight: float

    ap_hi: float

    ap_lo: float

    cholesterol: int

    gluc: int

    smoke: int

    alco: int

    active: int

    age_years: float

    bmi: float

    bp_category_encoded: int