from PIL import Image, ImageDraw, ImageFont
import re
import os
import textwrap
import random

#################################
### Image Generator Utilities ###
#################################

def extract_list_of_hexcodes_from_file(input_file):
    chars = extract_valid_chars(input_file)
    hexcodes = convert_to_hexcodes(chars)
    return hexcodes

# double check that this works bzw. dont forget to set hexcodes variable in the other script where you want to call it
def get_random_color(hexcodes):
    return random.choice(hexcodes)


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


def save_image(image, output_dir, index):
    # Save generated image to output directory with organized filenames
    filename = os.path.join(output_dir, f"{index:0>4}.png")
    try:
        image.save(filename)
    except Exception as e:
        print(f"Error saving image {filename}: {e}")


def put_text_on_image(words_list, output_path, background_color=(255, 255, 255), text_color=(0, 0, 0), margin_percent=10):
    """
    Place a list of words on a 1080x1080 image with dynamic font sizing and line wrapping.
    
    Args:
        words_list (list): List of words to place on the image
        output_path (str): Path to save the resulting image
        background_color (tuple): RGB color for the background
        text_color (tuple): RGB color for the text
        margin_percent (int): Percentage of image height to use as top/bottom margin
    """
    # Create a blank image
    img_size = (1080, 1080)
    img = Image.new('RGB', img_size, color=background_color)
    draw = ImageDraw.Draw(img)
    
    # Calculate margins
    margin = int(img_size[1] * (margin_percent / 100))
    text_area_height = img_size[1] - (2 * margin)
    text_area_width = img_size[0] - (2 * margin)
    
    # Join the words with spaces
    text = ' '.join(words_list)
    
    # Start with a reasonable font size
    font_size = 100
    font_path = "glasgow.otf"  # Use default font
    
    # Try to find the optimal font size
    while font_size > 10:
        font = ImageFont.truetype(font_path, size=font_size) if font_path else ImageFont.load_default().font_variant(size=font_size)
        
        # Calculate how many characters can fit per line
        avg_char_width = font.getlength('x')
        max_chars_per_line = int(text_area_width / avg_char_width)
        
        # Wrap text
        wrapped_text = textwrap.fill(text, width=max_chars_per_line)
        lines = wrapped_text.split('\n')
        
        # Calculate total text height
        line_height = font.getbbox("A")[3] + 10  # Add some line spacing
        total_text_height = line_height * len(lines)
        
        # Check if text fits within the text area
        if total_text_height <= text_area_height:
            break
        
        # Reduce font size and try again
        font_size -= 5
    
    # Calculate starting Y position to center the text block
    y_position = margin + (text_area_height - total_text_height) // 2
    
    # Draw each line of text
    for line in lines:
        # Center text horizontally
        line_width = font.getlength(line)
        x_position = (img_size[0] - line_width) // 2
        
        # Draw the text
        draw.text((x_position, y_position), line, font=font, fill=text_color)
        
        # Move to the next line
        y_position += line_height
    
    # Save the image
    img.save(output_path)
    print(f"Image saved to {output_path}")
    return img





if __name__ == "__main__":
    # Example Usage
    # put_text_on_image(words, "text_on_image.png")

