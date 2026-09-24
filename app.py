import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("housing_price_model.pkl")

st.title("Sydney Housing Price Prediction")
st.write("Enter the property details to estimate its sale price.")

suburb = st.selectbox(
    "Suburb",
    ["Blacktown", "Parramatta", "Liverpool"]
)

bedrooms = st.number_input("Bedrooms", min_value=0, max_value=30, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0, max_value=20, value=2)
parking = st.number_input("Parking", min_value=0, max_value=10, value=1)
land_size = st.number_input("Land Size (m²)", min_value=0.0, value=500.0)

property_type = st.selectbox(
    "Property Type",
    ["House", "Apartment", "Unit", "Townhouse"]
)

total_rooms = bedrooms + bathrooms

input_data = pd.DataFrame({
    "Suburb": [suburb],
    "Bedrooms": [bedrooms],
    "Bathrooms": [bathrooms],
    "Parking": [parking],
    "Land Size": [land_size],
    "Property Type": [property_type],
    "Total Rooms": [total_rooms]
})

if st.button("Predict Sale Price"):
    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Sale Price: ${prediction:,.0f}"
    )