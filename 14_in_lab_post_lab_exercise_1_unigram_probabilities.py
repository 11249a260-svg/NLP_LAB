"""In-Lab / Post-Lab Exercise 1 - Unigram probabilities using NLTK FreqDist
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
import nltk
from nltk.probability import FreqDist
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"[a-z']+", text)
    return tokens

tokens = tokenize(corpus)
freq_dist = FreqDist(tokens)
N = len(tokens)

print("Total tokens (N):", N)
print(f"{'Word':<12}{'Count':<8}{'P(word)':<10}")
print("-" * 30)
for word, count in freq_dist.most_common():
    probability = count / N
    print(f"{word:<12}{count:<8}{probability:<10.4f}")

test_word = "fox"
probability = freq_dist[test_word] / N
print(f"\nP('{test_word}') = {probability:.4f}")
