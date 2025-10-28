FROM python:3.10-slim

RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# hiermit wird der Port "öffentlich" gemacht - docker hat standardmäßig keinen Port offen
EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]