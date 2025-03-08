import os
from datetime import date
import TextGen
import ImgGen

# Specify File I/Os
input_file = "headlines.txt"
output_dir = "ready2post"
output_file = f"post-{date.today()}.png"

# Specify Parameters of the Poem
POEM_LENGTH = 20
MINIUM_WORD_LENGTH = 3

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save generated image to output directory with organized filenames
output_path = os.path.join(output_dir, output_file)

# Generate Poem from File
text = TextGen.import_file_as_list(input_file)
text = TextGen.remove_all_symbols(text)
text = TextGen.remove_short_words(text, MINIUM_WORD_LENGTH-1)
text = TextGen.remove_prepositions(text)
text = TextGen.remove_duplicates(text)
poem = TextGen.generate_poem(text, POEM_LENGTH, TextGen.LOWERCASE)

# Get Colors from file
hexcodes = ImgGen.extract_list_of_hexcodes_from_file(input_file)

# Combine both and create image
ImgGen.put_text_on_image(poem, output_path, background_color=ImgGen.get_random_color(hexcodes))