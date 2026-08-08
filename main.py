"""
==========================================================
main.py

Project
-------
Heart Disease Prediction

Description
-----------
Project-level entry point for executing the machine
learning training pipeline.

The Flask web application has a separate entry point
located at:

    backend/app.py
==========================================================
"""

import sys

from src.logger import logger

from src.exception import ProjectException

from src.pipeline.training_pipeline import TrainingPipeline


# ==========================================================
# Main Function
# ==========================================================

def main() -> None:
    """
    Execute the machine learning training pipeline.
    """

    try:

        logger.info("=" * 70)

        logger.info(
            "HEART DISEASE PREDICTION "
            "MACHINE LEARNING PIPELINE"
        )

        logger.info("=" * 70)

        training_pipeline = TrainingPipeline()

        result = training_pipeline.start_training()

        logger.info(
            f"Training completed successfully: {result}"
        )

        logger.info("=" * 70)

        logger.info(
            "MACHINE LEARNING TRAINING COMPLETED"
        )

        logger.info("=" * 70)

    except Exception as error:

        logger.exception(
            "Machine learning training failed."
        )

        raise ProjectException(
            error,
            sys
        ) from error


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    main()