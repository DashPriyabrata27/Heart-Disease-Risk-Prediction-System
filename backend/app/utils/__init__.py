"""
==========================================================
utils/__init__.py

Project:
--------
Heart Disease Prediction

Description:
------------
Exports utility functions used throughout
the Flask backend.
==========================================================
"""

from .form_parser import parse_prediction_form


__all__ = [

    "parse_prediction_form"

]