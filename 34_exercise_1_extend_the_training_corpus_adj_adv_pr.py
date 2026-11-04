"""Exercise 1 - Extend the training corpus (ADJ, ADV, PRON)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.tag import UnigramTagger

train = [
    [("The","DET"), ("small","ADJ"), ("boy","NOUN"), ("runs","VERB"), ("quickly","ADV")],
    [("She","PRON"), ("reads","VERB"), ("a","DET"), ("good","ADJ"), ("book","NOUN")],
    [("He","PRON"), ("speaks","VERB"), ("slowly","ADV")],
    [("The","DET"), ("beautiful","ADJ"), ("girl","NOUN"), ("sings","VERB")],
    [("They","PRON"), ("play","VERB"), ("very","ADV"), ("well","ADV")],
    [("I","PRON"), ("like","VERB"), ("fresh","ADJ"), ("food","NOUN")]
]
tagger = UnigramTagger(train)
sentence = "She sings beautifully"
print(tagger.tag(sentence.split()))
