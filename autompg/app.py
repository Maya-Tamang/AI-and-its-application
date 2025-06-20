import streamlit as st
import joblib
import numpy as np
import pandas as pd


# Load models
baseline_model = joblib.load("rf_model.pkl")
tuned_model = joblib.load("rf_tuned_model.pkl")

# Page config
st.set_page_config(page_title="MPG Prediction App", layout="centered")

# Main title
st.markdown("<h1 style='text-align: center; color: #0073e6;'>MPG Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Compare predictions from Baseline vs Tuned Random Forest Models</h4>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar input section
st.sidebar.header("📋 Input Vehicle Features")


def user_input():
    cylinders = st.sidebar.number_input(' Cylinders', 3, 12, step=1, value=4)
    displacement = st.sidebar.slider('Displacement (cu in)', 50.0, 500.0, 150.0)
    horsepower = st.sidebar.slider(' Horsepower', 40.0, 250.0, 100.0)
    weight = st.sidebar.slider(' Weight (lbs)', 1500.0, 6000.0, 3000.0)
    acceleration = st.sidebar.slider('Acceleration (0-60 mph time)', 5.0, 30.0, 15.0)
    model_year = st.sidebar.selectbox(' Model Year', list(range(70, 83)), index=6)
    origin = st.sidebar.selectbox(' Origin', ['1 - USA', '2 - Europe', '3 - Japan'])

    origin_code = origin.split(" ")[0]
    origin_1 = 1 if origin_code == '1' else 0
    origin_2 = 1 if origin_code == '2' else 0
    origin_3 = 1 if origin_code == '3' else 0

    power_to_weight = horsepower / weight if weight != 0 else 0.001

    # Match feature names used during training
    data = {
        'cylinders': [cylinders],
        'displacement': [displacement],
        'horsepower': [horsepower],
        'weight': [weight],
        'acceleration': [acceleration],
        'model year': [model_year],
        'power_to_weight': [power_to_weight],
        'origin_1': [origin_1],
        'origin_2': [origin_2],
        'origin_3': [origin_3]
    }

    features = pd.DataFrame(data)
    return features



# Collect input
input_data = user_input()

# Make predictions
baseline_pred = baseline_model.predict(input_data)[0]
tuned_pred = tuned_model.predict(input_data)[0]

# Result display
st.markdown("## 🔍 Prediction Results")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="padding: 20px; background-color: #e6f2ff; border-radius: 10px;">
            <h3 style="color:#004080;">Baseline Model </h3>
            <h2 style="color:#003366;">{:.2f} MPG</h2>
        </div>
    """.format(baseline_pred), unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="padding: 20px; background-color: #d9f2d9; border-radius: 10px;">
            <h3 style="color:#1a6600;">Tuned Model </h3>
            <h2 style="color:#145214;">{:.2f} MPG</h2>
        </div>
    """.format(tuned_pred), unsafe_allow_html=True)



st.markdown("---")

st.markdown("<p style='text-align: center; color: grey;'>Built using Streamlit</p>", unsafe_allow_html=True)
