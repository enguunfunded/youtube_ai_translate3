import pysrt
import os

def generate_srt(text, duration_per_line=5):
    os.makedirs("output", exist_ok=True)
    lines = text.split('. ')
    subs = pysrt.SubRipFile()
    for i, line in enumerate(lines):
        start = i * duration_per_line
        end = start + duration_per_line
        subs.append(pysrt.SubRipItem(
            index=i+1,
            start=pysrt.SubRipTime(seconds=start),
            end=pysrt.SubRipTime(seconds=end),
            text=line.strip()
        ))
    srt_path = 'output/subtitles.srt'
    subs.save(srt_path, encoding='utf-8')
    return srt_path
