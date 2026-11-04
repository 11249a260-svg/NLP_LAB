"""Backoff smoothing
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

from collections import Counter

corpus = [
    "I like NLP",
    "I like Python",
    "I love NLP",
    "I love Python"
]
sentences = [sentence.lower().split() for sentence in corpus]
unigrams = Counter()
bigrams = Counter()
trigrams = Counter()

for words in sentences:
    for word in words:
        unigrams[word] += 1
    for i in range(len(words) - 1):
        bigrams[(words[i], words[i + 1])] += 1
    for i in range(len(words) - 2):
        trigrams[(words[i], words[i + 1], words[i + 2])] += 1

total_words = sum(unigrams.values())

def unigram_probability(word):
    return unigrams[word] / total_words

def bigram_probability(previous, word):
    if bigrams[previous, word] == 0:
        return 0
    return bigrams[previous, word] / unigrams[previous]

def trigram_probability(w1, w2, word):
    if trigrams[w1, w2, word] == 0:
        return 0
    return trigrams[w1, w2, word] / bigrams[w1, w2]

def backoff_probability(w1, w2, word):
    # 1. Try trigram
    if trigrams[(w1, w2, word)] > 0:
        return trigram_probability(w1, w2, word)
    # 2. Otherwise try bigram
    elif bigrams[(w2, word)] > 0:
        return bigram_probability(w2, word)
    # 3. Otherwise use unigram
    else:
        return unigram_probability(word)

print("P(Python | I, like) =", backoff_probability("i", "like", "python"))
print("P(NLP | I, love) =", backoff_probability("i", "love", "nlp"))
