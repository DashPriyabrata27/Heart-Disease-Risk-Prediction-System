"""
==========================================================
app.py

Project:
--------
Heart Disease Prediction

Description:
------------
Application entry point for starting
the Flask web server.
==========================================================
"""

from datetime import datetime

from app import create_app
from app.config import get_config

from src.logger import logger
# ==========================================================
# Load Configuration
# ==========================================================

configuration = get_config()


# ==========================================================
# Create Flask Application
# ==========================================================

app = create_app()


# ==========================================================
# Global Template Context
# ==========================================================

@app.context_processor
def inject_current_year() -> dict[str, int]:
    """
    Make the current year available to all templates.

    Returns
    -------
    dict[str, int]
        Dictionary containing the current year.
    """

    return {

        "current_year": datetime.now().year

    }


# ==========================================================
# Start Application
# ==========================================================

if __name__ == "__main__":

    logger.info(

        "Starting Heart Disease Prediction application."

    )

    app.run(

        host=configuration.HOST,

        port=configuration.PORT,

        debug=configuration.DEBUG

    )