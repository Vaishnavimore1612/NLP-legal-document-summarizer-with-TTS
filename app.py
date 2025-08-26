import streamlit as st
from pipeline import run_pipeline   #type:ignore 

st.title("📜 Legal Document Summarization & Simplification")
st.write("Upload a legal document, choose task (summarize/simplify), select language, and get both text & speech output.")

uploaded_file = st.file_uploader("Upload Legal Document (.txt)", type=["txt"])
task = st.selectbox("Choose Task", ["summarize", "simplify"])
language = st.selectbox("Translate to Language", ["en", "hi", "mr", "bn", "ta", "te", "gu", "kn", "ml", "pa", "ur"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    if st.button("Process"):
        result_text, audio_path = run_pipeline(text, task, language)

        st.subheader("📝 Processed Text")
        st.write(result_text)

        st.subheader("🔊 Speech Output")
        audio_file = open(audio_path, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
