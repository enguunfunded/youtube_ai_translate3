import yt_dlp
import os

def download_video(url):
    os.makedirs("input", exist_ok=True)
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'input/video.%(ext)s',
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_ext = info['ext']
        video_path = f"input/video.{video_ext}"
        audio_path = f"input/audio.wav"
        os.system(f'ffmpeg -y -i {video_path} -vn -acodec pcm_s16le -ar 16000 -ac 1 {audio_path}')
        return video_path, audio_path
