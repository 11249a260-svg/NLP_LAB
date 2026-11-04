"""Exercise 3 - Compare the tagger with NLTK's built-in pos_tag
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk.corpus import treebank
from nltk.tag import DefaultTagger, UnigramTagger
nltk.download(['treebank', 'punkt_tab', 'averaged_perceptron_tagger_eng'], quiet=True)

data = treebank.tagged_sents()
train, test = data[:int(len(data)*0.8)], data[int(len(data)*0.8):]
custom_tagger = UnigramTagger(train, backoff=DefaultTagger('NN'))

tokens = nltk.word_tokenize("The quick brown fox jumps over the lazy dog")
custom_tags = custom_tagger.tag(tokens)
nltk_tags = nltk.pos_tag(tokens)

print(f"Custom Accuracy: {custom_tagger.accuracy(test):.2%}\n")
print(f"{'Word':<10} | {'Custom':<10} | {'NLTK':<10}")
print("-" * 35)
for (w, c), (_, n) in zip(custom_tags, nltk_tags):
    print(f"{w:<10} | {c:<10} | {n:<10}")
