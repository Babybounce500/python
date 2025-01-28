# 1️⃣ Basis-Image mit Python
FROM python:3.9

# 2️⃣ Setze Arbeitsverzeichnis
WORKDIR /app

# 3️⃣ Kopiere alle Dateien ins Image
COPY . .

# 4️⃣ Installiere Flask & YouTube API Library
RUN pip install --no-cache-dir flask youtube-transcript-api

# 5️⃣ Setze Umgebungsvariable für Cloud Run
ENV PORT=8080

# 6️⃣ Starte die Flask-App
CMD ["python", "TRANSCRIBE.py"]
