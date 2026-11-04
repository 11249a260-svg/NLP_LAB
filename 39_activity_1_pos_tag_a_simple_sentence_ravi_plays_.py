"""Activity 1 - POS tag a simple sentence: "Ravi plays cricket every evening."
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

sentence = "Ravi plays cricket every evening."

words = sentence.replace(".", "").split()

nouns = ["Ravi", "cricket", "evening"]
verbs = ["plays"]
adverbs = ["every"]

print("Sentence:", sentence)
print("Nouns:", [w for w in words if w in nouns])
print("Verbs:", [w for w in words if w in verbs])
print("Adverbs:", [w for w in words if w in adverbs])
