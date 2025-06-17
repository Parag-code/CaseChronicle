# ⚖️ CaseChronicle – AI Legal Case Timeline Generator

**CaseChronicle** is an AI-powered web application that helps legal professionals, students, and researchers quickly understand the sequence of events in legal cases. By uploading a legal case PDF, the app extracts text, generates a concise summary, and visually plots key events as a timeline.

---

## 🚀 Features

🔍 **PDF Parsing**  
Extracts and processes legal case documents in PDF format using NLP.

🧠 **AI-Powered Summary**  
Automatically generates a brief and clear summary of the case using advanced text summarization.

📆 **Event Extraction**  
Uses NLP techniques to extract important legal events and dates from the case document.

📊 **Timeline Visualization**  
Displays a dynamic, interactive timeline chart to visualize the chronological flow of legal events.

📤 **User-Friendly Upload Interface**  
Streamlit-based frontend for easy and intuitive PDF uploads and result display.

---

## 📂 How It Works

1. **Upload a legal case PDF**  
   Upload any legal case in PDF format using the web interface.

2. **Text Extraction**  
   The app extracts raw text from the PDF using custom parsing logic.

3. **Summarization**  
   The extracted text is processed to generate a high-level summary of the case.

4. **Event Detection**  
   Key events (like filings, hearings, judgments) are identified and timestamped.

5. **Timeline Generation**  
   Events are plotted on an interactive timeline using Plotly.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**: 
  - `PyMuPDF` or similar (for PDF parsing)
  - `spaCy` / `transformers` (for NLP tasks)
  - `Plotly` (for interactive timeline charts)

## 📸 Example Output

- **Generated Case Summary**:  
> "The petitioner filed a writ challenging the dismissal order issued on Jan 3, 2021. A hearing was held on Feb 5, 2021..."

- **Interactive Timeline**:  
> A Plotly chart showing events such as case filing, hearing dates, evidence submissions, and verdicts.

---
