"""Activity 3 - Compare grammar rules (NP only vs NP + VP + PP)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The teacher explains the lesson in the classroom."
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

# Grammar 1: NP only
grammar1 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
# Grammar 2: NP + VP + PP
grammar2 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*>+}
    PP: {<IN><NP>}
"""
parser1 = RegexpParser(grammar1)
parser2 = RegexpParser(grammar2)
tree1 = parser1.parse(tagged_words)
tree2 = parser2.parse(tagged_words)

print("POS Tagged Words:")
print(tagged_words)
print("\nChunk Tree 1: NP Only")
print(tree1)
print("\nChunk Tree 2: NP + VP + PP")
print(tree2)
