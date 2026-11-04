"""Activity 1 - Change the input
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The young scientist is developing a new application."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*>+}
"""
parser = RegexpParser(grammar)
result = parser.parse(tagged_words)

print("POS Tagged Words:")
print(tagged_words)
print("\nChunk Structure:")
print(result)
print("\nRecognized Phrases:")
for subtree in result.subtrees():
    if subtree.label() in ("NP", "VP"):
        print(subtree.label(), ":", " ".join(word for word, tag in subtree.leaves()))
