"""Post-Lab Exercise 5 - Bigram vs trigram text generation
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
import random
from collections import defaultdict, Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z']+", sentence)

sentences = [tokenize(s) for s in corpus.strip().split("\n")]

# BIGRAM MODEL
bigram_model = defaultdict(Counter)
for sent in sentences:
    tokens = ["<s>"] + sent + ["</s>"]
    for i in range(len(tokens) - 1):
        bigram_model[tokens[i]][tokens[i + 1]] += 1

# TRIGRAM MODEL
trigram_model = defaultdict(Counter)
for sent in sentences:
    tokens = ["<s>", "<s>"] + sent + ["</s>"]
    for i in range(len(tokens) - 2):
        context = (tokens[i], tokens[i + 1])
        next_word = tokens[i + 2]
        trigram_model[context][next_word] += 1

# BIGRAM GENERATION
def generate_bigram(max_len=15):
    word = "<s>"
    result = []
    for _ in range(max_len):
        next_words = bigram_model[word]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        word = random.choices(words, weights=counts, k=1)[0]
        if word == "</s>":
            break
        result.append(word)
    return " ".join(result)

# TRIGRAM GENERATION
def generate_trigram(max_len=15):
    w1 = "<s>"
    w2 = "<s>"
    result = []
    for _ in range(max_len):
        next_words = trigram_model[(w1, w2)]
        if not next_words:
            break
        words, counts = zip(*next_words.items())
        w3 = random.choices(words, weights=counts, k=1)[0]
        if w3 == "</s>":
            break
        result.append(w3)
        w1 = w2
        w2 = w3
    return " ".join(result)

# GENERATE SENTENCES
random.seed(42)
print("BIGRAM GENERATED SENTENCES")
print("--------------------------")
for i in range(3):
    print(f"Sentence {i + 1}: {generate_bigram()}")

print("\nTRIGRAM GENERATED SENTENCES")
print("----------------------------")
for i in range(3):
    print(f"Sentence {i + 1}: {generate_trigram()}")
