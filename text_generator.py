import random

def generate_poem(input_file="headlines.txt", length=5):
    # outputs a string of random word from an input file with a specified length
    try:
        with open(input_file, encoding="utf-8") as file:
            poem = []
            for line in file:
                word = line.rstrip().split(" ")
                selection = random.choice(word)
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