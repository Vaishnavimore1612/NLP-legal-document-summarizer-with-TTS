from gtts import gTTS
import os

def text_to_speech(text, lang="hi"):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "output_audio.mp3"
    tts.save(filename)
    return filename

