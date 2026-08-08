"""
==========================================================
config.py

Project:
--------
Heart Disease Prediction

Description:
------------
Defines the Flask application configuration
used throughout the backend.

Responsibilities:
-----------------
✓ Store Flask configuration
✓ Manage development/testing/production settings
✓ Configure security
✓ Configure application paths
==========================================================
"""

import os

from dataclasses import dataclass


# ==========================================================
# Base Configuration
# ==========================================================

@dataclass(frozen=True)
class Config:
    """
    Base configuration shared by all environments.
    """

    # ------------------------------------------------------
    # Security
    # ------------------------------------------------------

    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key-in-production"
    )

    # ------------------------------------------------------
    # Flask Settings
    # ------------------------------------------------------

    DEBUG: bool = False

    TESTING: bool = False

    TEMPLATES_AUTO_RELOAD: bool = True

    JSON_SORT_KEYS: bool = False

    JSONIFY_PRETTYPRINT_REGULAR: bool = True

    # ------------------------------------------------------
    # Application
    # ------------------------------------------------------

    APP_NAME: str = "Heart Disease Prediction"

    HOST: str = "127.0.0.1"

    PORT: int = 5000

    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024

    # ------------------------------------------------------
    # Static & Template Paths
    # ------------------------------------------------------

    BASE_DIR: str = os.path.dirname(
        os.path.abspath(__file__)
    )

    TEMPLATE_FOLDER: str = os.path.join(
        BASE_DIR,
        "../../frontend/templates"
    )

    STATIC_FOLDER: str = os.path.join(
        BASE_DIR,
        "../../frontend/static"
    )


# ==========================================================
# Development Configuration
# ==========================================================

@dataclass(frozen=True)
class DevelopmentConfig(Config):
    """
    Configuration used during development.
    """

    DEBUG: bool = True

    TEMPLATES_AUTO_RELOAD: bool = True

# ==========================================================
# Testing Configuration
# ==========================================================

@dataclass(frozen=True)
class TestingConfig(Config):
    """
    Configuration used during automated testing.
    """

    TESTING: bool = True

    DEBUG: bool = False


# ==========================================================
# Production Configuration
# ==========================================================

@dataclass(frozen=True)
class ProductionConfig(Config):
    """
    Configuration used in production.
    """

    DEBUG: bool = False

    TEMPLATES_AUTO_RELOAD: bool = False


# ==========================================================
# Configuration Mapping
# ==========================================================

CONFIG_MAP = {

    "development": DevelopmentConfig(),

    "testing": TestingConfig(),

    "production": ProductionConfig()

}


# ==========================================================
# Get Configuration
# ==========================================================

def get_config() -> Config:
    """
    Return the configuration object based on
    the FLASK_ENV environment variable.

    Returns
    -------
    Config
        Flask configuration object.
    """

    environment = os.getenv(

        "FLASK_ENV",

        "development"

    ).lower()

    return CONFIG_MAP.get(

        environment,

        DevelopmentConfig()

    )

