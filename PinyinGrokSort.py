"""
PinyinGrokSort - A Pinyin sorting module with custom rules.

Description:
    This module implements a Pinyin sorting algorithm based on rules outlined by John DeFrancis in
    "ABC Chinese-English Dictionary". It sorts Pinyin strings considering base characters, tones,
    umlauts (u vs ü), case sensitivity, and separators. The rules are:
    1. Sort by base characters (ignoring tones, case, and separators) alphabetically.
    2. For identical bases, sort by tones (0=no tone, 1=ā, 2=á, 3=ǎ, 4=à) per syllable.
    3. For identical tones, sort u before ü.
    4. For identical u/ü, sort lowercase/mixed case before all uppercase (proportion-based).
    5. For identical case, sort by separators: no separator < space < hyphen.

    The sort can handle plain Pinyin strings or lists of dictionaries with a specified key.

Credits:
    - John DeFrancis: Original Pinyin sorting rules from "ABC Chinese-English Dictionary".
    - Mark Swofford: Preserving and explaining the rules via pinyin.info blog.
    - Grok (xAI): Coding the implementation with flair and precision.
    - Alfons Grabher: Prompting, testing, and driving the development.

Usage:
    - For strings: `sorted_list = pinyin_grok_sort(["hòujìn", "Hòu Jìn"])`
    - For dictionaries: `sorted_list = pinyin_grok_sort([{"pinyin": "hòujìn"}, {"pinyin": "Hòu Jìn"}], key="pinyin")`
"""

from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    """Compare two Pinyin words with proper sorting rules."""
    def get_base_and_tones(word):
        base = ""
        tones = []
        syllable = ""
        for c in word.lower():
            if c in ' -':  # Handle separators
                if syllable:
                    tones.append(0)  # No tone for consonant-only syllables
                    base += syllable.translate(str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ', 'aaaaeeeeiiiioooouuuuüüüü'))
                    syllable = ""
                continue
            syllable += c
            if c in 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ':
                tones.append(1 if c in 'āēīōūǖ' else 2 if c in 'áéíóúǘ' else 3 if c in 'ǎěǐǒǔǚ' else 4 if c in 'àèìòùǜ' else 0)
        if syllable:  # Handle last syllable
            base += syllable.translate(str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ', 'aaaaeeeeiiiioooouuuuüüüü'))
            tones.append(0 if not any(c in 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ' for c in syllable) else tones[-1] if tones else 0)
        return base, tones

    base1, tones1 = get_base_and_tones(w1)
    base2, tones2 = get_base_and_tones(w2)

    if base1 != base2:
        return -1 if base1 < base2 else 1
    if tones1 != tones2:
        return -1 if tones1 < tones2 else 1

    u1, u2 = 'ü' in w1.lower(), 'ü' in w2.lower()
    if u1 != u2:
        return 1 if u1 else -1

    alpha1, alpha2 = [c for c in w1 if c.isalpha()], [c for c in w2 if c.isalpha()]
    case1 = sum(c.isupper() for c in alpha1) / len(alpha1) if alpha1 else 0
    case2 = sum(c.isupper() for c in alpha2) / len(alpha2) if alpha2 else 0
    if case1 != case2:
        return -1 if case1 < case2 else 1

    sep1 = 0 if ' ' not in w1 and '-' not in w1 else 1 if ' ' in w1 else 2
    sep2 = 0 if ' ' not in w2 and '-' not in w2 else 1 if ' ' in w2 else 2
    return -1 if sep1 < sep2 else 1 if sep1 > sep2 else 0

def pinyin_grok_sort(items, key=None, reverse=False):
    """
    Sort a list of Pinyin strings or dictionaries using custom Pinyin rules.

    Args:
        items (list): List of strings or dictionaries to sort.
        key (str, optional): Dictionary key to extract Pinyin strings from. If None, assumes items are strings.
        reverse (bool, optional): Sort in descending order if True. Default is False (ascending, A to Z).

    Returns:
        list: Sorted list of items.
    """
    extractor = (lambda x: x[key]) if key else (lambda x: x)
    return sorted(items, key=cmp_to_key(lambda a, b: _compare_pinyin(extractor(a), extractor(b))), reverse=reverse)

if __name__ == "__main__":
    # Test with strings
    test_words = ["shīshi", "shīshī", "shīshí", "hòujìn", "Hòu Jìn", "Hòujìn", "bólì", "bōli", "HòuJìn"]
    print("Sorted strings:")
    for word in pinyin_grok_sort(test_words):
        print(word)
    
    # Test with dictionaries
    test_dicts = [{"pinyin": "bólì", "meaning": "later Jin"}, {"pinyin": "bōli", "meaning": "Later Jin dynasty"}]
    print("\nSorted dictionaries:")
    for item in pinyin_grok_sort(test_dicts, key="pinyin"):
        print(item)
