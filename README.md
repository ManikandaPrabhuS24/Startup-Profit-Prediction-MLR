### **Startup Profit Prediction using Multiple Linear Regression**

###### 

#### Author: MANIKANDAPRABHU.S  

#### Project Type: Machine Learning – Regression



###### 

#### **1)Project Overview**

###### 

###### This project predicts startup profit using Multiple Linear Regression.  

###### The model is trained using investment and spending data from startups to understand how different factors influence profit.





###### 

#### **2)Dataset**

###### 

##### File used: 50\_Startups.csv

###### 

###### The dataset contains:

###### 

* ###### R\&D Spend
* ###### Administration
* ###### Marketing Spend
* ###### State (Categorical Variable)
* ###### Profit (Target Variable)

###### 

###### The goal is to predict Profit based on the independent variables.





###### 

#### **3)Workflow**

###### 

* ###### Import required libraries
* ###### Load dataset using pandas
* ###### Handle categorical variable (State) using encoding
* ###### Prepare feature matrix (X) and target variable (y)
* ###### Split dataset into training and testing sets
* ###### Train Multiple Linear Regression model
* ###### Make predictions
* ###### Evaluate model using:

###### &nbsp;	- R² Score

###### &nbsp;	- Adjusted R²

###### &nbsp;	- Mean Squared Error (MSE)

* ###### Visualize results using:

###### &nbsp;	- Actual vs Predicted Plot

###### &nbsp;	- Residual Plot

* ###### Save trained model using pickle

###### 



#### 

#### 4\)**Model Evaluation**

###### 

* ###### The model explains approximately 87% of the variance in startup profit (R² ≈ 0.8752655285748308).

###### 

* ###### Mean Squared Error (MSE : 118348525.66956936)

###### 





#### **5)Project Files**

###### 

###### \- **01\_Startup\_Profit\_Prediction.ipynb** – Model training and evaluation

###### \- **02\_Model\_Deployment.ipynb** – Model loading and prediction

###### \- **50\_Startups.csv** – Dataset

###### \- **Finalized\_model.sav** – Trained regression model

###### \- **requirements.txt** – Required Python libraries

###### 





#### **6)Technologies Used**

###### 

* ###### Python
* ###### Pandas
* ###### NumPy
* ###### Matplotlib
* ###### Scikit-Learn
* ###### Pickle

###### 



