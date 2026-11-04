"""Task 1 - Word analysis using stemming (Porter Stemmer)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ['Playing', 'Played', 'Plays', 'studies', 'happiness', 'unhappiness', 'nationalization', 'files',
    'running']
print(f"{'Word':15}{'Stem'}")
print('-'*25)
for w in words:
    print(f"{w:15}{ps.stem(w)}")
