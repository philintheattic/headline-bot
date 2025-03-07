import image_generator
from text_generator import *
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import random

# Image part
chars = image_generator.extract_valid_chars("headlines.txt")
hexcodes = image_generator.convert_to_hexcodes(chars)
image = image_generator.generate_image(random.choice(hexcodes))

# Text part
text = generate_poem("headlines.txt", 9, UPPERCASE)
words = text.split(" ")


img_width, img_height = image.size
draw = ImageDraw.Draw(image)
fontsize = 150
font = ImageFont.truetype("font.otf", fontsize)
line_height= -40


def get_width_of_word(word, font):
    left, top, right, bottom = font.getbbox(word)
    return (right - left) + 50

def resize_word(word, fontsize):
    while True:
        font = ImageFont.truetype("font.otf", fontsize)
        if get_width_of_word(word, font) < img_width:
            break
        fontsize -= 1
    return font


for i, word in enumerate(words):

    draw.text((10, (fontsize+line_height)*i), word, font=resize_word(word, fontsize), fill='black')

output_path = f"combined_images/post-{date.today()}.png"

image.save(output_path)