from PIL import Image
import os

def convert_webp_to_jpg(input_file, output_file):
    try:
        image = Image.open(input_file)
        rgb_image = image.convert("RGB")
        rgb_image.save(output_file, "JPEG")
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Error converting the image: {e}")

if __name__ == "__main__":
    input_file = "2023-bmw-m2.webp"  # Replace with the path to your .webp file
    output_file = "2023-bmw-m2.jpg"  # Replace with the desired output .jpg file name

    convert_webp_to_jpg(input_file, output_file)

