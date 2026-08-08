Heart-Disease-Prediction/
│
├── frontend/
|    ├── templates/
|    │   │
|    │   ├── base.html 
|    │   ├── index.html
|    │   ├── result.html
|    │   │
|    │   └── errors/
|    │       ├── 404.html
|    │       ├── 500.html
|    │       └── error.html
|    │
|    ├── static/
|    │   │
|    │   ├── css/
|    │   │   ├── base.css
|    │   │   ├── home.css
|    │   │   ├── result.css
|    │   │   └── error.css
|    │   │
|    │   ├── js/
|    │   │   ├── form_validation.js
|    │   │   ├── prediction.js
|    │   │   └── ui.js
|    │   │
|    │   ├── images/
|    │   │   ├── logo.png
|    │   │   ├── hero.jpg 
|    |   |   ├── background.jpg
|    |   |   ├── doctor.jpg
|    |   |   ├── prediction.jpg
|    |   |   ├── dashboard.jpg
|    │   │   └── medical_pattern.jpg
|    |   |
|    │   └── icons/
|    │       ├── heart.svg
|    |       ├── heartbeat.svg
|    |       ├── prediction.svg
|    |       ├── warning.svg
|    |       ├── doctor.svg
|    |       ├── dashboard.svg
|    |       ├── patient.svg
|    |       ├── hospital.svg
|    |       ├── success.svg
|    |       ├── error.svg
|    |       ├── loading.svg
|    │       ├── info.svg
|    │       └── github.svg
|    │   
│
├── backend/
|    │
|    ├── app.py                          # Flask Application Entry Point
|    │
|    ├── app/
|    │   │
|    │   ├── __init__.py                 # Create Flask Application
|    │   │
|    │   ├── routes/
|    │   │   ├── __init__.py
|    │   │   ├── home_routes.py          # Home Page
|    │   │   ├── prediction_routes.py    # Prediction
|    │   │   └── error_routes.py         # Custom Error Pages
|    │   │
|    │   ├── services/
|    │   │   ├── __init__.py
|    │   │   └── prediction_service.py   # Calls Prediction Pipeline
|    │   │
|    │   ├── validators/
|    │   │   ├── __init__.py
|    │   │   └── input_validator.py      # Form Validation
|    │   │
|    │   ├── utils/
|    │   │   ├── __init__.py
|    │   │   └── form_parser.py          # Convert Form → PredictionInput
|    │   │
|    │   └── config.py                   # Flask Configuration
|    │
|    └── instance/
│
├── data/
│   ├── raw/
│   │   └── heart_disease.csv
│   │
│   ├── processed/
│   │   ├── train.csv
|   |   └── test.csv
│   └── external/
│
├── research/
│   └── research.ipynb
│
├──artifacts/
|    │
|    ├── baseline_model.pkl
|    ├── best_model.pkl
|    ├── preprocessor.pkl
|    ├── metrics.json
|    ├── classification_report.json
|    ├── confusion_matrix.json
|    ├── confusion_matrix.png
|    ├── roc_curve.png
|    └── train.csv
|    └── test.csv
│
├── src/
│   │
│   ├── __init__.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_preprocessing.py
│   │   ├── feature_selection.py
│   │   ├── model_trainer.py
|   |   ├── hyperparameter_tuning.py           
│   │   ├── model_evaluation.py
│   │   └── model_prediction.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
|   |
|   ├── models/
│   |   ├── __init__.py
│   |   └── prediction_input.py
|   |
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   └── constants.py
│
├── logs/
│      ├── training.log
|
├── main.py
├── requirements.txt
├── README.md
├── setup.py
└── .gitignore