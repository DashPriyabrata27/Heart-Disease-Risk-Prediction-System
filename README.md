# ❤️ Heart Disease Risk Prediction System

An end-to-end Machine Learning web application that predicts the risk of heart disease from patient health information using a trained Support Vector Machine (SVM) model, Flask backend, and a simple web-based interface.

---

## 📌 Part 1 — Project Introduction

### Project Overview

Heart Disease Risk Prediction System is an end-to-end Machine Learning project developed to predict the likelihood of heart disease based on patient health information.

The system combines a Machine Learning prediction pipeline with a Flask backend and a simple web-based frontend. Users can enter patient information through the web interface, and the system validates the input, processes the data, applies the trained Machine Learning model, and displays the prediction along with probability values.

The complete workflow is designed as:

Patient Information  
↓  
Input Validation  
↓  
Prediction Input  
↓  
Prediction Pipeline  
↓  
Preprocessing  
↓  
Trained SVM Model  
↓  
Prediction + Probability  
↓  
Result Page

---

### 🎯 Project Objectives

The main objectives of this project are:

- Develop an end-to-end Machine Learning solution for heart disease risk prediction.
- Train and evaluate multiple Machine Learning classification algorithms.
- Perform hyperparameter tuning to improve model performance.
- Select and save the optimized Machine Learning model.
- Build a modular prediction pipeline.
- Develop a Flask-based backend for handling prediction requests.
- Validate and process user-provided patient information.
- Build a simple and user-friendly web interface.
- Display the predicted result and prediction probabilities.
- Organize the complete project into a structured and maintainable architecture.

---

### 🧠 Machine Learning Approach

The project uses supervised Machine Learning for binary classification of heart disease risk.

The Machine Learning workflow includes:

```text
Dataset
   ↓
Data Processing
   ↓
Feature Preparation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Prediction

---

## 🏗️ Part 2 — Project Architecture & Structure

The Heart Disease Risk Prediction System follows a modular project architecture that separates the Machine Learning workflow, Flask backend, frontend, datasets, and trained model artifacts.

This separation makes the project easier to understand, maintain, test, and extend.

### 📁 Project Structure

```text
Heart-Disease-Risk-Prediction-System/
│
├── backend/
│   │
│   ├── app.py
│   │
│   └── app/
│       ├── __init__.py
│       ├── config.py
│       │
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── home_routes.py
│       │   ├── prediction_routes.py
│       │   └── error_routes.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   └── prediction_service.py
│       │
│       ├── validators/
│       │   ├── __init__.py
│       │   └── input_validator.py
│       │
│       └── utils/
│           ├── __init__.py
│           └── form_parser.py
│
├── src/
│   │
│   ├── components/
│   │   ├── model_training.py
│   │   ├── hyperparameter_tuning.py
│   │   └── model_prediction.py
│   │
│   ├── models/
│   │   └── prediction_input.py
│   │
│   ├── pipeline/
│   │   └── prediction_pipeline.py
│   │
│   ├── constants.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── frontend/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── result.html
│   │   └── errors/
│   │       ├── 404.html
│   │       ├── 500.html
│   │       └── error.html
│   │
│   └── static/
│       ├── css/
│       ├── js/
│       ├── images/
│       └── icons/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── artifacts/
│   ├── best_model.pkl
│   ├── preprocessor.pkl
│   └── ...
│
├── research/
│   └── research.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md

---

## 🔄 Part 3 — End-to-End Machine Learning & Prediction Workflow

The project follows a complete Machine Learning workflow, starting from the raw heart disease dataset and ending with real-time prediction through the Flask web application.

### 🧠 Machine Learning Workflow

```text
Raw Dataset
     │
     ▼
Data Validation
     │
     ▼
Data Splitting
     │
     ▼
Data Preprocessing
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Hyperparameter Tuning
     │
     ▼
Best Model Selection
     │
     ▼
Model Serialization
     │
     ▼
Flask Prediction Application

---

## ⚙️ Part 4 — Backend Architecture

The backend of the application is developed using **Flask**.

It acts as the bridge between the frontend interface and the Machine Learning prediction pipeline.

The backend follows a modular structure where different responsibilities are separated into routes, services, validators, utilities, and Machine Learning components.

### 🔹 Backend Workflow

```text
Frontend
   │
   ▼
Flask Route
   │
   ▼
Input Validator
   │
   ▼
Form Parser
   │
   ▼
Prediction Service
   │
   ▼
Prediction Pipeline
   │
   ▼
Model Prediction
   │
   ▼
Prediction Result
   │
   ▼
Frontend Result Page

---

## 🎨 Part 5 — Frontend Architecture

The frontend provides a simple and user-friendly interface for interacting with the Heart Disease Risk Prediction System.

It is built using **HTML, CSS, JavaScript, and Jinja2 templates** and is integrated with the Flask backend.

The frontend focuses on keeping the prediction process simple:

