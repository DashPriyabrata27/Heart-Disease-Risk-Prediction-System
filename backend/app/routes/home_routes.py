"""
==========================================================
home_routes.py

Project:
--------
Heart Disease Prediction

Description:
------------
Defines routes responsible for rendering
the application's home page.
==========================================================
"""

from flask import (

    Blueprint,
    render_template

)

from src.logger import logger


# ==========================================================
# Home Blueprint
# ==========================================================

home_bp = Blueprint(

    "home",

    __name__

)


# ==========================================================
# Home Page
# ==========================================================

@home_bp.route(

    "/",

    methods=["GET"]

)
def home():
    """
    Render the application's home page.

    Returns
    -------
    Response
        Rendered home page.
    """

    logger.info(

        "Rendering Home Page."

    )

    try:

        return render_template(

            "index.html"

        )

    except Exception:

        logger.exception(

            "Failed to render home page."

        )

        raise