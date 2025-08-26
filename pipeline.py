from summarizer import summarize_text  #type:ignore
from simplifier import simplify_text   #type:ignore
from translation import translate_text #type:ignore
from gtts import text_to_speech

def process_document(input_text, task="summarize", target_lang="hi", with_audio=False):
    if task == "summarize":
        english_output = summarize_text(input_text)
    else:
        english_output = simplify_text(input_text)

    translated_output = translate_text(english_output, target_lang)

    audio_file = None
    if with_audio:
        audio_file = text_to_speech(translated_output, target_lang)

    return english_output, translated_output, audio_file

