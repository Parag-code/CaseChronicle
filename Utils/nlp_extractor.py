import streamlit as st
import spacy

@st.cache_resource
def get_nlp():
    return spacy.load("en_core_web_sm")

def extract_events(text):
    nlp = get_nlp()
    doc = nlp(text)
    events = []
    for sent in doc.sents:
        for ent in sent.ents:
            if ent.label_ == "DATE":
                events.append({
                    "date": ent.text,
                    "event": sent.text.strip()
                })
                break
    return events