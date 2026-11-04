"""Lab Activity - Perplexity comparison (unigram, bigram, trigram)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

# Lab Activity: Perplexity Comparison

def perplexity(prob, n):
    return prob ** (-1 / n) if prob > 0 else float("inf")

test_sentence = "the fox runs away"
n = len(test_sentence.split())

uni_p = 0.0009
bi_p = 0.00021
tri_p = 0.00007

print("Test Sentence:", test_sentence)
print("Number of words:", n)

print("\nSentence Probabilities:")
print("Unigram:", uni_p)
print("Bigram :", bi_p)
print("Trigram:", tri_p)

print("\nPerplexity:")
print("Unigram Perplexity:", round(perplexity(uni_p, n), 2))
print("Bigram Perplexity :", round(perplexity(bi_p, n), 2))
print("Trigram Perplexity:", round(perplexity(tri_p, n), 2))
