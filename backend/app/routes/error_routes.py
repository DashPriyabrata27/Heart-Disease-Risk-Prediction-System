"""
==========================================================
error_routes.py

Project:
--------
Heart Disease Prediction

Description:
------------
Registers application-wide error handlers
for common HTTP and unexpected exceptions.
==========================================================
"""

from flask import (

    Flask,
    render_template

)

from src.logger import logger


# ==========================================================
# Register Error Handlers
# ==========================================================

def register_error_handlers(app: Flask) -> None:
    """
    Register all application error handlers.

    Parameters
    ----------
    app : Flask
        Flask application instance.
    """

    # ======================================================
    # 404 - Page Not Found
    # ======================================================

    @app.errorhandler(404)
    def page_not_found(error):
        """
        Handle 404 - Page Not Found.
        """

        logger.warning(

            "404 Page Not Found."

        )

        return (

            render_template(

                "errors/404.html"

            ),

            404

        )


    # ======================================================
    # 500 - Internal Server Error
    # ======================================================

    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Handle 500 - Internal Server Error.
        """

        logger.exception(

            "Internal Server Error."

        )

        return (

            render_template(

                "errors/500.html"

            ),

            500

        )
        # ======================================================
    # Generic Exception Handler
    # ======================================================

    @app.errorhandler(Exception)
    def handle_unexpected_exception(error):
        """
        Handle unexpected application exceptions.
        """

        logger.exception(

            "Unhandled application exception."

        )

        if app.config["DEBUG"]:

            error_message = str(error)

        else:

            error_message = (

                "An unexpected error occurred while "
                "processing your request."

            )

        return (

            render_template(

                "errors/error.html",

                error=error_message

            ),

            500

        )