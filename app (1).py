
import streamlit as st
import pandas as pd
import joblib


# Page configuration
st.set_page_config(
    page_title="TikTok Day 30 Views Prediction",
    layout="wide"
)


# Title and introduction
st.title("TikTok Day 30 Views Prediction")

st.write(
    "This application predicts the cumulative number of TikTok views "
    "by Day 30 using early engagement metrics, video metadata, "
    "and creator statistics."
)


# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("final_model_pipeline.pkl")


model = load_model()

st.success("Model loaded successfully.")


# File upload section
st.header("Upload Data")

st.write(
    "Upload the prepared feature dataset used by the trained model."
)

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)


# Prediction section
if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Input Data")
    st.dataframe(data.head())

    st.write(f"Rows: {data.shape[0]} | Columns: {data.shape[1]}")

    if st.button("Predict Day 30 Views"):

        predictions = model.predict(data)

        result = data.copy()
        result["predicted_day30_views"] = predictions

        st.subheader("Prediction Results")

        st.dataframe(result)

        st.download_button(
            label="Download Predictions",
            data=result.to_csv(index=False),
            file_name="tiktok_predictions.csv",
            mime="text/csv"
        )
