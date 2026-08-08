"""
==========================================================
exception.py

Project
-------
Heart Disease Prediction

Description
-----------
Provides a custom exception class for the project.

The custom exception captures detailed information
about errors to make debugging and troubleshooting
easier.

Captured Information
--------------------
✓ Original exception
✓ File name
✓ Function name
✓ Line number
✓ Error type
✓ Timestamp
✓ Detailed error message
==========================================================
"""

from datetime import datetime

from pathlib import Path

import sys

from typing import Any


# ==========================================================
# Generate Error Details
# ==========================================================

def get_error_details(
    error: Exception,
    error_detail: Any
) -> str:
    """
    Generate detailed information about an exception.

    Parameters
    ----------
    error : Exception
        Original exception that occurred.

    error_detail : Any
        Exception information provider, normally
        the Python sys module.

    Returns
    -------
    str
        Formatted error information.
    """

    _, _, traceback = (
        error_detail.exc_info()
    )

    # ======================================================
    # No Traceback Available
    # ======================================================

    if traceback is None:

        return str(error)

    # ======================================================
    # Locate Final Traceback Frame
    # ======================================================

    while traceback.tb_next:

        traceback = traceback.tb_next

    # ======================================================
    # Extract Error Information
    # ======================================================

    file_name = Path(

        traceback.tb_frame.f_code.co_filename

    ).name

    function_name = (

        traceback.tb_frame.f_code.co_name

    )

    line_number = traceback.tb_lineno

    error_type = type(error).__name__

    timestamp = datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )

    # ======================================================
    # Format Error Details
    # ======================================================

    return (

        "\n"

        + "=" * 70 + "\n"

        + "PROJECT EXCEPTION\n"

        + "=" * 70 + "\n"

        + f"Time       : {timestamp}\n"

        + f"File       : {file_name}\n"

        + f"Function   : {function_name}\n"

        + f"Line       : {line_number}\n"

        + f"Error Type : {error_type}\n"

        + f"Message    : {error}\n"

        + "=" * 70

    )
# ==========================================================
# Project Exception
# ==========================================================

class ProjectException(Exception):
    """
    Custom exception class for the project.

    Provides detailed information about the
    original exception, including the file,
    function, line number, error type,
    timestamp, and error message.
    """

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(
        self,
        error: Exception,
        error_detail: Any
    ) -> None:
        """
        Initialize the custom project exception.

        Parameters
        ----------
        error : Exception
            Original exception.

        error_detail : Any
            Exception information provider,
            normally the sys module.
        """

        super().__init__(
            str(error)
        )

        self.error_message = get_error_details(

            error,

            error_detail

        )

    # ======================================================
    # String Representation
    # ======================================================

    def __str__(self) -> str:
        """
        Return the formatted project exception.

        Returns
        -------
        str
            Detailed error message.
        """

        return self.error_message