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

    st.write("### 📈 Your Personality Scores")
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

#Setting up visualiztions for data frames
if 'df' in locals():
    st.subheader("📊 Trait Visualization & Interpretation")
    #Plotting the data 
    fig, ax = plt.subplots()
    sns.barplot(x='Trait', y='Score', data=df, palette='coolwarm')
    ax.set_ylim(0,100)
    ax.set_title("Your Big Five Personality Profile")
    st.pyplot(fig)
    #Interpreting the data 
    def interpret_trait(trait,score):
        if trait == 'Openness':
            if score > 70:
                return "You are highly open to new experiences, enjoy abstract thinking, creativity, and value art and imagination."
            elif score < 30: 
                return "You prefer routine and familiarity, practical thinking, and may be skeptical of new ideas or abstract concepts."
            else:
                return "You are moderately open: you enjoy new experiences but still value tradition and practical approaches."
        elif trait == 'Conscientiousness':
            if score > 70:
                return "You are very organized, disciplined, and goal-oriented. You likely plan ahead and value reliability."
            elif score < 30: 
                return "You may act more spontaneously and struggle with organization or long-term planning, preferring flexibility."
            else:
                return "You show a balanced approach to discipline: you can be organized but also adaptable when needed."
        elif trait == 'Extraversion':
            if score > 70:
                return "You are highly outgoing, energetic, and enjoy being around people. You likely draw energy from social interactions."
            elif score < 30:
                return "You are introverted and may prefer solitude or small, quiet settings. You tend to reflect inwardly and enjoy calm environments."
            else:
                return "You are an ambivert: comfortable in social settings but also value your alone time."
        elif trait == 'Agreeableness':
            if score > 70: 
                return "You are very compassionate, cooperative, and trusting. You value getting along with others and often avoid conflict."
            elif score < 30: 
                return "You may be more skeptical of others’ intentions and prioritize personal goals over social harmony."
            else:
                return "You strike a balance: you are friendly and cooperative, but can assert yourself when needed."
        elif trait == 'Neuroticism':
            if score > 70: 
                return "You may be more emotionally reactive and prone to stress, anxiety, or mood swings. You may often worry or feel overwhelmed."
            elif score < 30: 
                return "You tend to be emotionally stable, calm, and resilient under pressure. You likely handle stress well."
            else: 
              return "You have a moderate level of emotional reactivity: sometimes affected by stress but generally composed."   
    #Loop through each trait 
    for i, row in df.iterrows():
        trait = row['Trait']
        score = row['Score']
        st.markdown(f"### {trait} ({score})")
        st.write(interpret_trait(trait, score))

            

