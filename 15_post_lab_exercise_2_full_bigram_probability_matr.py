"""Post-Lab Exercise 2 - Full bigram probability matrix (dictionary of dictionaries)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
from collections import Counter, defaultdict
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

bigram_matrix = defaultdict(dict)
for w1 in vocab:
    for w2 in vocab:
        probability = (bigram_counts[(w1, w2)] + 1) / (unigram_counts[w1] + V)
        bigram_matrix[w1][w2] = probability

words = sorted(vocab)
print("BIGRAM PROBABILITY MATRIX")
print()
print(f"{'Word':<12}", end="")
for word in words:
    print(f"{word:<10}", end="")
print()
print("-" * (12 + 10 * len(words)))
for w1 in words:
    print(f"{w1:<12}", end="")
    for w2 in words:
        print(f"{bigram_matrix[w1][w2]:<10.4f}", end="")
    print()
