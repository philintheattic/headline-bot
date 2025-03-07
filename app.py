import TextGen
import ImgGen

input_file = "headlines.txt"
output_path = "combined_images/test.png"

# Generate Poem from File
text = TextGen.import_file_as_list("headlines.txt")
text = TextGen.remove_all_symbols(text)
text = TextGen.remove_short_words(text, maxlength=2)
text = TextGen.remove_prepositions(text)
text = TextGen.remove_duplicates(text)
poem = TextGen.generate_poem(text, 20, TextGen.LOWERCASE)

# Get Colors from file
hexcodes = ImgGen.extract_list_of_hexcodes_from_file("headlines.txt")
print(hexcodes)

# Combine both and create image
ImgGen.put_text_on_image(poem, output_path, background_color=ImgGen.get_random_color(hexcodes))





