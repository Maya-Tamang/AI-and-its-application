import streamlit as st
import pandas as pd
import joblib

# Load saved models
baseline_model = joblib.load('linreg_model.pkl')
tuned_model = joblib.load('tuned_linregression.pkl')

# Manually define course-to-encoded mapping (must match training)
course_mapping = {
    "Tailoring": 0,
    "Beautician": 2,
    "Mobile Repair": 3,
    "Electrical": 4,
    "Computer Operator": 5
}


reverse_mapping = {v: k for k, v in course_mapping.items()}

# Streamlit app
st.title(" SEEP Mela Participant Predictor")

# Show encoding table
st.subheader("📘 Course Encoding Reference")
st.table(pd.DataFrame(course_mapping.items(), columns=["Course Name", "Encoded Value"]))

# User input section
st.subheader(" Input Details")
course_name = st.selectbox("Select Course", list(course_mapping.keys()))
year = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2024)
sessions = st.number_input("Sessions Conducted", min_value=1, max_value=100, value=3)

# Prepare input for prediction
course_encoded = course_mapping[course_name]
input_df = pd.DataFrame({
    'Year': [year],
    'Course': [course_encoded],
    'Sessions_Conducted': [sessions]
})

# Predictions
st.subheader(" Prediction Output")
if st.button("Predict using Baseline Model"):
    pred = baseline_model.predict(input_df)
    st.success(f" Predicted Participants (Baseline): {int(pred[0])}")

if st.button("Predict using Tuned Model"):
    pred = tuned_model.predict(input_df)
    st.success(f" Predicted Participants (Tuned): {int(pred[0])}")
