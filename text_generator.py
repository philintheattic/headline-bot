import random
import re

KEEP_CASE = 0 # 0000
UPPERCASE = 1 # 0001
LOWERCASE = 2 # 0010
CAPITALIZE = 4 # 0100

def generate_poem(input_file="headlines.txt", length=5, flags=KEEP_CASE):
    # outputs a string of random word from an input file with a specified length
    try:
        with open(input_file, encoding="utf-8") as file:
            poem = []
            for line in file:
                words = line.strip().split(" ")
                selection = random.choice(words).strip("+?:")
                # print(selection)
                # Apply text transformations if flag is set
                if flags & LOWERCASE:
                    selection = selection.lower()
                elif flags & UPPERCASE:
                    selection = selection.upper()
                elif flags & CAPITALIZE:
                    selection = selection.capitalize()

                poem.append(selection)
            # can also be written as:
            # poem = [random.choice(line.rstrip().split(" ")) for line in file]


    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return ""

    # If the user inputs a length that is too high nothing bad happens but inform the user nonetheless
    if length > len(poem):
        print(f"Length parameter exceeded limit. Max length of {len(poem)} was used instead.")

    return " ".join(poem[:length])




if __name__ == "__main__":
    generate_poem()