from googletrans import Translator

def translate_text(segments):
    translator = Translator()
    translated_segments = []
    for seg in segments:
        translated = translator.translate(seg['text'], src='en', dest='mn')
        translated_segments.append({
            'start': seg['start'],
            'end': seg['end'],
            'text': translated.text
        })
    return translated_segments
