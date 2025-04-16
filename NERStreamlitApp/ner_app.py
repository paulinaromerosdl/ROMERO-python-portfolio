import json
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
#Custom Entity Pattern Input 
st.markdown("### 🧩 Define Custom Entity Patterns:")
example_json = '''{"label": "BUILDING", "pattern": "Golden Dome"}
{"label": "UNIVERSITY", "pattern": "Notre Dame"}
{"label": "LOCATION", "pattern": "Main Building"}
{"label": "MATERIAL", "pattern": [{"TEXT": {"REGEX": "^23\\.9-karat$"}}, {"LOWER": "gold"}, {"LOWER": "leaf"}]}'''
custom_patterns_text = st.text_area("Paste your custom patterns below:", value=example_json, height=200)

custom_patterns = []
if custom_patterns_text:
    try:
        for line in custom_patterns_text.strip().splitlines():
            custom_patterns.append(json.loads(line))
    except json.JSONDecodeError:
        st.error("⚠️ One or more lines are not valid JSON. Please check the format.")
#Processing the Text
if st.button("🔍 Analyze Text"):
    if not user_text.strip():
        st.warning("Please enter or upload some text!")
else:
    nlp = spacy.load("en_core_web_sm")
    if "entity_ruler" in nlp.pipe_names:
        nlp.remove_pipe("entity_ruler")

        doc = nlp(user_text)

ruler = nlp.add_pipe("entity_ruler", before="ner")
if custom_patterns:
    ruler.add_patterns(custom_patterns)
#Display the entites
st.markdown("### 🏷️ Detected Entities")
doc = nlp(user_text)
if doc.ents:
    for ent in doc.ents:
        st.markdown(f"- **{ent.text}** — `{ent.label_}`")
else:
    st.info("No entities found.")
#Visualizing the entities
st.markdown("### 🔎 Entity Visualization")
html = displacy.render(doc, style="ent", jupyter=False)
st.components.v1.html(html, scrolling=True, height=300)