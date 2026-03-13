import fitz
import os

def extract_images(pdf_path):

    doc = fitz.open(pdf_path)

    os.makedirs("extracted/images", exist_ok=True)

    images = []

    for page_index in range(len(doc)):

        page = doc[page_index]

        for img_index, img in enumerate(page.get_images(full=True)):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]

            image_ext = base_image["ext"]

            image_path = f"extracted/images/page{page_index}_{img_index}.{image_ext}"

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            images.append(image_path)

    return images