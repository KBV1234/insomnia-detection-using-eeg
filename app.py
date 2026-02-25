import streamlit as st
import numpy as np

st.set_page_config(page_title="Insomnia Detection")

st.title("🧠 Insomnia Detection Using EEG Signals")

st.write("Enter EEG feature values to predict insomnia.")

def simple_model(features):
    return 1 if sum(features) > 5 else 0

f1 = st.number_input("Feature 1")
f2 = st.number_input("Feature 2")
f3 = st.number_input("Feature 3")
f4 = st.number_input("Feature 4")
f5 = st.number_input("Feature 5")

if st.button("Predict"):
    result = simple_model([f1,f2,f3,f4,f5])

    if result == 1:
        st.error("🚨 Insomnia Detected")
    else:
        st.success("✅ No Insomnia Detected")
