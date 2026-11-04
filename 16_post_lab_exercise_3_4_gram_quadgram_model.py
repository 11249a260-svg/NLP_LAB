"""Post-Lab Exercise 3 - 4-gram (quadgram) model
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
from collections import Counter
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
def tokenize(sentence):
    sentence = sentence.lower()
    return ["<s>", "<s>", "<s>"] + re.findall(r"[a-z']+", sentence) + ["</s>"]

sentences = [tokenize(s) for s in corpus.strip().split("\n")]
trigram_counts = Counter()
quadgram_counts = Counter()
vocab = set()
for sent in sentences:
    vocab.update(sent)
    for i in range(len(sent) - 3):
        trigram_counts[(sent[i], sent[i + 1], sent[i + 2])] += 1
        quadgram_counts[(sent[i], sent[i + 1], sent[i + 2], sent[i + 3])] += 1
V = len(vocab)

def quadgram_prob(w1, w2, w3, w4, smoothing=True):
    if smoothing:
        numerator = quadgram_counts[(w1, w2, w3, w4)] + 1
        denominator = trigram_counts[(w1, w2, w3)] + V
        return numerator / denominator
    denominator = trigram_counts[(w1, w2, w3)]
    if denominator:
        return quadgram_counts[(w1, w2, w3, w4)] / denominator
    return 0

print(f"{'Quadgram':<45}{'Count':<8}{'P(w4|w1,w2,w3)':<18}")
print("-" * 71)
for quadgram, count in quadgram_counts.most_common(10):
    probability = quadgram_prob(*quadgram)
    print(f"{quadgram!s:<45}{count:<8}{probability:<18.4f}")

def sentence_probability(sentence):
    tokens = tokenize(sentence)
    probability = 1.0
    for i in range(len(tokens) - 3):
        probability *= quadgram_prob(tokens[i], tokens[i + 1], tokens[i + 2], tokens[i + 3])
    return probability

test = "the quick brown fox"
print(f"\nP(\"{test}\") = {sentence_probability(test):.10f}")
