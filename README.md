# Student Performance Prediction

## Project Overview

This project is a comprehensive machine learning pipeline designed to predict student performance based on various academic and socio-economic factors. The solution encompasses the entire data science workflow, including data ingestion, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment via a user-friendly web application.

## Key Features

- **End-to-End ML Pipeline:** Automated data ingestion, preprocessing, model training, and prediction.
- **Robust Data Processing:** Handles missing values, categorical encoding, and feature scaling.
- **Model Training & Evaluation:** Utilizes advanced algorithms (e.g., CatBoost) for accurate predictions, with performance tracking and logging.
- **Web Application:** Interactive interface for users to input data and receive predictions in real-time.
- **Modular Codebase:** Clean, maintainable, and extensible architecture with clear separation of concerns.
- **Logging & Error Handling:** Comprehensive logging and custom exception handling for easier debugging and monitoring.

## Technologies Used

- **Python 3.x**
- **Pandas, NumPy, Scikit-learn:** Data manipulation and machine learning.
- **CatBoost:** Gradient boosting for tabular data.
- **Flask:** Web application framework.
- **Jupyter Notebook:** Exploratory data analysis and prototyping.
- **Logging:** Custom logging for tracking pipeline execution.
- **Pickle:** Model serialization.

## Project Structure

```
ML Projects/
│
├── application.py                # Flask app entry point
├── artifact/                     # Stores datasets, trained models, and preprocessors
├── catboost_info/                # CatBoost training logs and artifacts
├── logs/                         # Log files for pipeline execution
├── notebooks/                    # EDA and model training notebooks
├── src/                          # Source code for pipeline and components
│   ├── components/               # Data ingestion, transformation, and model training modules
│   ├── pipeline/                 # Training and prediction pipeline scripts
│   ├── logger.py                 # Custom logging setup
│   ├── exception.py              # Custom exception handling
│   └── utils.py                  # Utility functions
├── templates/                    # HTML templates for the web app
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## How It Works

1. **Data Ingestion:** Loads raw student data, splits into training and test sets.
2. **Data Transformation:** Cleans data, encodes categorical variables, scales features.
3. **Model Training:** Trains a CatBoost model, evaluates performance, and saves the best model.
4. **Prediction Pipeline:** Loads the trained model and preprocessor to make predictions on new data.
5. **Web App:** Users can input student data via a web form and receive instant predictions.

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the web application:**
   ```bash
   python application.py
   ```
3. **Access the app:**  
   Open your browser and go to `http://localhost:5000`.

