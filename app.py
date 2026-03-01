import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("price_vs_area_model.pkl", "rb"))

#App title
st.title("Apartment Price Prediction")

#User Input
area = st.slider("Select the area of the apartment (in square meters)", 20, 200, 50)

if st.button("Predict Price"):
    input_data = pd.DataFrame({"surface_covered_in_m2": [area]})
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted price of the apartment is: ${prediction:,.2f}")