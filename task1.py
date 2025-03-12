from PIL import Image
import io
import fitz  # PyMuPDF
import os

def extract_pdf(file_path, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    pdf_document = fitz.open(file_path)
    num_pages = pdf_document.page_count

    extracted_images = set()  # Track extracted image xref values
    total_images = 0  # Counter for unique images

    for page_num in range(num_pages):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)
        
        print(f"Processing Page {page_num + 1}: Found {len(images)} images")

        for img_index, img in enumerate(images):
            xref = img[0]
            
            if xref in extracted_images:
                print(f"Skipping duplicate image (xref={xref}) on page {page_num + 1}")
                continue  # Skip already extracted images
                
            extracted_images.add(xref)  # Mark image as extracted
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            try:
                image_pil = Image.open(io.BytesIO(image_bytes))
                resized_image = image_pil.resize((width, height), Image.Resampling.LANCZOS)
                
                total_images += 1
                image_path = os.path.join(output_folder, f"image_{total_images}.png")
                resized_image.save(image_path)
                print(f"Saved unique image {total_images} to {image_path}")

            except Exception as e:
                print(f"Error processing image {img_index + 1} on page {page_num + 1}: {e}")

    print(f"\n Total Unique Images Extracted: {total_images}")
