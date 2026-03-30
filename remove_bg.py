import os
from rembg import remove, new_session
from PIL import Image

def remove_bg_pro(input_path, output_path):
    # 1. Initialize a specialized session
    # 'u2net' is generally best for non-photorealistic/doodle art
    model_name = "u2net"
    session = new_session(model_name)

    try:
        # 2. Open the image using PIL
        # We use PIL to ensure we can handle different color profiles correctly
        img = Image.open(input_path)

        # 3. Remove background with Alpha Matting
        # This creates a much smoother transition on the edges of the hair/suit
        output = remove(
            img,
            session=session,
            alpha_matting=True,
            alpha_matting_foreground_threshold=240,
            alpha_matting_background_threshold=10,
            alpha_matting_erode_size=10
        )

        # 4. Save as PNG (Must be PNG to keep transparency)
        # We use 'optimize=True' to keep file size down without losing quality
        output.save(output_path, "PNG", optimize=True)
        
        print(f"✅ Success! Subject isolated and saved to: {output_path}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    # Ensure these files exist in your folder
    INPUT = "input_images/input_image.png"
    OUTPUT = "output_images/habil_isolated.png"

    if os.path.exists(INPUT):
        remove_bg_pro(INPUT, OUTPUT)
    else:
        print(f"File {INPUT} not found. Please check the filename!")