from transformers import pipeline

# Helsinki-NLP models support most Indian languages
def translate_text(text, target_lang="hi"):
    if target_lang == "en":
        return text
    
    model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
    translator = pipeline("translation", model=model_name)
    result = translator(text)
    return result[0]['translation_text']
