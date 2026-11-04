"""Activity 2 - Extend the noun phrase rule (possessive determiners and plural nouns)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The students read their textbooks."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
"""
parser = RegexpParser(grammar)
result = parser.parse(tagged_words)

print("POS Tagged Words:")
print(tagged_words)
print("\nUpdated Grammar:")
print(grammar)
print("\nChunk Structure:")
print(result)
print("\nIdentified Noun Phrases:")
for subtree in result.subtrees(filter=lambda t: t.label() == "NP"):
    print(" ".join(word for word, tag in subtree.leaves()))
