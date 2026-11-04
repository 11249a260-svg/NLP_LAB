"""Exercise 2 - Analyzer extended for irregular plurals and irregular past tense
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

def morph_analyze(word):
    # Dictionary of irregular forms
    irregular = {
        # Irregular plurals
        "mice": ("mouse", "+PLURAL"),
        "geese": ("goose", "+PLURAL"),
        "children": ("child", "+PLURAL"),
        "men": ("man", "+PLURAL"),
        "women": ("woman", "+PLURAL"),
        "feet": ("foot", "+PLURAL"),
        "teeth": ("tooth", "+PLURAL"),
        # Irregular past tense
        "went": ("go", "+PAST"),
        "ate": ("eat", "+PAST"),
        "ran": ("run", "+PAST"),
        "came": ("come", "+PAST"),
        "saw": ("see", "+PAST"),
        "gave": ("give", "+PAST"),
    }

    # Check irregular forms first
    if word in irregular:
        root, tag = irregular[word]
        return f"{root}{tag}"

    # Regular suffix-stripping rules
    rules = [
        ('ies', 'y', '+PLURAL'),
        ('es', '', '+PLURAL'),
        ('s', '', '+PLURAL'),
        ('ing', '', '+PROG'),
        ('ed', '', '+PAST'),
    ]
    for suffix, replacement, tag in rules:
        if word.endswith(suffix):
            root = word[:-len(suffix)] + replacement
            return f"{root}{tag}"
    return f"{word}+ROOT"

# Test words
test_words = ['cats', 'boxes', 'flies', 'playing', 'jumped', 'book',
              'mice', 'geese', 'children', 'went', 'ate', 'ran']
for w in test_words:
    print(f"{w:10} -> {morph_analyze(w)}")
