import random

with open("headlines.txt", "r", encoding="utf-8") as file:
    nouns = []
    rest = []
    for line in file:
        for word in line.split():
            if word.istitle():
                nouns.append(word)
            else:
                rest.append(word)

n = 3
out = []

nouns_sample = random.sample(nouns, n)
verbs_sample = random.sample(rest, n)

for noun, verb in zip(nouns_sample, verbs_sample):
    out.append(f"{noun} {verb}")
    
output_text = " ".join(out)
print(output_text)