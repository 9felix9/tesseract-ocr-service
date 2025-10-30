# ocr-email-parser

## Description

This service is a FastAPI-based OCR (Optical Character Recognition) microservice that extracts text from images. The service uses Tesseract OCR for text recognition from uploaded image files (JPG, PNG, etc.).

**Main Features:**
- `/ocr` POST endpoint for text extraction from images
- Automatic image conversion to grayscale for better OCR accuracy
- Error handling and detailed response messages
- Support for various image formats

The service is containerized and can be easily deployed via Docker Compose.

## Assumptions
- fastAPI project
- some kind of model needs to be loaded

## Deployment
- fast deployment via `docker-compose up`
- prod config in `docker-compose.override.yml`
### Requirements

## Development
- Run tests with `make test`
- Lint with `lint`. Additional flake8 check via `lint-check`
### Devcontainer (recommended)
- VS Code required
- Needs the dev containers extension https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

### Local dev
- Set up by running `make setup-local && make setup-dev-local`