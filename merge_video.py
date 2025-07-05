import os

def burn_subtitle(video_path, srt_path):
    output_path = 'output/final_video.mp4'
    command = f'ffmpeg -y -i "{video_path}" -vf "subtitles={srt_path}:charenc=UTF-8" "{output_path}"'
    os.system(command)
    return output_path

