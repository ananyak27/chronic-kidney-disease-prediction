# Chronic Kidney Disease Prediction

A Machine Learning project that predicts the likelihood of Chronic Kidney Disease (CKD) using patient clinical data. The project focuses on early disease detection through data preprocessing, exploratory data analysis, model training, and performance evaluation.

## Overview

Early detection of Chronic Kidney Disease can significantly improve treatment outcomes. This project applies supervised machine learning algorithms to classify whether a patient is likely to have CKD based on medical attributes.

## Features

- Data preprocessing and cleaning
- Missing value handling
- Exploratory Data Analysis (EDA)
- Feature engineering
- Machine Learning model training
- Model evaluation using classification metrics
- CKD prediction based on patient input

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset

This project uses the **Chronic Kidney Disease Dataset** from the **UCI Machine Learning Repository**. The dataset contains clinical and laboratory measurements used to classify patients as having Chronic Kidney Disease (CKD) or not.

Dataset Source:
https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease

## Project Workflow

1. Load the dataset
2. Clean and preprocess data
3. Perform Exploratory Data Analysis
4. Encode categorical features
5. Split data into training and testing sets
6. Train Machine Learning models
7. Evaluate model performance
8. Predict Chronic Kidney Disease

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Project Structure

```
chronic-kidney-disease-prediction/
│── app.py
│── ckd_model.pkl
│── encoders.pkl
│── scaler.pkl
│── requirements.txt
│── README.md
```

> Folder names may vary depending on the repository version.

## Installation

Clone the repository:

```bash
git clone https://github.com/ananyak27/chronic-kidney-disease-prediction.git
```

Navigate to the project folder:

```bash
cd chronic-kidney-disease-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Jupyter Notebook or Python script to train the model and make predictions.

## Future Improvements

- Hyperparameter tuning
- Model deployment using Flask or Streamlit
- Explainable AI (SHAP/LIME)
- Real-time prediction interface
- Cloud deployment

## Author

**Ananya Hebbar**

- LinkedIn: https://www.linkedin.com/in/ananya-hebbar/
- GitHub: https://github.com/ananyak27
