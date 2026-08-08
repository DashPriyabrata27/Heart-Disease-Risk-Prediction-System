"""
==========================================================
routes/__init__.py

Project:
--------
Heart Disease Prediction

Description:
------------
Exports all application routes and
error handlers for easy registration
inside the Flask application factory.
==========================================================
"""

from .home_routes import home_bp

from .prediction_routes import prediction_bp

from .error_routes import register_error_handlers


__all__ = [

    "home_bp",

    "prediction_bp",

    "register_error_handlers"

]