# 1️⃣ Basis-Image: Nutze Python 3.9
FROM python:3.9

# 2️⃣ Setze Arbeitsverzeichnis im Container
WORKDIR /app

# 3️⃣ Kopiere das Skript in den Container
COPY TRANSCRIBE.py .

# 4️⃣ Installiere die benötigte Bibliothek
RUN pip install youtube-transcript-api

# 5️⃣ Starte das Skript automatisch
CMD ["python", "TRANSCRIBE1.py"]
