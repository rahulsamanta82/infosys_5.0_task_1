import fitz
from PIL import Image
import os
import io

def extract_pictures_from_pdf(pdf_path, save_folder, img_width, img_height):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    try:
        pdf_file = fitz.open(pdf_path)
        num_pages = pdf_file.page_count
        
        for page_idx in range(num_pages):
            current_page = pdf_file.load_page(page_idx)
            pictures = current_page.get_images(full=True)
            print(f"Processing Page {page_idx + 1}...")
            
            for pic_idx, pic in enumerate(pictures):
                ref_id = pic[0]
                extracted_image = pdf_file.extract_image(ref_id)
                img_data = extracted_image["image"]
                print(f"  Extracting Image {pic_idx + 1}: Size = {len(img_data)} bytes, Ref = {ref_id}")
                
                try:
                    img_pil = Image.open(io.BytesIO(img_data))
                    resized_pic = img_pil.resize((img_width, img_height), Image.Resampling.LANCZOS)
                    img_file_path = os.path.join(save_folder, f"page_{page_idx + 1}_image_{pic_idx + 1}.png")
                    resized_pic.save(img_file_path)
                    print(f"  Saved: {img_file_path}")
                except Exception as error:
                    print(f"  Error processing image {pic_idx + 1} on page {page_idx + 1}: {error}")
        
        print("Image extraction completed successfully.")
    except Exception as error:
        print(f"Error opening PDF file: {error}")

# Parameters
pdf_file_path = "mycheque.pdf"
output_folder = "outputs"
image_width, image_height = 1200, 600

# Run extraction
extract_pictures_from_pdf(pdf_file_path, output_folder, image_width, image_height)
