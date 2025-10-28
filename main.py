from fastapi import FastAPI, UploadFile
from io import BytesIO
from PIL import Image
import pytesseract as pt
import requests

app = FastAPI()

@app.post("/ocr")
async def image_to_text(raw_image_url: dict):
    """
    Lädt ein Bild von einer URL und extrahiert Text mittels Tesseract OCR.
    Gibt den erkannten Text zurück (oder einen leeren String bei Fehlern).
    """
    try:
        resp = requests.get(raw_image_url["url"], timeout=10)
        resp.raise_for_status()  # HTTP-error if not 200

        img = Image.open(BytesIO(resp.content)).convert("L")  # makes image grey -> better readability for extracting 

        text = pt.image_to_string(img).strip()

        if text:
            print("Textauslesung erfolgreich.")
        else:
            print("Kein Text erkannt.")
        return text

    except Exception as e:
        print("Fehler bei der OCR-Verarbeitung: {}".format(e))
        return ""
