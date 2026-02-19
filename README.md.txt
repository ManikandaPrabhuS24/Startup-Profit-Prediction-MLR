# Startup Profit Prediction using Multiple Linear Regression

Author: Manikandaprabhu.S  
Project Type: Machine Learning – Regression

## Project Overview

This project predicts startup profit using Multiple Linear Regression.  
The model is trained using investment and spending data from startups to understand how different factors influence profit.

## Dataset

File used: 50_Startups.csv

The dataset contains:

- R&D Spend
- Administration
- Marketing Spend
- State (Categorical Variable)
- Profit (Target Variable)

The goal is to predict Profit based on the independent variables.

## Workflow

1. Import required libraries
2. Load dataset using pandas
3. Handle categorical variable (State) using encoding
4. Prepare feature matrix (X) and target variable (y)
5. Split dataset into training and testing sets
6. Train Multiple Linear Regression model
7. Make predictions
8. Evaluate model using:
   - R² Score
   - Adjusted R²
   - Mean Squared Error (MSE)
9. Visualize results using:
   - Actual vs Predicted Plot
   - Residual Plot
10. Save trained model using pickle

## Model Evaluation

The model explains approximately 87% of the variance in startup profit (R² ≈ 0.87).

Adjusted R² is used to ensure that unnecessary features do not artificially inflate performance.

## Project Files

- 01_Startup_Profit_Prediction.ipynb – Model training and evaluation
- 02_Model_Deployment.ipynb – Model loading and prediction
- 50_Startups.csv – Dataset
- Finalized_model.sav – Trained regression model
- requirements.txt – Required Python libraries

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Pickle

## Model Usage

The trained model can be loaded and used as follows:

import pickle

model = pickle.load(open('Finalized_model.sav', 'rb'))
prediction = model.predict([[165349.2, 136897.8, 471784.1, 1, 0]])
print(prediction)

This project demonstrates the complete workflow of building and evaluating a Multiple Linear Regression model for real-world business prediction.