from PIL import Image
import os

def convert_webp_to_png(input_file, output_file):
    try:
        image = Image.open(input_file)
        if image.mode != "RGBA":
            image = image.convert("RGBA")
        image.save(output_file, "PNG")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error converting the image: {e}")

if __name__ == "__main__":
    input_file = "2023-bmw-m2.webp"  # Replace with the path to your .webp file
    output_file = "2023-bmw-m2.png"  # Replace with the desired output .png file name

    convert_webp_to_png(input_file, output_file)

