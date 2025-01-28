# 1️⃣ Wähle ein Basis-Image mit Python
FROM python:3.9-slim

# 2️⃣ Setze Arbeitsverzeichnis
WORKDIR /app

# 3️⃣ Kopiere die Anwendungsdateien in das Image
COPY . .

# 4️⃣ Installiere alle erforderlichen Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Setze Umgebungsvariable für Cloud Run
ENV PORT 8080

# 6️⃣ Starte die Flask-App
CMD ["python", "TRANSCRIBE.py"]
