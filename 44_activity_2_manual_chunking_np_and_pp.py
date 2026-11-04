"""Activity 2 - Manual chunking (NP and PP)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The teacher explains the lesson in the classroom."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
    PP: {<IN><NP>}
"""
parser = RegexpParser(grammar)
result = parser.parse(tagged_words)

print("POS Tagged Words:")
print(tagged_words)

print("\nIdentified Phrases:")
for subtree in result.subtrees():
    if subtree.label() in ("NP", "PP"):
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(subtree.label(), ":", phrase)
