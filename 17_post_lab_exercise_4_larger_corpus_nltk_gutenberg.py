"""Post-Lab Exercise 4 - Larger corpus (NLTK Gutenberg: austen-emma.txt)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
import nltk
from collections import Counter

# Download Gutenberg corpus
nltk.download("gutenberg")
from nltk.corpus import gutenberg

# Load a larger corpus
text = gutenberg.raw("austen-emma.txt")

# Tokenization
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)

tokens = tokenize(text)
print("Total tokens:", len(tokens))

# 1. UNIGRAM MODEL
unigram_counts = Counter(tokens)
print("\nTOP 10 UNIGRAMS")
print(f"{'Word':<15}{'Count':<10}{'Probability':<12}")
print("-" * 37)
N = len(tokens)
for word, count in unigram_counts.most_common(10):
    probability = count / N
    print(f"{word:<15}{count:<10}{probability:<12.6f}")

# 2. BIGRAM MODEL
bigram_counts = Counter()
for i in range(len(tokens) - 1):
    bigram = (tokens[i], tokens[i + 1])
    bigram_counts[bigram] += 1
print("\nTOP 10 BIGRAMS")
print(f"{'Bigram':<35}{'Count':<10}")
print("-" * 45)
for bigram, count in bigram_counts.most_common(10):
    print(f"{str(bigram):<35}{count:<10}")

# 3. TRIGRAM MODEL
trigram_counts = Counter()
for i in range(len(tokens) - 2):
    trigram = (tokens[i], tokens[i + 1], tokens[i + 2])
    trigram_counts[trigram] += 1
print("\nTOP 10 TRIGRAMS")
print(f"{'Trigram':<45}{'Count':<10}")
print("-" * 55)
for trigram, count in trigram_counts.most_common(10):
    print(f"{str(trigram):<45}{count:<10}")

# TEST WORD PROBABILITY
test_word = "emma"
probability = unigram_counts[test_word] / N
print("\nTest Word:", test_word)
print(f"P('{test_word}') = {probability:.6f}")
