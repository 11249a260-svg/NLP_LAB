"""Activity 3 - Annotate a sentence
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The young researcher develops an AI model."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

print("POS-Tagged Sequence:")
print(tagged_words)

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
parser = RegexpParser(grammar)
result = parser.parse(tagged_words)

print("\nBracketed Noun Phrases:")
print(result)
