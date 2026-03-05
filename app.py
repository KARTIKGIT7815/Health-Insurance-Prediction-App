# Libraries Required
import streamlit as st
import pickle

# Deployed Model
model = pickle.load(open('Health_model.pkl', 'rb'))

# Project Title
st.title('Health Insurance Prediction App')

# Heading
st.header("Fill your Personal Information")

# First 2 Input Tabs
col1, col2 = st.columns(2)

# Age Input Tab
with col1:
    st.subheader("Age")
    age = st.number_input('Enter Age', min_value=1, max_value=70, value=10, 
                          step=1, label_visibility="collapsed")

# Gender Input Tab
with col2:
    st.subheader("Gender")
    gender = st.selectbox("Select Gender", ["Male", "Female"], label_visibility="collapsed")
    # Encoding for model
    gender_val = 1 if gender == 'Female' else 0

# Next 2 Input Tabs
col3, col4 = st.columns(2)

# BMI Input Tab
with col3:
    st.subheader("Body Mass Index")
    bmi = st.number_input('BMI (Body Mass Index)', min_value=10.0, max_value=54.0, 
                          value=22.5, label_visibility="collapsed")

# Smoker Input Tab
with col4:
    st.subheader("Do you smoke?")
    smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'], label_visibility="collapsed")
    # Encoding for model
    smoker_val = 1 if smoker == 'Yes' else 0

# Children Input Tab
st.subheader("How many children do you have?")
children = st.slider('Number of Children', 0, 7, 0, label_visibility="collapsed")

# Data Submit Button
if st.button('Submit'):

    # Data Input for Model Testing
    X = [[age,bmi,children,gender_val,smoker_val]]

    # Trained Model for Prediction
    yp = model.predict(X)

    st.divider()
    # Result to display
    st.metric(label="Your Insurance Premium is", value=f"${round(yp[0]):,}")