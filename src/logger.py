"""
==========================================================
logger.py

Project
-------
Heart Disease Prediction

Description
-----------
Configures the centralized logging system for
the Heart Disease Prediction project.

Features
--------
✓ Creates a new log file for every execution.
✓ Stores log files inside the logs directory.
✓ Writes logs to both console and file.
✓ Prevents duplicate logging handlers.
✓ Uses the centralized LOG_FORMAT configuration.
==========================================================
"""

import logging

from datetime import datetime

from src.constants import (
    LOGS_DIR,
    LOG_FORMAT
)


# ==========================================================
# Create Logs Directory
# ==========================================================

LOGS_DIR.mkdir(

    parents=True,

    exist_ok=True

)


# ==========================================================
# Generate Log File Name
# ==========================================================

LOG_FILE_NAME = (

    f"{datetime.now():%Y-%m-%d_%H-%M-%S}.log"

)


# ==========================================================
# Generate Log File Path
# ==========================================================

LOG_FILE_PATH = (

    LOGS_DIR / LOG_FILE_NAME

)


# ==========================================================
# Create Project Logger
# ==========================================================

logger = logging.getLogger(

    "HeartDiseasePrediction"

)

logger.setLevel(

    logging.INFO

)

logger.propagate = False

# ==========================================================
# Configure Logger Handlers
# ==========================================================

if not logger.handlers:

    # ======================================================
    # File Handler
    # ======================================================

    file_handler = logging.FileHandler(

        filename=LOG_FILE_PATH,

        encoding="utf-8"

    )

    file_handler.setLevel(

        logging.INFO

    )

    # ======================================================
    # Console Handler
    # ======================================================

    console_handler = logging.StreamHandler()

    console_handler.setLevel(

        logging.INFO

    )

    # ======================================================
    # Create Formatter
    # ======================================================

    formatter = logging.Formatter(

        fmt=LOG_FORMAT,

        datefmt="%Y-%m-%d %H:%M:%S"

    )

    # ======================================================
    # Apply Formatter
    # ======================================================

    file_handler.setFormatter(

        formatter

    )

    console_handler.setFormatter(

        formatter

    )

    # ======================================================
    # Register Handlers
    # ======================================================

    logger.addHandler(

        file_handler

    )

    logger.addHandler(

        console_handler
    )