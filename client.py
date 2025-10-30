import requests
payload = {
  "url": "https://dashboard.trustprofile.com/webshops/email/4034104.png?m=1761655122"
}
OCR_ENDPOINT = "https://tesseract-ocr-service-22755122169.europe-west1.run.app/ocr"

print(requests.post(OCR_ENDPOINT, json=payload).text)