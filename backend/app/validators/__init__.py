"""
==========================================================
validators/__init__.py

Project:
--------
Heart Disease Prediction

Description:
------------
Exports all input validation utilities used
by the Flask backend.
==========================================================
"""

from .input_validator import validate_prediction_input


__all__ = [

    "validate_prediction_input"

]