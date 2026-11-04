"""Lab Activity 5 - Compute probability tables (transition and emission counts)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

from collections import defaultdict, Counter

corpus = [
    [("The","DET"), ("big","ADJ"), ("dog","NOUN"), ("runs","VERB")],
    [("She","PRON"), ("reads","VERB"), ("a","DET"), ("book","NOUN")],
]

transition_count = defaultdict(Counter)
emission_count = defaultdict(Counter)

for sentence in corpus:
    for i, (word, tag) in enumerate(sentence):
        emission_count[tag][word] += 1
        if i > 0:
            prev_tag = sentence[i-1][1]
            transition_count[prev_tag][tag] += 1

print("Transition Count:")
print(dict(transition_count))
print("\nEmission Count:")
print(dict(emission_count))
