FROM python:3.10-slim

# Installiere Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

# Arbeitsverzeichnis
WORKDIR /app

# Requirements installieren
COPY requirements/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Haupt-App kopieren (liegt bei dir evtl. in src/)
COPY src/main.py .

# Port für Cloud Run (Standard 8080)
EXPOSE 8080

# App starten (HOST=0.0.0.0 ist Pflicht für Cloud Run)
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
