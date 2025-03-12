import os
import logging
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import pandas as pd

# Load the processor and model
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-stage1')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-stage1')

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values, max_new_tokens=50)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_text.strip()
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        return ""

def process_all_folders(base_dir, output_file):
    data = []

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            folder_data = {"Folder": folder_name}
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('png', 'jpg', 'jpeg')):
                    image_path = os.path.join(folder_path, file_name)
                    extracted_text = extract_text_from_image(image_path)
                    column_name = os.path.splitext(file_name)[0]
                    folder_data[column_name] = extracted_text
            data.append(folder_data)

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
