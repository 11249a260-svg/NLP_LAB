"""Lab Activity 6 - Implement the Viterbi function
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

def viterbi(words, tags, trans, emit):
    V = [{}]
    BP = [{}]

     # First word
     for t in tags:
         V[0][t] = emit.get(t, {}).get(words[0], 0)
         BP[0][t] = None

     # Remaining words
     for i in range(1, len(words)):
         V.append({})
         BP.append({})
         for t in tags:
             V[i][t], BP[i][t] = max(
                 (V[i-1][p] * trans.get(p, {}).get(t, 0) *
                  emit.get(t, {}).get(words[i], 0), p)
                 for p in tags
             )

     # Backtracking
     last = max(V[-1], key=V[-1].get)
     path = [last]
     for i in range(len(words)-1, 0, -1):
         last = BP[i][last]
         path.append(last)
     return V, BP, path[::-1]

tags = ["DET", "NOUN", "VERB"]
trans = {
    "DET": {"NOUN": 2},
    "NOUN": {"VERB": 1}
}
emit = {
    "NOUN": {"dog": 1},
    "VERB": {"barks": 1}
}
words = ["The", "dog", "barks"]
V, BP, result = viterbi(words, tags, trans, emit)
print("V =", V)
print("BP =", BP)
print("Result =", result)
