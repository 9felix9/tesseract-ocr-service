from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
import pytesseract as pt

app = FastAPI(
    title="OCR Service for Text Extraction from Images",
    description="Microservice for Optical Character Recognition (OCR) on images and screenshots using Tesseract.",
)

@app.post(
    "/ocr",
    summary="Extract text from an uploaded image",
    description="This endpoint receives an image file (e.g., JPG or PNG) and performs Optical Character Recognition (OCR) using Tesseract. "
                "The extracted text is returned as plain text.",
)
def image_to_text(
    file: UploadFile = File(..., description="The image file to be uploaded (e.g., JPG or PNG).")
):
    """
    Receives an image (UploadFile) and extracts text using Tesseract OCR.
    Returns the recognized text as a string.
    """
    try:
        # Read the uploaded file
        image_bytes = file.file.read()

        # Convert to grayscale for better OCR accuracy
        img = Image.open(BytesIO(image_bytes)).convert("L")

        # Perform OCR using Tesseract
        text = pt.image_to_string(img).strip()

        if text:
            print(f"Text successfully extracted ({len(text)} characters).")
        else:
            print("No text detected in the image.")

        return {"text": text}

    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return {"error": f"Exception occurred: {str(e)}"}


if __name__ == "__main__":
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser(
        description="Running the dev api server, if main module."
    )
    parser.add_argument("port", type=int, help="Port number")
    args = parser.parse_args()

    uvicorn.run(app, host="0.0.0.0", port=args.port)
