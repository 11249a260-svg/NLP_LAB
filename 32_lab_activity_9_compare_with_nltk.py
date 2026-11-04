"""Lab Activity 9 - Compare with NLTK
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import nltk
nltk.download('averaged_perceptron_tagger')

sentences = [
    "The big dog runs",
    "She reads a book",
]
for sentence in sentences:
    words = sentence.split()
    result = nltk.pos_tag(words)
    print("\nSentence:", sentence)
    print("NLTK:", result)
