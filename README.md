# NLP-legal-document-summarizer-with-TTS

This is a Streamlit web app built in Python that uses NLP to summarize, simplify, translate, and convert legal documents into speech. It helps users understand complex legal language in a simpler, translated, and spoken form.

## Features

Summarization, condenses long legal texts into short, clear summaries.

Simplification, rewrites legal jargon into easy-to-understand language.

Translation, supports multiple Indian languages (hi, mr, ta, te, bn, gu, kn, ml, pa, ur, en).

Speech Output, converts processed text into audio (MP3) while retaining the text output.

Web UI, built using Streamlit for easy document upload and interaction.


 ## Project Structure

app.py → Streamlit app (UI)

pipeline.py → NLP pipeline for summarization, simplification, translation & TTS

requirements.txt → List of dependencies

utils/ → Helper functions (optional future use)

sample_docs/ → Sample test files (.txt, .pdf, .docx)

contract_sample.txt

agreement_sample.pdf

case_law_sample.docx

## Installation
1. Clone the Repository
git clone https://github.com/your-username/legaldoc-summarization.git
cd legaldoc-summarization

2. Create a Virtual Environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Linux/Mac

3. Install Dependencies
pip install -r requirements.txt

 ## Running the App
streamlit run app.py

If Streamlit runs successfully, you’ll see:

Local URL: http://localhost:8501

Open this link in your browser to use the app.

## Usage

Upload a .txt legal document.

Select Task → Summarize or Simplify.

Select Language → English, Hindi, Marathi, Tamil, Telugu, etc.

Click Process → Get the simplified or summarized output in the chosen language.

Listen to the speech output (MP3) or read the text output.

## Tech Stack

Python 3.8+

Streamlit – Web UI

Transformers (HuggingFace) – NLP models

Torch – Deep learning backend

gTTS – Text-to-Speech

Googletrans – Translation (supports Indian languages)

## Example Output

Input: Long legal contract text (~2000 words)  
Output:  
✔ Summarized → 3 to 4 paragraphs  
✔ Simplified → Easy-to-read sentences  
✔ Translated → Hindi, Marathi, Tamil, Telugu, etc.  
✔ Speech → MP3 audio playback  

## License

This project is licensed under the MIT License, which allows free use and modification.

## Future Improvements

More Indian language dialects.

Offline translation and TTS (no API dependency).

Fine-tuned models specific to legal documents.
