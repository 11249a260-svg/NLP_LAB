"""Task 3 - Rule-based morphological analyzer
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

def morph_analyze(word):
    rules = [
        ('ies', 'y', '+PLURAL'),
        ('es', '', '+PLURAL'),
        ('s', '', '+PLURAL'),
        ('ing', '', '+PROG'),
        ('ed', '', '+PAST'),
    ]
    for suffex, replacement, tag in rules:
        if word.endswith(suffex):
            root = word[:-len(suffex)] + replacement
            return f"{root}{tag}"
    return f"{word}+ROOT"

test_words = ['cats', 'boxes', 'files', 'playing', 'jumped', 'book']
for w in test_words:
    print(f"{w:10} -> {morph_analyze(w)}")
