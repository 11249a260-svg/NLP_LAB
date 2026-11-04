"""Lab Activity 8 - Effect of smoothing
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

from collections import Counter

tags = ["DET", "NOUN", "VERB"]
initial_count = {"DET": 2, "NOUN": 0, "VERB": 0}
transition_count = {
    "DET": {"NOUN": 2},
    "NOUN": {"VERB": 1},
    "VERB": {}
}
emission_count = {
    "DET": {"The": 2},
    "NOUN": {"dog": 1},
    "VERB": {"runs": 1}
}
initial_prob = {
    t: initial_count[t] / sum(initial_count.values())
    for t in tags
}

def emission_prob(tag, word):
    return emission_count.get(tag, {}).get(word, 0)

def transition_prob(prev, curr):
    total = sum(transition_count.get(prev, {}).values())
    if total == 0:
        return 0
    return transition_count[prev].get(curr, 0) / total

words = ["The", "cat", "runs"]
for word in words:
    print(word)
    for tag in tags:
        print(tag, emission_prob(tag, word))
