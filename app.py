from modules.pdf_parser import parse_pdf
from modules.image_extractor import extract_images
from modules.observation_extractor import extract_observations
from modules.observation_merger import merge_observations
from modules.ddr_generator import generate_ddr


INSPECTION_PDF = "data/inspection_report.pdf"
THERMAL_PDF = "data/thermal_report.pdf"


print("Extracting text")

inspection_pages = parse_pdf(INSPECTION_PDF)


print("Extracting images")

images = extract_images(THERMAL_PDF)


print("Extracting observations")

inspection_text = ""

for page in inspection_pages:
    inspection_text += page["text"] + "\n"


inspection_obs = extract_observations(inspection_text)


print("Merging observations")

merged_obs = merge_observations(inspection_obs)


print("Generating DDR report")

report = generate_ddr(merged_obs)


with open("DDR_Report.md", "w", encoding="utf-8") as f:
    f.write(report)


print("DDR report generated successfully")