from gtts.tts import gTTS
import streamlit as st
from pipeline import run_pipeline
import PyPDF2
from docx import Document 
from gtts import gTTS
import tempfile 

# -------------------------
# Function to extract text
# -------------------------
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text

    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    else:
        st.error("Unsupported file format! Please upload .txt, .pdf, or .docx")
        return None

# -------------------------
# Streamlit UI
# -------------------------
st.title("📜 Legal Document Summarization & Simplification")

st.write(
    "Upload a legal document (.txt, .pdf, .docx), "
    "choose a task, select your language, and get simplified/summarized output with speech."
)

# File uploader
uploaded_file = st.file_uploader("Upload your legal document", type=["txt", "pdf", "docx"])

# Task selection
task = st.selectbox("Choose Task", ["Summarize", "Simplify"])

# Language selection
language = st.selectbox(
    "Choose Output Language",
    [
        "english", "hindi", "marathi", "tamil", "telugu", "bengali", "gujrati", "kannada", "malyalam", "punjabi", "urdu"
    ],
    index=0
)

def process_document(text, task, language):
    # Example: Summarization task
    if task == "summarize":
        output_text = text[:500] + "..." if len(text) > 500 else text  # simple trim summarization
    elif task == "translate":
        # Placeholder for translation (could integrate Googletrans or Hugging Face)
        output_text = f"[Translated to {language}] " + text
    else:
        output_text = text  # default - return original

    # Convert to speech
    tts = gTTS(output_text, lang=language)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)

    return output_text, tmp_file.name

    

if uploaded_file is not None:
    text = extract_text_from_file(uploaded_file)
    if text:
        if st.button("Process Document"):
            with st.spinner("Processing..."):
                output_text, audio_file = process_document(text, task, language)

            # Display text output
            st.subheader("Processed Output:")
            st.write(output_text)

            # Display audio output
            st.subheader("Speech Output:")
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")
