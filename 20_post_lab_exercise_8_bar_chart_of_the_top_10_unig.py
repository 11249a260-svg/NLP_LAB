"""Post-Lab Exercise 8 - Bar chart of the top 10 unigrams (matplotlib)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

import re
from collections import Counter
import matplotlib.pyplot as plt

# Corpus
corpus = """the quick brown fox jumps over the lazy dog
the dog barks at the fox
the quick fox runs away from the dog"""
# Tokenization
def tokenize(text):
    text = text.lower()
    return re.findall(r"[a-z']+", text)

tokens = tokenize(corpus)
unigram_counts = Counter(tokens)

# Get top 10 unigrams
top_10 = unigram_counts.most_common(10)
words = [item[0] for item in top_10]
counts = [item[1] for item in top_10]

# Display frequency table
print("Top 10 Unigrams")
print("-" * 30)
print(f"{'Word':<15}{'Frequency':<10}")
print("-" * 30)
for word, count in top_10:
    print(f"{word:<15}{count:<10}")

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.title("Top 10 Unigram Frequency Distribution")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
