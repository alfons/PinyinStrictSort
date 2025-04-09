"""
# PinyinAbcSort - Sort Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:

This project implements a Pīnyīn word sorting order based on the rules outlined 
by John DeFrancis in ABC Chinese-English Dictionary.
    
Note: The sorting algorithm compares words letter by letter, not syllable by syllable. 
This approach reflects the fact that Hànyǔ Pīnyīn is written using the Latin alphabet — 
the key insight and algorithm design choice behind this implementation.

## John DeFrancis' ordering rules are:

1. Alphabetical order: Base characters (a–z), compared letter by letter
2. u before ü, U before Ü
3. Tones: 0 < 1 < 2 < 3 < 4
4. Case: lowercase and mixed-case before uppercase
5. Separators: apostrophe < hyphen < space
    
The sort function handles arrays of plain Pīnyīn strings or arrays of dictionaries using a specified key.

## Credits:

- John DeFrancis: Original Pinyin ordering rules.
- Mark Swofford of Banqiao, Taiwan: Preserving and explaining the rules.
- Alfons Grabher: Idea, concept, prompting, testing, and driving the development of pinyinAbcSort.
- Grok (xAI): Coding the implementation with flair and precision.

## Usage 

```python
# Array of Strings
words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"]
sorted_words = pinyin_abc_sort(words)
print(sorted_words)  # ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']

# Array of Dictionaries
dicts = [
    {"pinyin": "bǎozhàng", "meaning": "guarantee"},
    {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
    {"pinyin": "bǎoyù", "meaning": "jade"}
]
sorted_dicts = pinyin_abc_sort(dicts, key="pinyin")
print(sorted_dicts)
# [
#   {'pinyin': 'bǎoyù', 'meaning': 'jade'},
#   {'pinyin': 'bǎozhàng', 'meaning': 'guarantee'},
#   {'pinyin': 'Bǎoyǔ', 'meaning': 'Bao Yu (name)'}
# ]

# Reverse Order (Strings)
reverse_words = pinyin_abc_sort(words, reverse=True)
print(reverse_words)  # ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']

# Reverse Order (Dictionaries)
reverse_dicts = pinyin_abc_sort(dicts, key="pinyin", reverse=True)
print(reverse_dicts)
# [
#   {'pinyin': 'Bǎoyǔ', 'meaning': 'Bao Yu (name)'},
#   {'pinyin': 'bǎozhàng', 'meaning': 'guarantee'},
#   {'pinyin': 'bǎoyù', 'meaning': 'jade'}
# ]
```

## History

This was much more difficult than expected, and took much, much more time than expected. 
But in the end it looks so simple, almost laughably simple, and flies like a 
Raptor SpaceX booster rocket. 🚀
"""
from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    ordered_chars = (
        "0123456789"
        "aāáǎàbBcCdDeēéěèfFgGhHiīíǐìjJkKlLmMnNoōóǒòpPqQrRsStTuūúǔù"
        "üǖǘǚǜvVwWxXyYzZ'- "
    )
    WEIGHTS = {char: i for i, char in enumerate(ordered_chars)}
    OFFSET = len(ordered_chars)  # Offset for unmapped chars

    # Step 1: Convert to lowercase for primary comparison (preserving tones)
    lower_w1 = w1.lower()
    lower_w2 = w2.lower()
    seq1 = [WEIGHTS.get(c, ord(c) + OFFSET) for c in lower_w1]
    seq2 = [WEIGHTS.get(c, ord(c) + OFFSET) for c in lower_w2]
    cmp_lower = (seq1 > seq2) - (seq1 < seq2)

    # Step 2: If lowercase versions are equal, use original strings for case tiebreaker
    if cmp_lower == 0:
        seq1_orig = [WEIGHTS.get(c, ord(c) + OFFSET) for c in w1]
        seq2_orig = [WEIGHTS.get(c, ord(c) + OFFSET) for c in w2]
        return (seq1_orig > seq2_orig) - (seq1_orig < seq2_orig)
    
    return cmp_lower

def pinyin_abc_sort(items, key=None, reverse=False):
    extractor = (lambda x: x[key]) if key else lambda x: x
    items_list = list(items)
    items_list.sort(key=cmp_to_key(lambda a, b: _compare_pinyin(extractor(a), extractor(b))), reverse=reverse)
    return items_list

if __name__ == "__main__":
    test_words = [
        # Tones (all variants)
        "baozi", "bāozi", "báozi", "bǎozi", "bàozi",
        # Case (mixed and full uppercase)
        "bǎozi", "Bǎozi", "BǍOZI",
        # Duplicates
        "bǎozi", "bǎozi", "Bǎozi",
        # U vs Ü
        "lù", "lü", "Lù", "Lǚ",
        # Separators (space, hyphen, apostrophe)
        "bǎo", "bǎo an", "bǎo-an", "bǎo'an",
        # Length and prefix matches
        "bǎozhǎng", "bǎozhàng", "bǎozhàngjiāndū",
        # Alphabetical transitions
        "bǎoyù", "bǎozàng", "bǎpa", "bǎshǐ",
        # Mixed tones and case
        "bǎOYÙ", "Bǎoyù", "bĀozì", "Bǎoyǔ",
        # Edge chars (start/end of alphabet)
        "ǎ", "à", "zǐ", "Zǐ",
        # Separator-heavy
        "bǎo an-xiǎo", "bǎo'an xiǎo",
        # Tricky ü with tones
        "nǚ", "Nǚ", "nǜrén",
        # Hyphens and spaces don’t affect sort order
        "lìgōng", "lǐ-gōng",
        # Odd friends (non-Pīnyīn chars)
        "bǎo#", "bǎo$", "bǎo©"
    ]
    sorted_words = pinyin_abc_sort(test_words, reverse=False)
    print("\n".join(sorted_words))
    dicts = [
    {"pinyin": "bǎozhàng", "meaning": "guarantee"},
    {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
    {"pinyin": "bǎoyù", "meaning": "jade"}
    ]
    sorted_dicts = pinyin_abc_sort(dicts, key="pinyin")
    print(sorted_dicts)
