from utils.video_downloader import download_video
from transcribe import transcribe_audio
from translate import translate_text
from subtitle import generate_srt
from merge_video import burn_subtitle

def main(youtube_url):
    print("🔻 Видеог татаж байна...")
    video_path, audio_path = download_video(youtube_url)

    print("🔊 Англи текст үүсгэж байна...")
    eng_text = transcribe_audio(audio_path)

    print("🌐 Монгол руу орчуулж байна...")
    mon_text = translate_text(eng_text)

    print("📄 Subtitle файл үүсгэж байна...")
    srt_path = generate_srt(mon_text)

    print("🎬 Subtitle-г видео дээр шатааж байна...")
    output_video = burn_subtitle(video_path, srt_path)

    print(f"✅ Дууслаа: {output_video}")

if __name__ == "__main__":
    yt_url = input("👉 YouTube видео линк оруулна уу: ")
    main(yt_url)
