import random

nouns = []
verbs = []
adjectives = []
sentence_structures = [
    ["NOUN", "VERB", "ADJ", "NOUN"],
    ["ADJ", "NOUN", "VERB"],
    ["NOUN", "VERB", "ADJ"]
]

word_pools = {"NOUN": nouns, "VERB": verbs, "ADJ": adjectives}

def fill_word_pool(nouns: list, verbs: list, adjectives: list):
    with open("headlines.txt", "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                if word.istitle():
                    nouns.append(word)
                else:
                    if word.endswith("en") or word.endswith("t"):
                        verbs.append(word)
                    else:
                        adjectives.append(word)

fill_word_pool(nouns, verbs, adjectives)

def generate_sentence():
    structure = random.choice(sentence_structures)
    words = [random.choice(word_pools[pos]) for pos in structure]
    return " ".join(words)

for _ in range(3):
    print(generate_sentence())