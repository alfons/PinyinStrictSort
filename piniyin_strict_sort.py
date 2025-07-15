"""Strict alphabetical sorting for Hànyǔ Pīnyīn words.

Sorts Pīnyīn strings or dictionaries letter by letter, treating tone marks as integral
to letters (e.g., a < ā < á < ǎ < à). Inspired by, but stricter than, the ABC Chinese-English Dictionary.
See https://github.com/alfons/PinyinStrictSort for details.
"""

from functools import cmp_to_key

def _compare_pinyin(w1: str, w2: str) -> int:
    """Compare two Pīnyīn strings for strict alphabetical ordering.

    Args:
        w1: First Pīnyīn string.
        w2: Second Pīnyīn string.

    Returns:
        -1 if w1 < w2, 1 if w1 > w2, 0 if equal, based on strict rules.
    """
    ordered_chars = "0123456789aāáǎàbcdeēéěèfghiīíǐìjklmnoōóǒòpqrsstuūúǔùüǖǘǚǜvwxyz'- "
    weights = {char: i for i, char in enumerate(ordered_chars)}
    offset = len(ordered_chars)

    # Step 1: Compare lowercase (tones preserved)
    lower_w1, lower_w2 = w1.lower(), w2.lower()
    seq1 = [weights.get(c, ord(c) + offset) for c in lower_w1]
    seq2 = [weights.get(c, ord(c) + offset) for c in lower_w2]
    cmp_lower = (seq1 > seq2) - (seq1 < seq2)

    # Step 2: Tiebreaker with original case
    if cmp_lower == 0:
        seq1_orig = [weights.get(c, ord(c) + offset) for c in w1]
        seq2_orig = [weights.get(c, ord(c) + offset) for c in w2]
        return (seq1_orig > seq2_orig) - (seq1_orig < seq2_orig)
    return cmp_lower

def pinyin_strict_sort(items, key: str = None, reverse: bool = False) -> list:
    """Sort Pīnyīn strings or dictionaries in strict alphabetical order.

    Args:
        items: List of Pīnyīn strings or dictionaries containing Pīnyīn.
        key: Dictionary key for Pīnyīn strings (default: None for strings).
        reverse: If True, sort in descending order (default: False).

    Returns:
        Sorted list of items.

    Examples:
        >>> pinyin_strict_sort(["bǎozhàng", "Bǎoyǔ", "bǎoyù"])
        ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']
        >>> pinyin_strict_sort([{"pinyin": "bǎozhàng"}, {"pinyin": "bǎoyù"}], key="pinyin")
        [{"pinyin": "bǎoyù"}, {"pinyin": "bǎozhàng"}]
    """
    extractor = (lambda x: x[key]) if key else lambda x: x
    items_list = list(items)
    items_list.sort(key=cmp_to_key(lambda a, b: _compare_pinyin(extractor(a), extractor(b))), reverse=reverse)
    return items_list

if __name__ == "__main__":
    test_words = [
        "bāozi", "baozi", "báozi", "bǎozi", "bàozi",
        "bǎozi", "Bǎozi", "BǍOZI",
        "lù", "lü", "Lù", "Lǚ",
        "bǎo", "bǎo an", "bǎo-an", "bǎo'an",
        "bǎozhǎng", "bǎozhàng", "bǎozhàngjiāndū",
        "bǎoyù", "bǎozàng", "bǎpa", "bǎshǐ",
        "bǎOYÙ", "Bǎoyù", "bĀozì", "Bǎoyǔ",
        "ǎ", "à", "a","á","ā",
        "zǐ", "Zǐ",
        "bǎo an-xiǎo", "bǎo'an xiǎo",
        "nǚ", "Nǚ", "nǜrén",
        "lìgōng", "lǐ-gōng",
        "bǎo#", "bǎo$", "bǎo©"
    ]
    sorted_words = pinyin_strict_sort(test_words)
    print("\n".join(sorted_words))
    dicts = [
        {"pinyin": "bǎozhàng", "meaning": "guarantee"},
        {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
        {"pinyin": "bǎoyù", "meaning": "jade"}
    ]
    sorted_dicts = pinyin_strict_sort(dicts, key="pinyin")
    print(sorted_dicts)
