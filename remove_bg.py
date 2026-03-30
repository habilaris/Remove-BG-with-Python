from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):

    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()
    
    # Remove background
    output_data = remove(input_data)
    
    # Save output image
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)
    
    print(f"Background removed! Saved to: {output_path}")

def remove_background_pil(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)
    
    print(f"Background removed! Saved to: {output_path}")

if __name__ == "__main__":
    # Method 1: Using file paths directly
    remove_background("input_images/input_image.jpg", "output_images/output_image.png")
    
    # Method 2: Using PIL (optional)
    # remove_background_pil("input_images/input_image.jpg", "output_images/output_image.png")