"""Task 5 (program) - Rule-based stemmer using suffix stripping
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

def stem_word(word):
    if word.endswith("ization"):
        return word[:-7]
    elif word.endswith("iness"):
        return word[:-5]
    elif word.endswith("ness"):
        return word[:-4]
    elif word.endswith("ing"):
        return word[:-3]
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("ies"):
        return word[:-3]
    elif word.endswith("s") and len(word) > 1:
        return word[:-1]
    else:
        return word

words = ["Playing", "Played", "Plays", "Studies", "Happiness",
         "Unhappiness", "Nationalization", "Files", "Running"]
print("Word".ljust(20), "Stem")
print("-"*30)
for word in words:
    print(word.ljust(20), stem_word(word))
