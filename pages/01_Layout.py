import streamlit as st

placeholder = st.empty()

st_main_columns = st.columns((1, 1))

st_main_columns[0].header("Column 1")
st_main_columns[1].header("Column 2")

st_main_columns = st.columns((2, 1))

st_main_columns[0].header("Column 1")
st_main_columns[1].header("Column 2")

st_main_columns = st.columns((2, 1), gap="large")

st_main_columns[0].header("Column 1")
st_main_columns[1].header("Column 2")

st_main_columns = st.columns((2, 1), gap="small")

st_main_columns[0].header("Column 1")
st_main_columns[1].header("Column 2")

with st.expander("Clicca per vedere qualcosa"):
    st.header("Qualcosa")

with placeholder.expander("Clicca per scoprire"):
    st.header("Expander placeholder")
