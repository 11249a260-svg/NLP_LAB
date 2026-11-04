"""Lab Activity 1 - Environment setup and POS tagger (pos_tagger.py)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

print("\nPOS Tagged Sentence:")
for word, tag in tags:
    print(word, "->", tag)
