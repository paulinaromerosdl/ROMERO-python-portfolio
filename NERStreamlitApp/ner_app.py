import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy 
nlp= spacy.load("en_core_web_sm")
st.title("Custom Named Entity Recognition (NER) App")
st.markdown("This app lets you input or upload text and define entities using spaCy's 'EntityRuler' Paste your custom patterns below, and explore the extracted entities!")
#Text Input Method 
text_input_method = st.radio("Choose text input method:", ("Write text", "Upload .txt file"))
if text_input_method== "Write text":
    user_text=st.text_area("✍️Enter your text:")
else: 
    uploaded_file = st.file_uploader("📄 Upload a .txt file", type=["txt"])
    if uploaded_file is not None:
        user_text = uploaded_file.read().decode("utf-8")
    else:
        user_text = ""
#Providing a sample text 
if st.button("📌 Use Sample Text"):
    user_text = "Did you know that the iconic Golden Dome atop Notre Dame's Main Building is covered in 23.9-karat gold leaf?"
    st.info("Sample text loaded!")