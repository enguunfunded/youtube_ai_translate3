import whisper
import os

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    segments = result['segments']

    # 🎯 Лаан бүрийн эхлэл төгсгөл, текстийг буцаана
    transcript = []
    for seg in segments:
        transcript.append({
            'start': seg['start'],
            'end': seg['end'],
            'text': seg['text']
        })
    return transcript
