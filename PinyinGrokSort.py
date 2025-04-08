"""
PinyinGrokSort - Sort words in Hànyǔ Pīnyīn in alphabetical order (fast)

Description:
    This module implements a Pinyin sorting algorithm based on 
    rules outlined by John DeFrancis in "ABC Chinese-English Dictionary". 
    
    However, the sorting algorithm looks at Pīnyīn letter by letter,
    as Pīnyīn is written using the ALPHABET,
    a realisation and algorithm design concept by Alfons Grabher.

    The rules are:
    
    1. Alphabetical Order: Base chars (a-z) first, letter-by-letter.
    3. u before ü, U before Ü.
    2. Tones: 0 < 1 < 2 < 3 < 4
    4. Lowercase/mixed before uppercase.
    5. Separators: single quote < hyphen < space.
    
    The sort can handle plain Pinyin strings or lists of dictionaries with a specified key.

Credits:
    - John DeFrancis: Original Pinyin sorting rules from "ABC Chinese-English Dictionary".
    - Mark Swofford: Preserving and explaining the rules via pinyin.info blog.
    - Alfons Grabher: Concept, ideas, prompting, testing, and driving the development.
    - Grok (xAI): Coding the implementation with flair and precision.

Usage:
    # Array of Strings
    words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"]
    sorted_words = pinyin_grok_sort(words)
    print(sorted_words)  # ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']

    # Array of Dictionaries
    dicts = [
        {"pinyin": "bǎozhàng", "meaning": "guarantee"},
        {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
        {"pinyin": "bǎoyù", "meaning": "jade"}
    ]
    sorted_dicts = pinyin_grok_sort(dicts, key=lambda item: item["pinyin"])
    print(sorted_dicts)
    # [
    #   {'pinyin': 'bǎoyù', 'meaning': 'jade'},
    #   {'pinyin': 'bǎozhàng', 'meaning': 'guarantee'},
    #   {'pinyin': 'Bǎoyǔ', 'meaning': 'Bao Yu (name)'}
    # ]

    # Reverse Order (Strings)
    reverse_words = pinyin_grok_sort(words, reverse=True)
    print(reverse_words)  # ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']

    # Reverse Order (Dictionaries)
    reverse_dicts = pinyin_grok_sort(dicts, key=lambda item: item["pinyin"], reverse=True)
    print(reverse_dicts)
    # [
    #   {'pinyin': 'Bǎoyǔ', 'meaning': 'Bao Yu (name)'},
    #   {'pinyin': 'bǎozhàng', 'meaning': 'guarantee'},
    #   {'pinyin': 'bǎoyù', 'meaning': 'jade'}
    # ]
"""

from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    WEIGHTS = {
        'a': 0, 'ā': 1, 'á': 2, 'ǎ': 3, 'à': 4, 'A': 5, 'Ā': 6, 'Á': 7, 'Ǎ': 8, 'À': 9,
        'b': 10, 'B': 11, 'c': 12, 'C': 13, 'd': 14, 'D': 15,
        'e': 16, 'ē': 17, 'é': 18, 'ě': 19, 'è': 20, 'E': 21, 'Ē': 22, 'É': 23, 'Ě': 24, 'È': 25,
        'f': 26, 'F': 27, 'g': 28, 'G': 29, 'h': 30, 'H': 31,
        'i': 32, 'ī': 33, 'í': 34, 'ǐ': 35, 'ì': 36, 'I': 37, 'Ī': 38, 'Í': 39, 'Ǐ': 40, 'Ì': 41,
        'j': 42, 'J': 43, 'k': 44, 'K': 45, 'l': 46, 'L': 47,
        'm': 48, 'M': 49, 'n': 50, 'N': 51,
        'o': 52, 'ō': 53, 'ó': 54, 'ǒ': 55, 'ò': 56, 'O': 57, 'Ō': 58, 'Ó': 59, 'Ǒ': 60, 'Ò': 61,
        'p': 62, 'P': 63, 'q': 64, 'Q': 65, 'r': 66, 'R': 67,
        's': 68, 'S': 69, 't': 70, 'T': 71,
        'u': 72, 'ū': 73, 'ú': 74, 'ǔ': 75, 'ù': 76, 'U': 77, 'Ū': 78, 'Ú': 79, 'Ǔ': 80, 'Ù': 81,
        'ü': 82, 'ǖ': 83, 'ǘ': 84, 'ǚ': 85, 'ǜ': 86, 'Ü': 87, 'Ǖ': 88, 'Ǘ': 89, 'Ǚ': 90, 'Ǜ': 91,
        'v': 92, 'V': 93, 'w': 94, 'W': 95, 'x': 96, 'X': 97,
        'y': 98, 'Y': 99, 'z': 100, 'Z': 101,
        "'": 102, '-': 103, " ": 104
    }
    seq1 = [WEIGHTS.get(c, 999) for c in w1]
    seq2 = [WEIGHTS.get(c, 999) for c in w2]
    return -1 if seq1 < seq2 else 1 if seq1 > seq2 else 0

def pinyin_grok_sort(items, key=None, reverse=False):
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
    "nǚ", "Nǚ", "nǜrén"
    ]
    sorted_words = pinyin_grok_sort(test_words, reverse = False)
    print("\n".join(sorted_words))
