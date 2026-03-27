import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib

# 1. Load the artifacts
model = tf.keras.models.load_model('churn_model.keras')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Bank Churn Predictor", page_icon="🏦")

st.title("🏦 Customer Churn Prediction")
st.markdown("Enter customer details to predict the likelihood of them leaving the bank.")

# 2. Create UI Layout with Columns
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    tenure = st.slider("Tenure (Years)", 0, 10, 5)

with col2:
    balance = st.number_input("Balance ($)", min_value=0.0, value=50000.0)
    num_products = st.slider("Number of Products", 1, 4, 1)
    has_card = st.selectbox("Has Credit Card?", ["No", "Yes"])
    active_member = st.selectbox("Is Active Member?", ["No", "Yes"])
    salary = st.number_input("Estimated Salary ($)", min_value=0.0, value=100000.0)

# 3. Preprocessing Logic (Must match the chrun.ipynb notebook exactly)
if st.button("Predict Churn"):
    # Convert Selectboxes to Binary
    gender_male = 1 if gender == "Male" else 0
    has_cr_card = 1 if has_card == "Yes" else 0
    is_active_member = 1 if active_member == "Yes" else 0
    
    # One-Hot Encode Geography
    geo_germany = 1 if geography == "Germany" else 0
    geo_spain = 1 if geography == "Spain" else 0
    
    # Feature Engineering: Age Group (Bins: 10, 30, 50, 100)
    if age <= 30:
        age_group = 0
    elif age <= 50:
        age_group = 1
    else:
        age_group = 2
        
    # Feature Engineering: Has Balance
    has_balance = 1 if balance > 0 else 0

    # 4. Construct the Feature Array (13 features in correct order)
    # Order from notebook: CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, 
    # IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male, age_group, has_balance
    features = np.array([[
        credit_score, age, tenure, balance, num_products, has_cr_card,
        is_active_member, salary, geo_germany, geo_spain, gender_male, age_group, has_balance
    ]])

    # 5. Scale and Predict
    features_scaled = scaler.transform(features)
    prediction_prob = model.predict(features_scaled)[0][0]
    prediction = 1 if prediction_prob > 0.5 else 0

    # 6. Display Results
    st.divider()
    if prediction == 1:
        st.error(f"⚠️ High Risk: This customer is likely to Churn! (Probability: {prediction_prob:.2f})")
    else:
        st.success(f"✅ Low Risk: This customer is likely to stay. (Probability: {prediction_prob:.2f})")