```text
Home Page
    ↓
Patient Information Form
    ↓
Submit Prediction
    ↓
Flask Backend
    ↓
Prediction Result

---

## 🧰 Part 6 — Technologies & Tools

The project uses Python-based Machine Learning technologies along with Flask for the backend and HTML, CSS, and JavaScript for the frontend.

### 🐍 Programming Language

- **Python**

Python is used for:

- Data processing
- Machine Learning
- Model training
- Hyperparameter tuning
- Prediction
- Backend development

---

### 🤖 Machine Learning & Data Science

| Technology | Purpose |
|---|---|
| **Pandas** | Data loading and manipulation |
| **NumPy** | Numerical operations |
| **Scikit-learn** | Machine Learning models, preprocessing, evaluation, and hyperparameter tuning |
| **Matplotlib** | Data visualization and evaluation plots |

---

### 🌐 Backend

| Technology | Purpose |
|---|---|
| **Flask** | Web application backend |
| **Jinja2** | Dynamic HTML templating |

Flask connects the web interface with the Machine Learning prediction pipeline.

---

### 🎨 Frontend

| Technology | Purpose |
|---|---|
| **HTML** | Web page structure |
| **CSS** | User interface styling |
| **JavaScript** | Client-side interactions |

The frontend is intentionally kept simple and focused on the prediction workflow.

---

### 📓 Research & Development

- **Jupyter Notebook** — Research, experimentation, and Machine Learning analysis.
- **VS Code** — Project development and code organization.

---

### 🔧 Development & Version Control

| Tool | Purpose |
|---|---|
| **Git** | Version control |
| **GitHub** | Source code management and project hosting |
| **Python Virtual Environment** | Dependency isolation |

---

### 📦 Project Dependencies

The Python dependencies required to run the project are listed in:

```text
requirements.txt

                    Heart Disease Risk Prediction
                              │
             ┌────────────────┴────────────────┐
             │                                 │
        Machine Learning                  Web Application
             │                                 │
     ┌───────┴────────┐                ┌───────┴────────┐
     │                │                │                │
   Python        Scikit-learn        Flask          Frontend
     │                                 │                │
 Pandas / NumPy                    Jinja2        HTML/CSS/JS


---

## 📊 Part 7 — Dataset & Features

The Machine Learning component of the project is built using a heart disease dataset containing patient health, blood pressure, lifestyle, and medical information.

The dataset is used to train classification models that predict whether a patient is likely to have heart disease.

### 📁 Dataset Location

The raw dataset is stored in:

```text
data/
└── raw/
    └── heart_disease.csv

---

## 🤖 Part 8 — Model Training & Hyperparameter Tuning

The Machine Learning component trains multiple classification models and evaluates their performance before selecting the final prediction model.

### 🔹 Models Considered

The project considers the following classification algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

The trained models are evaluated to identify a suitable model for the heart disease classification task.

---

### 🔹 Baseline Model

The Support Vector Machine (SVM) model is used as the baseline model for the final optimization workflow.

The baseline model is saved as:

```text
artifacts/baseline_model.pkl


---

# Part 9 — Model Evaluation & Results

```markdown
---

## 📈 Part 9 — Model Evaluation & Results

The trained Machine Learning models are evaluated to understand their classification performance.

The evaluation process is performed using the testing dataset that was kept separate from the training process.

### 🔹 Evaluation Metrics

The project evaluates the models using classification performance measures such as:

- Accuracy
- Classification Report
- Confusion Matrix
- ROC Curve
- AUC

These metrics provide different perspectives on the performance of the classification model.

---

### 🔹 Classification Report

The classification report provides class-level performance information for the prediction model.

It includes metrics such as:

```text
Precision
Recall
F1-Score
Support


---

# Part 10 — Model Artifacts

```markdown
---

## 📦 Part 10 — Model Artifacts

The Machine Learning workflow generates several artifacts that are required for model prediction and evaluation.

These artifacts are stored inside the:

```text
artifacts/

---

# Part 11 — Installation & Environment Setup

```markdown
---

## ⚙️ Part 11 — Installation & Environment Setup

Follow the steps below to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/DashPriyabrata27/Heart-Disease-Risk-Prediction-System.git
2. Navigate to the Project Directory
cd Heart-Disease-Risk-Prediction-System
3. Create a Virtual Environment
python -m venv .venv
4. Activate the Virtual Environment
Windows PowerShell
.venv\Scripts\Activate.ps1
Windows Command Prompt
.venv\Scripts\activate
5. Install Dependencies

Install the required Python packages using:

pip install -r requirements.txt
🔹 Verify Python Environment

After activating the virtual environment, verify Python:

python --version

Verify pip:

pip --version
🔹 Project Environment

The project uses a Python virtual environment to keep its dependencies isolated from other Python projects.

Project
   │
   └── .venv/
       ├── Python
       └── Project Dependencies

The .venv/ directory is excluded from Git using .gitignore.

🔹 Required Dependencies

The main technologies required by the project include:

Python
Flask
Pandas
NumPy
Scikit-learn
Matplotlib

The exact package versions are maintained in:

requirements.txt

---

# Part 12 — Running the Application

```markdown
---

## ▶️ Part 12 — Running the Application

After completing the installation steps, the Flask application can be started locally.

### 🔹 Step 1 — Activate Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
🔹 Step 2 — Set Python Path

The project uses the src package from the project root.

For Windows PowerShell, set the project root as the Python path:

$env:PYTHONPATH = $PWD.Path
🔹 Step 3 — Start Flask Application

Run:

python backend\app.py

If the application starts successfully, Flask will display:

Running on http://127.0.0.1:5000
🔹 Step 4 — Open the Application

Open the following URL in a web browser:

http://127.0.0.1:5000
🔄 Application Flow
Start Flask
     │
     ▼
Load Configuration
     │
     ▼
Initialize Prediction Pipeline
     │
     ▼
Load Best Model
     │
     ▼
Load Preprocessor
     │
     ▼
Start Flask Server
     │
     ▼
Open Home Page
     │
     ▼
Enter Patient Information
     │
     ▼
Submit Prediction
     │
     ▼
View Prediction Result
🧪 Making a Prediction
Open the home page.
Enter the required patient information.
Submit the prediction form.
The backend validates the input.
The prediction pipeline processes the input.
The trained SVM model generates the prediction.
The result page displays the prediction and probability values.
🛑 Stopping the Application

To stop the Flask development server, press:

Ctrl + C
