"""Chunking - shallow parsing with NP VP PP
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The children are playing in the garden."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

print("POS Tagged Words:")
print(tagged_words)

grammar = r"""
    NP: {<DT>?<JJ>*<NNS|NN|NNP>}
    VP: {<VBP|VBZ|VBD|VBG|VB>+}
    PP: {<IN><DT>?<NN|NNS>}
"""
parser = RegexpParser(grammar)
result = parser.parse(tagged_words)

print("\nShallow Parsing Result:")
print(result)
result.pretty_print()
