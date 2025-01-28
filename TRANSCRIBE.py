# Installiere die YouTube Transcript API, falls sie nicht installiert ist
import os
try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    os.system("pip install youtube-transcript-api")
    from youtube_transcript_api import YouTubeTranscriptApi

# Funktion, um ein Transcript für ein Video zu holen
def get_transcript(video_id):
    try:
        # Holt die Untertitel
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print("\nTranskript:")
        for line in transcript:
            print(f"{line['start']:.2f}s: {line['text']}")
    except Exception as e:
        print(f"Fehler beim Abrufen des Transkripts: {e}")

# Hauptprogramm
if __name__ == "__main__":
    print("Willkommen zur YouTube Transcript API! 🚀")
    # Eingabe der YouTube-Video-ID
    video_url = input("Gib die YouTube-URL ein: ").strip()

    # Extrahiere die Video-ID aus der URL
    if "youtube.com" in video_url or "youtu.be" in video_url:
        if "v=" in video_url:
            video_id = video_url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[-1].split("?")[0]
        else:
            video_id = video_url
    else:
        print("Ungültige URL. Bitte gib eine gültige YouTube-URL ein.")
        exit()

    # Hole das Transkript
    get_transcript(video_id)
