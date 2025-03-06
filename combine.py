import image_generator
from text_generator import *
from PIL import Image, ImageDraw, ImageFont
from datetime import date


text = generate_poem("headlines.txt", 9, UPPERCASE)
words = text.split(" ")

image = Image.open("generated_images/0000-#Bdebae.png")
width, height = image.size

draw = ImageDraw.Draw(image)
fontsize = 150
font = ImageFont.truetype("font.otf", fontsize)
line_height= -40

for i, word in enumerate(words):
    draw.text((10, (fontsize+line_height)*i), word, font=font, fill='black')

output_path = f"combined_images/post-{date.today()}.png"

image.save(output_path)