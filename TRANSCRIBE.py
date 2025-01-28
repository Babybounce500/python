import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- NEU
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)  # <-- Erlaubt externe Anfragen (z. B. von deiner Homepage)

@app.route("/")
def home():
    return "YouTube Transcript API läuft! 🚀"

@app.route("/transcribe", methods=["GET"])
def transcribe():
    video_url = request.args.get("url")
    if not video_url:
        return jsonify({"error": "Keine URL angegeben"}), 400

    try:
        if "youtube.com" in video_url or "youtu.be" in video_url:
            if "v=" in video_url:
                video_id = video_url.split("v=")[-1].split("&")[0]
            elif "youtu.be/" in video_url:
                video_id = video_url.split("youtu.be/")[-1].split("?")[0]
            else:
                video_id = video_url
        else:
            return jsonify({"error": "Ungültige URL"}), 400

        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
