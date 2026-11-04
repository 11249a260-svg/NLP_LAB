"""Activity 5 - Error analysis
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The students are working on projects."
tagged_words = pos_tag(word_tokenize(sentence))

# Original grammar
grammar1 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*>+}
    PP: {<IN><NP>}
"""
# Improved grammar
grammar2 = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*><VB.*>*}
    PP: {<IN><NP>}
"""
parser1 = RegexpParser(grammar1)
parser2 = RegexpParser(grammar2)

print("POS Tagged Words:")
print(tagged_words)
print("\nOriginal Chunk Tree:")
print(parser1.parse(tagged_words))
print("\nImproved Chunk Tree:")
print(parser2.parse(tagged_words))
