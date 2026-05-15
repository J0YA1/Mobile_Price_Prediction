import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("linear_regression_model.pkl")

# Load scaler
scaler = joblib.load(open("scaler.pkl", "rb"))

st.title("Mobile Price Prediction App")

st.write("Enter mobile specifications")

# Inputs
weight = st.slider('Weight', 150, 250)

ppi = st.number_input("PPI", min_value=250, max_value=600)

cpu_core = st.number_input("CPU Cores", min_value=1, max_value=8, step=1)

cpu_freq = st.number_input("CPU Frequency", min_value=0.1, max_value=3.0, step=0.1)

internal_mem = st.number_input("Internal Memory")

ram = st.selectbox(
    "RAM",
    options=[0.5, 1,2, 3, 4, 6, 8, 12, 16]
)

rear_cam = st.number_input("Rear Camera", min_value=0)

front_cam = st.number_input("Front Camera", min_value=0)

battery = st.number_input("Battery", min_value=1000, max_value=10000, step=100)

thickness = st.number_input("Thickness", min_value=5.0, max_value=20.0, step=0.1)

# Predict button
if st.button("Predict Price"):

    input_data = np.array([[
        weight,
        ppi,
        cpu_core,
        cpu_freq,
        internal_mem,
        ram,
        rear_cam,
        front_cam,
        battery,
        thickness
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Mobile Price: ${prediction[0]:,.2f}")

