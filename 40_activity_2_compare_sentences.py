"""Activity 2 - Compare sentences
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]

for sentence in sentences:
    print("\nSentence:", sentence)

    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    print("Tagged words:", tagged_words)

    for word, tag in tagged_words:
        if tag in ("NN", "NNS", "NNP", "NNPS"):
            category = "Noun"
        elif tag.startswith("VB"):
            category = "Verb"
        elif tag.startswith("JJ"):
            category = "Adjective"
        elif tag.startswith("RB"):
            category = "Adverb"
        elif tag.startswith("PRP"):
            category = "Pronoun"
        elif tag in ("DT", "PDT", "WDT"):
            category = "Determiner"
        else:
            category = "Other"

        print(word, ":", category)
