#Setting up environment
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App Title and description
st.title("🧠 Big Five Personality Test Analyzer")
st.markdown("This app is dedicated to analyze your results from the Big Five Personality Test invented by Ernest Tupes and Raymond Christal. Upload your results in a csv file or input the data manually below!")
#Let user choose an input method of data 
input_method = st.radio("Choose input method:",["Manual Input", "Upload CSV"] )
#Setting slider options for manual input
if input_method == "Manual Input":
    st.subheader("🔧 Enter Your Scores (0-100)")

    # Slider input for each  of the five traits
    openness = st.slider("Openness", 0, 100, 50)
    conscientiousness = st.slider("Conscientiousness", 0, 100, 50)
    extraversion = st.slider("Extraversion", 0, 100, 50)
    agreeableness = st.slider("Agreeableness", 0, 100, 50)
    neuroticism = st.slider("Neuroticism", 0, 100, 50)

    # Storing the data in a DataFrame
    df = pd.DataFrame({
        'Trait': ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'],
        'Score': [openness, conscientiousness, extraversion, agreeableness, neuroticism]
    })

    st.write("### Your Personality Scores")
    st.dataframe(df)
#Set up for a CSV file
elif input_method == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")

