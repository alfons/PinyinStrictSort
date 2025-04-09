"""
# PinyinAbcSort - Sort Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:

 This project implements sorting Pīnyīn words into alphabetical word order,
 based on the rules outlined by John DeFrancis in ABC Chinese-English
 Dictionary, Page xiii, Reader’s Guide, I. Arrangement of Entries.

 The sorting algorithm compares words letter by letter, not syllable by
 syllable. This approach reflects the fact that Hànyǔ Pīnyīn is written using
 the Latin alphabet — the key insight and algorithm design choice behind this
 implementation.

## The ordering rules are:

 1. Alphabetical order: Base characters (a–z), compared letter by letter
 2. u before ü, U before Ü
 3. Tones: 0 < 1 < 2 < 3 < 4
 4. Case: lowercase and mixed-case before uppercase
 5. Separators: apostrophe < hyphen < space

 Since no rules for numbers 0–9 were given, they were added first. All other
 characters are appended according to their Unicode value.

## Credits:

 - John DeFrancis: Original Pīnyīn alphabetical word order, in passionate
   acknowledgment of the advocates of writing reform Lù Zhuāngzhāng (陆璋章,
   1854–1928), Lǔ Xùn (鲁迅, 1881–1936), Máo Dùn (Shěn Yànbīng, 茅盾, 沈雁冰,
   1896–1981), Wáng Lì (王力, 1900–1988) and Lù Shūxiāng (吕叔湘, 1904–1998),
   and Zhōu Yǒuguāng (周有光, 1905–2017).
 - Mark Swofford of Banqiao, Taiwan: summarised the rules on the internet, and
   pointed out where to find them.
 - Alfons Grabher: Idea, concept, prompting, testing, and driving the
   development of pinyinAbcSort.
 - Grok (xAI), ChatGPT 4o: Coding the implementation with flair and precision.

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
sorted_dicts = pinyin_abc_sort(dicts, key=lambda item: item["pinyin"])
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
reverse_dicts = pinyin_abc_sort(dicts, key=lambda item: item["pinyin"], reverse=True)
print(reverse_dicts)
# [
#   {'pinyin': 'Bǎoyǔ', 'meaning': 'Bao Yu (name)'},
#   {'pinyin': 'bǎozhàng', 'meaning': 'guarantee'},
#   {'pinyin': 'bǎoyù', 'meaning': 'jade'}
# ]
```

## History

This was much more difficult than expected, and took much, much longer 
than expected. But in the end it looks so simple, almost laughably simple, 
and flies like a SpaceX starship. 🚀
"""

from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    ordered_chars = (
        "0123456789aāáǎàAĀÁǍÀbBcCdDeēéěèEĒÉĚÈfFgGhHiīíǐìIĪÍǏÌ"
        "jJkKlLmMnNoōóǒòOŌÓǑÒpPqQrRsStTuūúǔùUŪÚǓÙ"
        "üǖǘǚǜÜǕǗǙǛvVwWxXyYzZ'- "
    )
    WEIGHTS = {char: i for i, char in enumerate(ordered_chars)}
    OFFSET = len(ordered_chars)

    seq1 = [WEIGHTS.get(c, ord(c) + OFFSET) for c in w1]
    seq2 = [WEIGHTS.get(c, ord(c) + OFFSET) for c in w2]

    return (seq1 > seq2) - (seq1 < seq2)

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
    "bǎOYÙ", "Bǎoyù", "bĀozì",
    # Edge chars (start/end of alphabet)
    "ǎ", "à", "zǐ", "Zǐ",
    # Separator-heavy
    "bǎo an-xiǎo", "bǎo'an xiǎo",
    # Tricky ü with tones
    "nǚ", "Nǚ", "nǜrén",
    # In ABC, hyphens and spaces don’t affect the sort order 
    "lìgōng","lǐ-gōng"
    ]
    sorted_words = pinyin_abc_sort(test_words, reverse = False)
    print("\n".join(sorted_words))
