import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy 
nlp= spacy.load("en_core_web_sm")
st.title("Custom Named Entity Recognition (NER) App")
st.markdown("This app lets you input or upload text and define entities using spaCy's 'EntityRuler' Paste your custom patterns below, and explore the extracted entities!")