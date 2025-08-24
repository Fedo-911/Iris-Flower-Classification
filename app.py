import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model, scaler, and label encoder
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🌸 Iris Flower Classification App")
st.write("Predict the species of an Iris flower based on its measurements.")

# Valid ranges from Kaggle dataset
valid_ranges = {
    "SepalLengthCm": (4.3, 7.9),
    "SepalWidthCm": (2.0, 4.4),
    "PetalLengthCm": (1.0, 6.9),
    "PetalWidthCm": (0.1, 2.5),
}

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict"):
    # Check valid ranges
    if not (valid_ranges["SepalLengthCm"][0] <= sepal_length <= valid_ranges["SepalLengthCm"][1]):
        st.error(
            f"❌ Sepal Length must be between {valid_ranges['SepalLengthCm'][0]} and {valid_ranges['SepalLengthCm'][1]} cm.")
    elif not (valid_ranges["SepalWidthCm"][0] <= sepal_width <= valid_ranges["SepalWidthCm"][1]):
        st.error(
            f"❌ Sepal Width must be between {valid_ranges['SepalWidthCm'][0]} and {valid_ranges['SepalWidthCm'][1]} cm.")
    elif not (valid_ranges["PetalLengthCm"][0] <= petal_length <= valid_ranges["PetalLengthCm"][1]):
        st.error(
            f"❌ Petal Length must be between {valid_ranges['PetalLengthCm'][0]} and {valid_ranges['PetalLengthCm'][1]} cm.")
    elif not (valid_ranges["PetalWidthCm"][0] <= petal_width <= valid_ranges["PetalWidthCm"][1]):
        st.error(
            f"❌ Petal Width must be between {valid_ranges['PetalWidthCm'][0]} and {valid_ranges['PetalWidthCm'][1]} cm.")
    else:
        # Convert to DataFrame
        input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                                  columns=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"])

        # Scale features
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)
        flower_name = label_encoder.inverse_transform(prediction)[0]

        st.success(f"🌼 The predicted Iris species is: **{flower_name}**")
