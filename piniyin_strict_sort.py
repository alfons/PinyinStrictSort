"""Strict alphabetical sorting for Hànyǔ Pīnyīn strings, or dictionaries, letter by letter, 
treating tone marks as integral to letters (e.g., a < ā < á < ǎ < à). 
See https://github.com/alfons/PinyinStrictSort for details.
"""
from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    """Compare two Pīnyīn strings alphabetically."""
    ordered_chars = "0123456789aāáǎàbcdeēéěèfghiīíǐìjklmnoōóǒòpqrsstuūúǔùüǖǘǚǜvwxyz'- "
    weights = {char: i for i, char in enumerate(ordered_chars)}
    offset = len(ordered_chars)

    lower_w1, lower_w2 = w1.lower(), w2.lower()
    seq1 = [weights.get(c, ord(c) + offset) for c in lower_w1]
    seq2 = [weights.get(c, ord(c) + offset) for c in lower_w2]
    cmp_lower = (seq1 > seq2) - (seq1 < seq2)

    if cmp_lower == 0:
        seq1_orig = [weights.get(c, ord(c) + offset) for c in w1]
        seq2_orig = [weights.get(c, ord(c) + offset) for c in w2]
        return (seq1_orig > seq2_orig) - (seq1_orig < seq2_orig)
    return cmp_lower

def pinyin_strict_sort(items, key=None, reverse=False):
    """Sort Pīnyīn strings or dictionaries alphabetically."""
    extractor = (lambda x: x[key]) if key else lambda x: x
    items_list = list(items)
    items_list.sort(key=cmp_to_key(lambda a, b: _compare_pinyin(extractor(a), extractor(b))), reverse=reverse)
    return items_list


# Sort strings
# words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"]
# print(pinyin_strict_sort(words))  # ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']

# Sort dictionaries
# dicts = [
#     {"pinyin": "bǎozhàng", "meaning": "guarantee"},
#     {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
#     {"pinyin": "bǎoyù", "meaning": "jade"}
# ]
# print(pinyin_strict_sort(dicts, key="pinyin"))

# Reverse order
# print(pinyin_strict_sort(words, reverse=True))  # ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']
