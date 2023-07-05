import streamlit as st
import pandas as pd

st.title("hello gianni!")
st.header("Gianni")
df = pd.read_csv("https://storage.googleapis.com/cloud-boot-app-bucket/1553768847-housing.csv")

st.dataframe(df)
dio cane