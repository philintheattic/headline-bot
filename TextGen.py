import random
import re

################################
### Text Generator Utilities ###
################################

# CONSTANTS (Mainly used for stylizing all Word as upper- or lowercase or capitalizing. Pass as flag in the generate_poem() function)
KEEP_CASE = 0 # 0000
UPPERCASE = 1 # 0001
LOWERCASE = 2 # 0010
CAPITALIZE = 4 # 0100

# List of prepositions for filtering. Feel free to use your own sets
PREPOSITIONS = {
    "an", "auf", "hinter", "in", "neben", "über", "unter", "vor", "zwischen",
    "aus", "bei", "mit", "nach", "seit", "von", "zu", "gegen", "ohne", "um", "am",
    "während", "wegen", "trotz", "wider", "entlang", "innerhalb", "außerhalb"
}


# Take a .txt file and prepare it as a list for further filtering
def import_file_as_list(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            corpus = []
            for line in f:
                corpus.extend(line.strip().split(" "))
            return corpus
        
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return []


# Cleans up the input by removing all symbols, whitespaces etc. 
def remove_all_symbols(input_list):
    corpus = []
    for line in input_list:
        corpus.extend(re.findall(r"\w+", line, re.IGNORECASE))
    return corpus
    

# Filter out short words or single letters
def remove_short_words(input_list, maxlength=2):
    return list(filter(lambda word: len(word) > maxlength, input_list ))
    

# Filter out prepositions via a hard coded list. See PREPOSITIONS at the top of this file
def remove_prepositions(input_list):
    return list(filter(lambda word: word.lower() not in PREPOSITIONS, input_list))


# filter out duplicates
def remove_duplicates(input_list):
    return list(set(input_list))


# Spit out random selection of words from the list
def generate_poem(input_list, length=5, flags=KEEP_CASE):
    output_list = []
    for word in input_list:
        if flags & LOWERCASE:
            word = word.lower()
        elif flags & UPPERCASE:
            word = word.upper()
        elif flags & CAPITALIZE:
            word = word.capitalize()
        output_list.append(word)
        
    return random.sample(output_list, length)
    


if __name__ == "__main__":
    # Example Usage:

    # Import a text file
    text = import_file_as_list("headlines.txt")
    
    # Use following functions to filter the list as you wish
    text = remove_all_symbols(text)
    text = remove_short_words(text, maxlength=2)
    text = remove_prepositions(text)
    text = remove_duplicates(text)

    # Generate a new random poem each time with specified length
    poem = generate_poem(input_list=text, length=5, flags=KEEP_CASE)
    print(poem)