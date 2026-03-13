# DDR AI System

A simple AI-based system that processes inspection PDFs and generates a **Detailed Diagnostic Report (DDR)** in Markdown format.

## Features

* Upload one or more PDF reports
* Extract text and images from PDFs
* Identify observations using an LLM
* Merge observations
* Generate a structured DDR report
* Download the report as a `.md` file
* FastAPI API interface
* Docker support for deployment

## Tech Stack

* Python
* FastAPI
* OpenRouter LLM
* PyMuPDF
* Docker

## Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the API:

```
uvicorn api:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### Generate DDR Report

**POST** `/generate-ddr`

Upload one or more PDF files and receive a generated DDR report.

Response:
Downloadable `DDR_Report.md` file.

## Docker

Build the image:

```
docker build -t ddr-ai-system .
```

Run the container:

```
docker run -p 8000:8000 ddr-ai-system
```

## Project Structure

```
DDR_submit
│
├── api.py
├── app.py
│
├── modules
│   ├── pdf_parser.py
│   ├── image_extractor.py
│   ├── openrouter_client.py
│   ├── observation_extractor.py
│   ├── observation_merger.py
│   └── ddr_generator.py
│
├── data
│   ├── inspection_report.pdf
│   └── thermal_report.pdf
│
├── extracted
│   ├── images
│   └── parsed_text.json
│
├── uploads
│
├── reports
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
└── README.md
```

## Output

The system generates a **Markdown DDR report** from uploaded inspection PDFs.

Example output:

```
DDR_Report.md
```

This report contains summarized observations, analysis, and diagnostic recommendations extracted from the uploaded reports.
