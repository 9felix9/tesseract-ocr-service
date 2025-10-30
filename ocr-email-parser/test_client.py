import requests
from PIL import Image
from io import BytesIO

url = "https://dashboard.trustprofile.com/webshops/email/4034045.png?m=1761807591"
resp = requests.get(url)
img = Image.open(BytesIO(resp.content))

buf = BytesIO()
img.save(buf, format="{}".format(img.format))
buf.seek(0)

# Als "Datei" an den Microservice schicken (ohne sie wirklich zu speichern)
response = requests.post(
    "http://127.0.0.1:8000/ocr",
    files={"file": buf.getvalue()}
)

print(response.json())
