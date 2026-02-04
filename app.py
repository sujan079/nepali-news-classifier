import streamlit as st
import joblib
model = joblib.load("npnews_model.pkl")

st.title("News predict")
text=st.text_area("enter the news")

if st.button("Predict"):
    input_data = text
    prediction = model.predict([input_data])
    st.success(f"The predicted NEWS type is: {prediction}")