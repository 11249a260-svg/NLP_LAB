"""Building POS tagger - basic POS tagging
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
# Download resources (run once; internet may be required)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The intelligent student reads a book."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

print("Word\tPOS Tag")
print("-" * 25)
for word, tag in tagged_words:
    print(f"{word}\t{tag}")
