"""
==========================================================
constants.py

Project
-------
Heart Disease Prediction

Description
-----------
Stores all project-wide constant values used
throughout the application.

This module provides centralized configuration
for project directories, datasets, model artifacts,
evaluation outputs, validation rules, and logging.
==========================================================
"""

from pathlib import Path


# ==========================================================
# Project Root Directory
# ==========================================================

PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)


# ==========================================================
# Directory Paths
# ==========================================================

DATA_DIR = (
    PROJECT_ROOT / "data"
)

RAW_DATA_DIR = (
    DATA_DIR / "raw"
)

PROCESSED_DATA_DIR = (
    DATA_DIR / "processed"
)

EXTERNAL_DATA_DIR = (
    DATA_DIR / "external"
)

ARTIFACTS_DIR = (
    PROJECT_ROOT / "artifacts"
)

LOGS_DIR = (
    PROJECT_ROOT / "logs"
)


# ==========================================================
# Dataset Configuration
# ==========================================================

TARGET_COLUMN = "cardio"

# ==========================================================
# Required Dataset Columns
# ==========================================================

REQUIRED_COLUMNS = [

    "id",

    "age",

    "gender",

    "height",

    "weight",

    "ap_hi",

    "ap_lo",

    "cholesterol",

    "gluc",

    "smoke",

    "alco",

    "active",

    "cardio"

]

# ==========================================================
# Data Splitting Configuration
# ==========================================================

TEST_SIZE = 0.20

RANDOM_STATE = 42


# ==========================================================
# HYPERPARAMETER TUNING
# ==========================================================

CV_FOLDS = 5

N_ITERATIONS = 4

SCORING_METRIC = "accuracy"

# ==========================================================
# Dataset File Names
# ==========================================================

RAW_DATA_FILE_NAME = "heart_disease.csv"

TRAIN_FILE_NAME = "train.csv"

TEST_FILE_NAME = "test.csv"


# ==========================================================
# Model Artifact File Names
# ==========================================================

BASELINE_MODEL_FILE_NAME = (
    "baseline_model.pkl"
)

BEST_MODEL_FILE_NAME = (
    "best_model.pkl"
)

PREPROCESSOR_FILE_NAME = (
    "preprocessor.pkl"
)


# ==========================================================
# Evaluation Artifact File Names
# ==========================================================

METRICS_FILE_NAME = (
    "metrics.json"
)

CLASSIFICATION_REPORT_FILE_NAME = (
    "classification_report.json"
)

CONFUSION_MATRIX_JSON_FILE_NAME = (
    "confusion_matrix.json"
)

CONFUSION_MATRIX_IMAGE_FILE_NAME = (
    "confusion_matrix.png"
)

ROC_CURVE_FILE_NAME = (
    "roc_curve.png"
)


# ==========================================================
# Dataset Paths
# ==========================================================

RAW_DATA_PATH = (
    RAW_DATA_DIR / RAW_DATA_FILE_NAME
)

TRAIN_DATA_PATH = (
    PROCESSED_DATA_DIR / TRAIN_FILE_NAME
)

TEST_DATA_PATH = (
    PROCESSED_DATA_DIR / TEST_FILE_NAME
)


# ==========================================================
# Model Artifact Paths
# ==========================================================

BASELINE_MODEL_PATH = (
    ARTIFACTS_DIR / BASELINE_MODEL_FILE_NAME
)

BEST_MODEL_PATH = (
    ARTIFACTS_DIR / BEST_MODEL_FILE_NAME
)

PREPROCESSOR_PATH = (
    ARTIFACTS_DIR / PREPROCESSOR_FILE_NAME
)


# ==========================================================
# Evaluation Artifact Paths
# ==========================================================

METRICS_PATH = (
    ARTIFACTS_DIR / METRICS_FILE_NAME
)

CLASSIFICATION_REPORT_PATH = (
    ARTIFACTS_DIR / CLASSIFICATION_REPORT_FILE_NAME
)

CONFUSION_MATRIX_JSON_PATH = (
    ARTIFACTS_DIR / CONFUSION_MATRIX_JSON_FILE_NAME
)

CONFUSION_MATRIX_PATH = (
    ARTIFACTS_DIR / CONFUSION_MATRIX_IMAGE_FILE_NAME
)

ROC_CURVE_PATH = (
    ARTIFACTS_DIR / ROC_CURVE_FILE_NAME
)

# ==========================================================
# Feature Columns
# ==========================================================

FEATURE_COLUMNS = [

    "age",

    "gender",

    "height",

    "weight",

    "ap_hi",

    "ap_lo",

    "cholesterol",

    "gluc",

    "smoke",

    "alco",

    "active",

    "age_years",

    "bmi",

    "bp_category_encoded"

]


# ==========================================================
# Selected Features
# ==========================================================

SELECTED_FEATURES = [

    "age",

    "gender",

    "height",

    "weight",

    "ap_hi",

    "ap_lo",

    "cholesterol",

    "gluc",

    "smoke",

    "alco",

    "active",

    "age_years",

    "bmi",

    "bp_category_encoded"

]

# ==========================================================
# Supported Machine Learning Models
# ==========================================================

MODEL_NAMES = [

    "Logistic Regression",

    "Decision Tree",

    "Random Forest",

    "Support Vector Machine",

    "K-Nearest Neighbors",

    "Naive Bayes"

]


# ==========================================================
# Input Validation Configuration
# ==========================================================

MIN_AGE = 1

MIN_HEIGHT = 50

MAX_HEIGHT = 250

MIN_WEIGHT = 20

MAX_WEIGHT = 300

MIN_SYSTOLIC_BP = 1

MIN_DIASTOLIC_BP = 1

MIN_BMI = 1.0


# ==========================================================
# Valid Categorical Values
# ==========================================================

VALID_GENDERS = [

    1,

    2

]

VALID_BINARY_VALUES = [

    0,

    1

]

VALID_CHOLESTEROL_LEVELS = [

    1,

    2,

    3

]

VALID_GLUCOSE_LEVELS = [

    1,

    2,

    3

]

VALID_BP_CATEGORIES = [

    0,

    1,

    2,

    3,

    4

]


# ==========================================================
# Logging Configuration
# ==========================================================

LOG_FORMAT = (

    "%(asctime)s | "

    "%(levelname)s | "

    "%(name)s | "

    "%(filename)s:%(lineno)d | "

    "%(message)s"

)