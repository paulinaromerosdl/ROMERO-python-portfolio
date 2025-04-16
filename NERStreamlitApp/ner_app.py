import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy 
nlp= spacy.load("en_core_web_sm")
