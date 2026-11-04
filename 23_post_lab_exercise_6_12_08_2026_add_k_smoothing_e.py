"""Post-Lab Exercise 6 (12-08-2026) - Add-k smoothing: effect of varying k on sentence probability
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()
for sent in sentences:
    unigram_counts.update(sent[:-1])
    vocab.update(sent)
    for i in range(len(sent) - 1):
        bigram_counts[(sent[i], sent[i + 1])] += 1
V = len(vocab)

# Add-k smoothing
def bigram_probability(w1, w2, k):
    numerator = bigram_counts[(w1, w2)] + k
    denominator = unigram_counts[w1] + (k * V)
    if denominator == 0:
        return 0
    return numerator / denominator

# Sentence probability
def sentence_probability(sentence, k):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 1):
        probability *= bigram_probability(tokens[i], tokens[i + 1], k)
    return probability

test_sentence = "the fox runs away"
print("Test Sentence:", test_sentence)
print("Vocabulary Size:", V)
print("\nAdd-k Smoothing Results")
print("-" * 45)
print(f"{'k':<10}{'Sentence Probability':<25}")
print("-" * 45)
for k in [0.1, 0.5, 1.0, 2.0]:
    probability = sentence_probability(test_sentence, k)
    print(f"{k:<10}{probability:<25.10f}")
