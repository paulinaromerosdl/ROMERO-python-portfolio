import streamlit as st
import pandas as pd
st.title("Welcome to My Streamlit App")
df = pd.read_csv(data.csv)
st.write(df)
