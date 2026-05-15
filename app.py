import streamlit as st
import pickle
import pandas as pd


# Load trained model
model = pickle.load(open("Finalized_model.sav", "rb"))

# App title
st.title("Startup Profit Prediction using (Multiple Linear Regression)")

st.write("Enter the details to predict  startup profict.")

# User Inputs
RandD = st.number_input("R&D Spend", min_value=100000.0, max_value=9999999.0, value=100000.0)

Administration = st.number_input("Administration", min_value=100000.0, max_value=9999999.0, value=100000.0)

Marketing = st.number_input("Marketing Spend", min_value=100000.0, max_value=9999999.0, value=100000.0)
State_California = st.selectbox("State_California", ["Yes", "No"])

State_Florida = st.selectbox("State_Florida", ["Yes", "No"])

State_New_York = st.selectbox("State_New_York", ["Yes", "No"])

# Convert categorical values
State_California = 1 if State_California == "Yes" else 0
State_Florida = 1 if State_Florida == "Yes" else 0
State_New_York = 1 if State_New_York == "Yes" else 0

# Prediction button
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame([[RandD, Administration, Marketing, State_California, State_Florida, State_New_York]],
                              columns=['R&D Spend', 'Administration', 'Marketing Spend', 'State_California', 'State_Florida', 'State_New York'])


    prediction = model.predict(input_data)
    

    st.success(f"Predicted Startup Profit: Rs./ {prediction[0][0]:,.2f}")