"""Activity 1 - Identify noun phrases
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]

grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>+}
"""
parser = RegexpParser(grammar)

for sentence in sentences:
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    result = parser.parse(tagged_words)

    print("\nSentence:", sentence)
    print("Noun Phrases:")
    for subtree in result.subtrees(filter=lambda t: t.label() == 'NP'):
        print(" ".join(word for word, tag in subtree.leaves()))
