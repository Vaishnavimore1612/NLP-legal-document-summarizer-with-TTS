from transformers import pipeline

# Using paraphrase model for simplification
simplifier = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def simplify_text(text):
    result = simplifier(f"simplify: {text}", max_length=150, do_sample=True)
    return result[0]['generated_text']

