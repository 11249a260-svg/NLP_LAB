"""Exercise 3 - spaCy lemmatization vs NLTK WordNet Lemmatizer
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import spacy
import nltk
from nltk.stem import WordNetLemmatizer

# Download WordNet data
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize NLTK WordNet Lemmatizer
wnl = WordNetLemmatizer()

# Input paragraph
text = """
The children were playing in the gardens and running around the trees.
They enjoyed the beautiful flowers and ate delicious fruits.
The cats chased the mice while the dogs were barking loudly.
"""

# spaCy lemmatization
doc = nlp(text)
print("spaCy Lemmatization:")
for token in doc:
    if token.is_alpha:
        print(f"{token.text:15} -> {token.lemma_}")

# NLTK WordNet Lemmatization
print("\nNLTK WordNet Lemmatization:")
for word in text.split():
    word_clean = word.lower().strip(".,")
    if word_clean.isalpha():
        print(f"{word_clean:15} -> {wnl.lemmatize(word_clean)}")

# Comparison
print("\nComparison:")
for token in doc:
    word = token.text.lower().strip(".,")
    if word.isalpha():
        spacy_lemma = token.lemma_
        nltk_lemma = wnl.lemmatize(word)
        if spacy_lemma != nltk_lemma:
             print(f"{word:15} spaCy: {spacy_lemma:10} NLTK: {nltk_lemma}")
