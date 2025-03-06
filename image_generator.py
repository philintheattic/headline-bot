from PIL import Image
import re
import os


def extract_valid_chars(input_file):
    # Extracts only hex-compatible characters (0-9, A-F) from a file
    try:
        with open(input_file) as file:
            return [char for line in file for char in line if re.match(r"[a-fA-F0-9]", char)]
    except FileNotFoundError:
        print(f"Error: the file '{input_file}' was not found.")
        return[]
    except Exception as e:
        print(f"an error occured while reading the file: {e}")
        return []

def convert_to_hexcodes(chars):
    # Converts a list of characters into full hex color codes
    return [f"#{''.join(chars[i:i+6]).ljust(6, '0')}" for i in range(0, len(chars), 6)]
    

def generate_image(hexcode, width=1080, height=1080):
    # create blank image filled with hex color
    return Image.new('RGB', (width, height), color=hexcode)


def save_image(image, output_dir, index, hexcode):
    # Save generated image to output directory with organized filenames
    filename = os.path.join(output_dir, f"{index:0>4}-{hexcode}.png")
    try:
        image.save(filename)
    except Exception as e:
        print(f"Error saving image {filename}: {e}")


def start_image_generator(input_file="headlines.txt", output_dir="generated_images"):
    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    chars = extract_valid_chars(input_file)
    hexcodes = convert_to_hexcodes(chars)

    for index, hexcode in enumerate(hexcodes):
        image = generate_image(hexcode)
        save_image(image, output_dir, index, hexcode)


if __name__ == "__main__":
    start_image_generator()