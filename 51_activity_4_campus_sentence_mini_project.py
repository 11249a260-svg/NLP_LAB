"""Activity 4 - Campus sentence mini-project
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The students attend lectures in the classroom.",
    "A professor explains the topic to the students.",
    "The library contains many useful books.",
    "Students are working on projects in the laboratory.",
    "The campus bus stops near the main gate."
]

grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<VB.*>+}
    PP: {<IN><NP>}
"""
parser = RegexpParser(grammar)

for sentence in sentences:
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    tree = parser.parse(tagged_words)

     print("\nSentence:", sentence)
     print("POS Tags:", tagged_words)
     print("Chunk Tree:", tree)
     print("Identified Phrases:")
     for subtree in tree.subtrees():
         if subtree.label() in ("NP", "VP", "PP"):
             phrase = " ".join(word for word, tag in subtree.leaves())
             print(subtree.label(), ":", phrase)
