import ImgGen
from TextGen import *
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import random
import os


# Image part
chars = ImgGen.extract_valid_chars("headlines.txt")
hexcodes = ImgGen.convert_to_hexcodes(chars)

# Text part
text = generate_poem("headlines.txt", 5, LOWERCASE)
words = text.split(" ")

def create_text_image(words, font_path="glasgow.otf", image_size=(1080, 1080), max_fontsize=150):
    """Creates a 1080x1080 image with 9 lines of evenly spaced text, ensuring no text exceeds the width."""
    
    # Ensure we have exactly 9 lines
    if len(words) != 5:
        raise ValueError("The words list must contain exactly 5 items.")

    img_width, img_height = image_size
    image = Image.new("RGB", (img_width, img_height), random.choice(hexcodes))
    draw = ImageDraw.Draw(image)
    
    # Find the maximum font size that fits all words within the image width
    def get_text_width(word, font):
        return font.getbbox(word)[2]  # Right-most coordinate
    
    # Function to get text height (more reliable than font.size)
    def get_text_height(font):
        return font.getbbox("Hg")[3]  # Bottom-most coordinate

    def find_max_fontsize(word, max_size):
        fontsize = max_size
        while fontsize > 10:
            font = ImageFont.truetype(font_path, fontsize)
            if get_text_width(word, font) <= img_width - 20:  # 10px padding on each side
                return fontsize, font
            fontsize -= 1
        return 10, ImageDraw.truetype(font_path, 10) # just a failsafe

    # Determine font size based on the widest word
    smallest_fontsize = max_fontsize
    fonts = []
    for word in words:
        fontsize, font = find_max_fontsize(word, max_fontsize)
        fonts.append(font)
        smallest_fontsize = min(smallest_fontsize, fontsize)  # Use the smallest font size for uniformity

    # Recreate fonts with the final chosen smallest size
    final_font = ImageFont.truetype(font_path, smallest_fontsize)
    line_height = get_text_height(final_font) # Get height of text

    # safe margins
    total_text_height = line_height * 6  # Space needed for all lines
    safe_margin = (img_height - total_text_height) // 3 # extra spacing for top & bottom
    spacing = (img_height - total_text_height - (2 * safe_margin)) // 6  # Even spacing

    # Draw the text, centered horizontally and evenly spaced vertically
    for i, word in enumerate(words):
        text_width = get_text_width(word, final_font)
        # x = (img_width - text_width) // 2  # Center horizontally
        x = 10
        y = safe_margin + i * (line_height + spacing)  # Even vertical distribution with margin
        draw.text((x, y), word, font=final_font, fill="black")

    return image


def save_image(image, output_dir="combined_images"):
    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save generated image to output directory with organized filenames
    filename = os.path.join(output_dir, f"post-{date.today()}.png")
    try:
        image.save(filename)
    except Exception as e:
        print(f"Error saving image {filename}: {e}")



# Example Usage
# words = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5", "Line 6", "Line 7", "Line 8", "Line 9"]
image = create_text_image(words)

save_image(image)