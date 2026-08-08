"""
==========================================================
services/__init__.py

Project:
--------
Heart Disease Prediction

Description:
------------
Exports all application services used by
the Flask backend.
==========================================================
"""

from .prediction_service import PredictionService


__all__ = [

    "PredictionService"

]