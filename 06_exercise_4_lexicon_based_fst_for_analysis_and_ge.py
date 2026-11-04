"""Exercise 4 - Lexicon-based FST for analysis and generation (15 nouns and verbs)
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

# Lexicon-based FST
lexicon = {
    # Nouns
    "cat":   {"type": "NOUN", "singular": "cat",   "plural": "cats"},
    "dog":   {"type": "NOUN", "singular": "dog",   "plural": "dogs"},
    "child": {"type": "NOUN", "singular": "child", "plural": "children"},
    "mouse": {"type": "NOUN", "singular": "mouse", "plural": "mice"},
    "book": {"type": "NOUN", "singular": "book", "plural": "books"},
    "city": {"type": "NOUN", "singular": "city", "plural": "cities"},
    "box":   {"type": "NOUN", "singular": "box",   "plural": "boxes"},
    "man":   {"type": "NOUN", "singular": "man",   "plural": "men"},
    # Verbs
    "play": {"type": "VERB", "base": "play", "past": "played", "progressive": "playing"},
    "walk": {"type": "VERB", "base": "walk", "past": "walked", "progressive": "walking"},
    "run":   {"type": "VERB", "base": "run",   "past": "ran",    "progressive": "running"},
    "eat":   {"type": "VERB", "base": "eat",   "past": "ate",    "progressive": "eating"},
    "go":    {"type": "VERB", "base": "go",    "past": "went",   "progressive": "going"},
    "see":   {"type": "VERB", "base": "see",   "past": "saw",    "progressive": "seeing"},
    "write": {"type": "VERB", "base": "write", "past": "wrote", "progressive": "writing"}
}

# Analysis: word -> lexical features
def analyze(word):
    for root, data in lexicon.items():
        if data["type"] == "NOUN":
            if word == data["singular"]:
                return f"{root}+NOUN+SINGULAR"
            if word == data["plural"]:
                return f"{root}+NOUN+PLURAL"
        elif data["type"] == "VERB":
            if word == data["base"]:
                return f"{root}+VERB+BASE"
            if word == data["past"]:
                return f"{root}+VERB+PAST"
            if word == data["progressive"]:
                return f"{root}+VERB+PROG"
    return "Unknown"

# Generation: lexical features -> word
def generate(root, feature):
    if root not in lexicon:
        return "Unknown"
    data = lexicon[root]
    if data["type"] == "NOUN":
        if feature == "+SINGULAR":
            return data["singular"]
        if feature == "+PLURAL":
            return data["plural"]
    elif data["type"] == "VERB":
        if feature == "+BASE":
            return data["base"]
        if feature == "+PAST":
            return data["past"]
        if feature == "+PROG":
            return data["progressive"]
    return "Unknown"

# Testing Analysis
print("Analysis:")
words = ["cats", "children", "mice", "boxes", "ran", "playing", "went", "writing"]
for word in words:
    print(f"{word:12} -> {analyze(word)}")

# Testing Generation
print("\nGeneration:")
tests = [("cat", "+PLURAL"), ("child", "+PLURAL"), ("run", "+PAST"),
         ("eat", "+PROG"), ("write", "+PAST")]
for root, feature in tests:
    print(f"{root} {feature} -> {generate(root, feature)}")
