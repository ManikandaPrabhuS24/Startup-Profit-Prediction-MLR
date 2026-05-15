# Startup Profit Prediction Using Multiple Linear Regression

## Project Overview

This project is a Machine Learning application developed to predict startup profit based on multiple business-related factors using the Multiple Linear Regression algorithm. The project demonstrates the complete Machine Learning workflow from data preprocessing to model deployment.

The application predicts startup profit using the following input features:

- Research and Development Spend
- Administration Cost
- Marketing Spend
- Startup State Information

The project also includes deployment using Streamlit for real-time user interaction.

---

## Project Structure

```text
Startup-Profit-Prediction-Project/
│
├── 01_Startup_Profit_Prediction.ipynb
├── 02_Model_Deployment.ipynb
├── app.py
├── 50_Startups.csv
├── Finalized_model.sav
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Category | Tools / Libraries |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Data Visualization | Matplotlib |
| Model Deployment | Streamlit |
| Model Serialization | Pickle |

---

## Dataset Information

The dataset contains startup business information used for profit prediction.

### Features Used

| Feature Name | Description |
|---|---|
| R&D Spend | Research and development investment |
| Administration | Administrative expenses |
| Marketing Spend | Marketing investment |
| State | Startup operating state |
| Profit | Target variable to predict |

---

## Machine Learning Workflow

### 1. Import Libraries

Required libraries are imported for:

- Data handling
- Data preprocessing
- Visualization
- Model training
- Deployment

---

### 2. Load Dataset

The dataset is loaded using Pandas for analysis and preprocessing.

The workflow includes:

- Data inspection
- Null value checking
- Feature analysis
- Data preparation

---

### 3. Data Preprocessing

The categorical state column is converted into numerical format using encoding techniques.

Example encoded states:

- State_California
- State_Florida
- State_New_York

---

### 4. Feature Selection

### Input Features

```text
R&D Spend
Administration
Marketing Spend
State Information
```

### Target Variable

```text
Profit
```

---

### 5. Model Training

The project uses:

```python
Multiple Linear Regression
```

The model learns relationships between startup investments and overall profit.

---

### 6. Model Saving

The trained model is saved using Pickle serialization.

```text
Finalized_model.sav
```

---

### 7. Model Deployment

The trained model is deployed using Streamlit to provide an interactive web application.

Users can provide startup details and receive instant profit predictions.

---

## Streamlit Application

The Streamlit application provides a user-friendly interface for profit prediction.

### User Inputs

| Input | Description |
|---|---|
| R&D Spend | Research investment |
| Administration | Administrative cost |
| Marketing Spend | Marketing budget |
| State Selection | Startup operating state |

---

### Application Output

```text
Predicted Startup Profit
```

---



## Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Example Prediction Workflow

### Sample Inputs

| Feature | Example Value |
|---|---|
| R&D Spend | 120000 |
| Administration | 100000 |
| Marketing Spend | 300000 |
| State | California |

### Predicted Output

```text
150248.91
```

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Multiple Linear Regression
- Data preprocessing
- Feature encoding
- Machine Learning workflow
- Model serialization
- Streamlit deployment
- Interactive ML applications

---

## Future Improvements

Potential enhancements for this project:

- Add advanced regression algorithms
- Improve model accuracy
- Add performance metrics
- Deploy on cloud platforms
- Add visualization dashboards
- Build responsive UI design
- Add real-time analytics

---

## Author

**MANIKANDAPRABHU.S**

Machine Learning and Artificial Intelligence Enthusiast
