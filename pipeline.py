from transformers import pipeline
from gtts import gTTS
import os


# ---------------- Summarization ----------------
def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return summary[0]['summary_text']


# ---------------- Text-to-Speech ----------------
def text_to_speech(text: str, filename: str = "output.mp3") -> str:
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename


# ---------------- Main Pipeline ----------------
def run_pipeline(text: str, enable_tts: bool = True) -> dict:
    """
    Runs summarization and (optional) TTS.
    Returns dictionary with summary and audio path (if generated).
    """
    result = {}

    # Summarize
    summary = summarize_text(text)
    result["summary"] = summary

    # TTS
    if enable_tts:
        audio_file = text_to_speech(summary, "summary_audio.mp3")
        result["audio_file"] = audio_file

    return result


# ---------------- Local Testing ----------------
if __name__ == "__main__":
    sample_text = """
    This Agreement is entered into by and between Party A and Party B, 
    with the intention of establishing mutual obligations, rights, and duties.
    The Agreement shall remain in effect until terminated by either party with prior notice.
    """
    output = run_pipeline(sample_text, enable_tts=True)
    print("Summary:", output["summary"])
    if "audio_file" in output:
        print("Audio file saved at:", output["audio_file"])


