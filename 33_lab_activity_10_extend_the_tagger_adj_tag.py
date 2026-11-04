"""Lab Activity 10 - Extend the tagger (ADJ tag)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.tag import UnigramTagger

train = [
    [("The", "DET"), ("big", "ADJ"), ("dog", "NOUN")],
    [("A", "DET"), ("small", "ADJ"), ("cat", "NOUN")],
    [("She", "PRON"), ("likes", "VERB"), ("red", "ADJ"), ("flowers", "NOUN")]
]
tagger = UnigramTagger(train)
sentence = "The small dog"
result = tagger.tag(sentence.split())
print("POS Tags:")
print(result)
