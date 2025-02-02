import cv2
import os
import numpy as np
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
dir = os.getenv("DIR")

def process_signature(image_path, output_path):
    try:
        # Read the image
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise ValueError("Could not read the image")

        # Normalize image size
        max_dim = 800
        height, width = img.shape
        if width > max_dim or height > max_dim:
            scale = max_dim / max(width, height)
            img = cv2.resize(img, None, fx=scale, fy=scale)

        # Enhance contrast
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img = clahe.apply(img)

        # Apply adaptive thresholding
        binary = cv2.adaptiveThreshold(
            img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 11, 2
        )

        # Remove noise
        processed = cv2.medianBlur(binary, 3)

        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save processed image
        cv2.imwrite(output_path, processed)
        return output_path

    except Exception as e:
        print(f"Error processing signature: {str(e)}")
        return None

# Experimental usage
if __name__ == "__main__":
    shared_dir = f"{dir}/testing_images"
    input_path = f"{shared_dir}/unclean_sample.jpg"
    output_path = f"{shared_dir}/clean_sample.png"
    result = process_signature(input_path, output_path)
    if result:
        print(f"Processed signature saved to: {result}")