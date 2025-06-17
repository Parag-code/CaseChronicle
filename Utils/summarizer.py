import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def generate_summary(text):
    summarizer = get_summarizer()
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']