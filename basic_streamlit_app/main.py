import streamlit as st
import pandas as pd
st.title("Welcome to My Streamlit App")
st.write("This website allos you to navigate through different datasets. For example the Palmer's Penguins dataset. You can filter the data using the dropdown and slider below.")
df = pd.read_csv("penguins.csv")
st.write(df)
species= st.selectbox("Select Species", df["species"].unique()) # type: ignore
year = st.slider("Select Year", int(df["year"].min(), int(df["year"].max), int(df["year"].min())))
filtered_df = df[(df["species"] == species)&(df["year"] == year)]
st.write(filtered_df)