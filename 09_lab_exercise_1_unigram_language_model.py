"""Lab Exercise 1 - Unigram language model
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
from collections import Counter

ask = input("Do you have any corpus or not (Yes or NO)").strip().lower()
if (ask == 'yes'):
    corpus = input("Enter your corpus")
elif (ask == 'no'):
    corpus = """the quick brown fox jumps over the lazy dog
    the dog barks at the fox
    the quick fox runs away from the dog"""
    print("The Corpus Automaticallytaken is:\nthe quick brown fox jumps over the lazy dog the dog barks at the
        fox "
           "the quick fox runs away from the dog")
else:
    print("The process will stop if you do not select Yes or No")
    exit()

def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"[a-z']+", text)
    return tokens

tokens = tokenize(corpus)
unigram_counts = Counter(tokens)
print("Total tokens (N):", len(tokens))
print(f"{'word':<12}{'Count':<8}{'P(word)':<10}")
print("-"*30)
for word, count in unigram_counts.most_common():
    prob = count / len(tokens)
    print(f"{word:<12}{count:<8}{prob:<10.4f}")

def unigram_probability(word):
    return unigram_counts[word]/len(tokens)

test_word = input("Enter the Token in the corpus(Without spaces)")
print(f"\nP('{test_word}') = {unigram_probability(test_word):.4f}")
