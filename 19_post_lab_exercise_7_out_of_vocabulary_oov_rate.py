"""Post-Lab Exercise 7 - Out-of-vocabulary (OOV) rate
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re

# Training corpus
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
# Tokenization function
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)

# Create training vocabulary
training_tokens = tokenize(corpus)
vocabulary = set(training_tokens)
print("Training Vocabulary:")
print(sorted(vocabulary))
print("\nVocabulary Size:", len(vocabulary))

# OOV rate function
def oov_rate(test_sentence):
    test_tokens = tokenize(test_sentence)
    if len(test_tokens) == 0:
        return 0
    oov_words = [word for word in test_tokens if word not in vocabulary]
    rate = len(oov_words) / len(test_tokens)
    return rate, oov_words

# Test sentence
test_sentence = "the fox flies over the mountain"
rate, oov_words = oov_rate(test_sentence)
print("\nTest Sentence:")
print(test_sentence)
print("\nOOV Words:")
print(oov_words)
print("\nTotal Test Words:", len(tokenize(test_sentence)))
print("Number of OOV Words:", len(oov_words))
print(f"OOV Rate: {rate:.4f}")
print(f"OOV Rate (%): {rate * 100:.2f}%")
