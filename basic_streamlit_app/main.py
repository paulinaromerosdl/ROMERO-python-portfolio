import streamlit as st
import pandas as pd
st.title("Welcome to My Streamlit App")
df = pd.read_csv("penguins.csv")
st.write(df)
