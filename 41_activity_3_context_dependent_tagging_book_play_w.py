"""Activity 3 - Context-dependent tagging (book, play, watch)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "I read a book.",
    "Please book a ticket.",
    "Children play football.",
    "We watched a play."
]

for sentence in sentences:
    print("\nSentence:", sentence)
    tagged_words = pos_tag(word_tokenize(sentence))
    print(tagged_words)
