import pysrt
import os

def generate_srt(translated_segments):
    os.makedirs("output", exist_ok=True)
    subs = pysrt.SubRipFile()

    for i, seg in enumerate(translated_segments):
        subs.append(pysrt.SubRipItem(
            index=i+1,
            start=pysrt.SubRipTime(seconds=seg['start']),
            end=pysrt.SubRipTime(seconds=seg['end']),
            text=seg['text'].strip()
        ))

    srt_path = 'output/subtitles.srt'
    with open(srt_path, "w", encoding="utf-8") as f:
        subs.write_into(f)

    return srt_path
