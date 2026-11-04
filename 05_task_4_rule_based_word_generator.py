"""Task 4 - Rule-based word generator
Extracted from the uploaded NLP lab record. Review against the PDF before submission."""

def morph_generate(root, tag):
    if tag == '+PLURAL':
        if root.endswith('y') and root[-2] not in 'aeiou':
            return root[:-1] + 'ies'
        elif root.endswith(('s', 'x', 'ch', 'sh')):
            return root + 'es'
        else:
            return root + 's'
    elif tag == '+PROG':
        return root[:-1] + 'ing' if root.endswith('e') else root + 'ing'
    elif tag == '+PAST':
        return root + 'ed'
    return root

pairs = [('cat', '+PLURAL'), ('fly', '+PLURAL'), ('box', '+PLURAL'),
         ('play', '+PROG'), ('jump', '+PAST')]
for root, tag in pairs:
    print(f"{root} {tag:10} -> {morph_generate(root, tag)}")
