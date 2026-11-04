"""Lab Activity 7 - Test on new sentences
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.tag import UnigramTagger

train = [
    [("The","DET"),("big","ADJ"),("dog","NOUN"),("runs","VERB")],
    [("She","PRON"),("reads","VERB"),("a","DET"),("book","NOUN")],
    [("He","PRON"),("eats","VERB"),("the","DET"),("red","ADJ"),("apple","NOUN")],
    [("I","PRON"),("like","VERB"),("a","DET"),("good","ADJ"),("car","NOUN")],
    [("They","PRON"),("play","VERB"),("the","DET"),("new","ADJ"),("game","NOUN")]
]

tagger = UnigramTagger(train)
tests = [
    "The big dog runs",
    "She reads a book"
]
for sentence in tests:
    print(sentence)
    print(tagger.tag(sentence.split()))
    print()
