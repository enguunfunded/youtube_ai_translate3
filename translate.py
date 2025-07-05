from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='mn')
    return translated.text
