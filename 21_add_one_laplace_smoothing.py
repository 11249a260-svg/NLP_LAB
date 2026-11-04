"""Add-One Laplace smoothing
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

from collections import Counter

corpus = [
    "I Like NLP",
    "I Like Python"
    "I Love NLP"
]
bigrams = []
for sentence in corpus:
    words = sentence.lower().split()
    for i in range(len(words)-1):
        bigrams.append((words[i], words[i+1]))
bigram_counts = Counter(bigrams)

word_counts = Counter()
for sentence in corpus:
    words = sentence.lower().split()
    for word in words[:-1]:
        word_counts[word] += 1

vocabulary = set()
for sentence in corpus:
    vocabulary.update(sentence.lower().split())
V = len(vocabulary)

def add_one_probability(previous_word, word):
    numerator = bigram_counts[(previous_word, word)] + 1
    denominator = word_counts[previous_word] + V
    return numerator / denominator

print("P(NLP | like) =", add_one_probability("Like", "nlp"))
print("P(love | like) =", add_one_probability("like", "love"))
