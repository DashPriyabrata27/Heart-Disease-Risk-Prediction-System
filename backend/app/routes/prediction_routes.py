"""
==========================================================
prediction_routes.py

Project:
--------
Heart Disease Prediction

Description:
------------
Defines the routes responsible for handling
heart disease prediction requests.
==========================================================
"""

from flask import (
    Blueprint,
    request,
    render_template
)

from app.services.prediction_service import (
    PredictionService
)

from src.logger import logger

from src.exception import ProjectException

from app.validators.input_validator import (
    validate_prediction_input
)

from app.utils.form_parser import (
    parse_prediction_form
)

# ==========================================================
# Prediction Blueprint
# ==========================================================

prediction_bp = Blueprint(

    "prediction",

    __name__,

    url_prefix="/prediction"

)


# ==========================================================
# Prediction Service
# ==========================================================

prediction_service = PredictionService()


# ==========================================================
# Predict Heart Disease
# ==========================================================

@prediction_bp.route(

    "/predict",

    methods=["POST"]

)
def predict():
    """
    Handle a heart disease prediction request.

    Workflow
    --------
    Request
        ↓
    Validation
        ↓
    Form Parsing
        ↓
    Prediction Service
        ↓
    Result Page

    Returns
    -------
    Response
        Rendered prediction result page.
    """

    logger.info(

        "Prediction request received."

    )

    try:
        # ==================================================
        # Receive Form Data
        # ==================================================

        form_data = request.form.to_dict()

        logger.info(

            "Patient information received successfully."

        )


        # ==================================================
        # Validate Input
        # ==================================================

        validated_data = validate_prediction_input(

            form_data

        )

        logger.info(

            "Input validation completed successfully."

        )


        # ==================================================
        # Parse Form Data
        # ==================================================

        prediction_input = parse_prediction_form(

            validated_data

        )

        logger.info(

            "Prediction input parsed successfully."

        )


        # ==================================================
        # Heart Disease Prediction
        # ==================================================

        prediction_result = prediction_service.predict(

            prediction_input

        )

        logger.info(

            "Prediction completed successfully."

        )


        # ==================================================
        # Render Prediction Result
        # ==================================================

        return render_template(

            "result.html",

            prediction=prediction_result

        )

    # ==================================================
    # Project Exception
    # ==================================================

    except ProjectException as error:

        logger.exception(

            "Prediction request failed."

        )

        return (

            render_template(

                "errors/error.html",

                error=str(error)

            ),

            400

        )


    # ==================================================
    # Unexpected Exception
    # ==================================================

    except Exception:

        logger.exception(

            "Unexpected error occurred during prediction."

        )

        return (

            render_template(

                "errors/error.html",

                error=(
                    "An unexpected error occurred while "
                    "processing your prediction request."
                )

            ),

            500

        )
    
    