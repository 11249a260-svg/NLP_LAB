"""Activity 4 - Compare two chunk structures
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

phrases = [
    "a student",
    "the very intelligent student"
]

grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""
parser = RegexpParser(grammar)

for phrase in phrases:
    words = word_tokenize(phrase)
    tagged_words = pos_tag(words)
    result = parser.parse(tagged_words)

    print("\nPhrase:", phrase)
    print("POS Tags:", tagged_words)
    print("Chunk Structure:", result)
