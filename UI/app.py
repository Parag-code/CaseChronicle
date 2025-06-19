import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Utils.pdf_parser import extract_text_from_pdf
from Utils.nlp_extractor import extract_events
from Utils.summarizer import generate_summary
from Utils.timeline_plotter import plot_timeline

st.set_page_config(page_title="CaseChronicle", layout="wide")

# Logo and Title Section
col1, col2 = st.columns([1, 4])
with col1:
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    st.image(logo_path, width=200)
with col2:
    st.title("⚖️ CaseChronicle – AI Legal Case Timeline Generator")

st.markdown("---")  # Add a horizontal line for separation

uploaded_file = st.file_uploader("📄 Upload a Legal Case PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("📑 Case Summary")
    with st.spinner("Generating summary..."):
        summary = generate_summary(text)
        st.write(summary)

    st.subheader("📊 Case Timeline")
    with st.spinner("Extracting timeline events..."):
        events = extract_events(text)
        fig = plot_timeline(events)
        st.plotly_chart(fig, use_container_width=True)
