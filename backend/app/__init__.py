"""
==========================================================
__init__.py

Project
-------
Heart Disease Prediction

Description
-----------
Creates and configures the Flask application.

Responsibilities
----------------
✓ Create Flask application
✓ Load configuration
✓ Register blueprints
✓ Register error handlers
==========================================================
"""

from flask import Flask

from app.config import get_config

from app.routes import (
    home_bp,
    prediction_bp,
    register_error_handlers
)


# ==========================================================
# Create Flask Application
# ==========================================================

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns
    -------
    Flask
        Configured Flask application.
    """

    # ======================================================
    # Load Configuration
    # ======================================================

    configuration = get_config()

    # ======================================================
    # Create Flask Application
    # ======================================================

    app = Flask(
        __name__,
        template_folder=configuration.TEMPLATE_FOLDER,
        static_folder=configuration.STATIC_FOLDER,
    )

    # ======================================================
    # Apply Configuration
    # ======================================================

    app.config.from_object(
        configuration
    )

    # ======================================================
    # Register Blueprints
    # ======================================================

    app.register_blueprint(
        home_bp
    )

    app.register_blueprint(
        prediction_bp
    )

    # ======================================================
    # Register Error Handlers
    # ======================================================

    register_error_handlers(
        app
    )

    # ======================================================
    # Return Flask Application
    # ======================================================

    return app