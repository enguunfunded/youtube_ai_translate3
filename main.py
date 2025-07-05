from transcribe import transcribe_audio
from translate import translate_text
from subtitle import generate_srt
# бусад хэсэг хэвээрээ

eng_segments = transcribe_audio(audio_path)
mon_segments = translate_text(eng_segments)
srt_path = generate_srt(mon_segments)
