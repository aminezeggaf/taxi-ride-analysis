import pandas as pd
import numpy as np
import streamlit as st

st.header("Taxi Trip Data Analysis")

df = pd.read_csv('data/Taxi_Trip_Data.csv')

st.divider()
st.subheader("1. Intial discovery, first 10 rows of the data")
st.dataframe(df.head(10),hide_index=True)

st.divider()
st.subheader("2. Data Size")
st.write(str(df.size) + " rows")

st.divider()
st.subheader("3. Describing the data")
st.dataframe(df.describe())

st.divider()
st.subheader("4. Summarzing the data")
info_df = pd.DataFrame({
    "Column": df.columns,
    "Non-Null Count": df.notnull().sum().values,
    "Null Count": df.isnull().sum().values,
    "Dtype": df.dtypes.values
})
st.table(info_df)
