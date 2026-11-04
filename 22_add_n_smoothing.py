"""Add-N smoothing
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

def add_n_probability(previous_word, word, n):
    numerator = bigram_counts[(previous_word, word)] + n
    denominator = word_counts[previous_word] + n * V
    return numerator / denominator

print("Add-1:")
print("P(NLP | like) =", add_n_probability("Like", "nlp", 1))
print("P(love | like) =", add_n_probability("like", "love", 1))

print("\nAdd-0.5:")
print("P(NLP | like) =", add_n_probability("like", "nlp", 0.5))
print("P(love | like) =", add_n_probability("like", "love", 0.5))
