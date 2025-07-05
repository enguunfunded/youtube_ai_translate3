from transformers import MarianMTModel, MarianTokenizer

def translate_text(text):
    src = "en"
    tgt = "mn"
    model_name = f'Helsinki-NLP/opus-mt-{src}-{tgt}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    inputs = tokenizer([text], return_tensors="pt", truncation=True, max_length=512)
    translated = model.generate(**inputs)
    result = tokenizer.decode(translated[0], skip_special_tokens=True)
    return result
