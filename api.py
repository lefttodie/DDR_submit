from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import uuid
import os

from modules.pdf_parser import parse_pdf
from modules.observation_extractor import extract_observations
from modules.observation_merger import merge_observations
from modules.ddr_generator import generate_ddr

app = FastAPI()

UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)


@app.post("/generate-ddr")
async def generate_ddr_report(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):

    file_id = str(uuid.uuid4())
    inspection_text = ""

    files = [file1, file2]

    for file in files:

        pdf_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

        with open(pdf_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        pages = parse_pdf(pdf_path)

        for page in pages:
            inspection_text += page["text"] + "\n"

    # Extract observations
    observations = extract_observations(inspection_text)

    # Merge observations
    merged = merge_observations(observations)

    # Generate DDR report
    report = generate_ddr(merged)

    report_path = f"{REPORT_DIR}/{file_id}.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    return FileResponse(
        report_path,
        media_type="text/markdown",
        filename="DDR_Report.md"
    )