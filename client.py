import requests
payload = {
  "url": "https://www.toushenne.de/files/2021/bilder/unformatierter-text.png"
}
OCR_ENDPOINT = "http://localhost:8000/ocr"

print(requests.post(OCR_ENDPOINT, json=payload).text)