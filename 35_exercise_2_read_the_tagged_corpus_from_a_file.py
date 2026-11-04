"""Exercise 2 - Read the tagged corpus from a file
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.tag import UnigramTagger

corpus = []
with open("corpus.txt", "r") as file:
    for line in file:
        sentence = []
        for item in line.split():
            word, tag = item.rsplit("/", 1)
            sentence.append((word, tag))
        corpus.append(sentence)

tagger = UnigramTagger(corpus)
sentence = input("Enter sentence: ")
print(tagger.tag(sentence.split()))
