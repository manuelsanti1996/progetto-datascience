import pandas as pd
import streamlit as st

st.title("Hello everyone!")

st.header("This is a Streamlit header!")

df = pd.read_csv("https://storage.googleapis.com/cloud-boot-app-bucket/1553768847-housing.csv")

st.dataframe(df)

st.session_state["my_dataframe"] = df.copy()

st.subheader("Selectbox")
selected_option = st.selectbox(
    "Seleziona opzione:",
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_option)

st.subheader("Multiselect")
selected_options = st.multiselect(
    "Seleziona opzione:",
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_options)

st.subheader("Radio")
selected_option = st.radio(
    "Seleziona opzione:",
    ["Opzione 1", "Opzione 2"]
)
st.write(selected_option)

st.subheader("Image")
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/London_Skyline_%28125508655%29.jpeg/800px-London_Skyline_%28125508655%29.jpeg"
)

st.subheader("Video")
st.video("https://www.youtube.com/watch?v=w2aw-nZrn1Q")
