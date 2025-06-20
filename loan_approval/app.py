import streamlit as st
import pandas as pd
import joblib

# Load models
baseline_model = joblib.load("baseline_model.pkl")
tuned_model = joblib.load("best_loan_model.pkl")

# Loan label decoder (assumes 1 = Approved, 0 = Not Approved)
label_map = {1: "Approved ✅", 0: "Not Approved ❌"}

# App title
st.title("🏦 Loan Approval Predictor")
st.markdown("Predict loan approval using baseline and tuned models trained on Age, Income, and Hours Worked.")

# Input fields
st.subheader("Enter Applicant Details")

age = st.slider("Age", 18, 100, value=30)
income = st.number_input("Monthly Income (in $)", min_value=0, step=100, value=3000)
hours = st.slider("Hours Worked per Week", 0, 100, value=40)

# Prepare input data
input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "HoursWorked": [hours]
})

# Prediction section
st.subheader("🔍 Prediction Results")

col1, col2 = st.columns(2)

with col1:
    if st.button("Predict (Baseline Model)"):
        pred_baseline = baseline_model.predict(input_data)[0]
        st.info("Result using Baseline Decision Tree:")
        st.success(f"Loan Status: {label_map[pred_baseline]}")

with col2:
    if st.button("Predict (Tuned Model)"):
        pred_tuned = tuned_model.predict(input_data)[0]
        st.info("Result using Tuned Decision Tree:")
        st.success(f"Loan Status: {label_map[pred_tuned]}")
