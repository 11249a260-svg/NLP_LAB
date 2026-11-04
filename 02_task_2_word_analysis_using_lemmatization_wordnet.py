"""Task 2 - Word analysis using lemmatization (WordNet Lemmatizer)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
nltk.download('WordNet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ['playing', 'played', 'plays', 'studies', 'better', 'geese']
print(f"{'Word':12}{'Lemma (verb)':15}{'lemma (noun)'}")
for w in words:
    v = lemmatizer.lemmatize(w, pos='v')
    n = lemmatizer.lemmatize(w, pos='n')
    print(f"{w:12}{v:15}{n}")
