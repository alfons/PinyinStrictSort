"""
PinyinGrokSort - A Pīnyīn sorting module

## Description

A fast sorting algorithm to sort words in Hànyǔ Pīnyīn in alphabetical order, 
inspired by the "ABC Chinese-English Dictionary" by John DeFrancis.

Hànyǔ Pīnyīn is the romanised writing form of modern, spoken, standard Chinese. 
The sorting algorithm is intended for Pīnyīn with diacritics (no fall-back to tone numbers.) 
It is assumed that words are written letter by letter, not by pre-defined syllable blocks.

## The Rules

    1. Sort by base characters (ignoring tones, case, and separators) alphabetically.
    2. Sort by tones: no tone, 1st tone (ā), 2nd tone (á), 3rd tone (ǎ), 4th tone (à).
    3. Sort u before ü.
    4. Sort lowercase/mixed case before all uppercase.
    5. Sort by separators: no separator < space < hyphen.


## Credits

    - John DeFrancis: Original Pinyin sorting rules from "ABC Chinese-English Dictionary".
    - Mark Swofford of Banqiao, Taiwan: Explaining the rules on the pinyin.info blog.
    - Grok (xAI): Coding the implementation with flair and precision.
    - Alfons Grabher: Idea, prompting, testing, and driving the development.

Usage:
    - For strings: `sorted_list = pinyin_grok_sort(["shīshi", "shīshī", "shīshí", "shīshǐ"])`
    - For dictionaries: `sorted_list = pinyin_grok_sort([{"pinyin": "shīshí"}, {"pinyin": "shīshi"}], key="pinyin")`
"""

from functools import cmp_to_key

def _compare_pinyin(w1, w2):
    """Compare two Pinyin words with proper sorting rules."""
    tones1, tones2 = [], []
    i, len1, len2 = 0, len(w1), len(w2)
    
    while i < min(len1, len2):
        c1, c2 = w1[i].lower(), w2[i].lower()
        if c1 in ' -' or c2 in ' -': break
        
        base1 = c1.translate(str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ', 'aaaaeeeeiiiioooouuuuüüüü'))
        base2 = c2.translate(str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ', 'aaaaeeeeiiiioooouuuuüüüü'))
        if base1 != base2:
            return -1 if base1 < base2 else 1
        
        for c, tones in [(c1, tones1), (c2, tones2)]:
            if c in 'aeiouüāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ':
                tones.append(1 if c in 'āēīōūǖ' else 2 if c in 'áéíóúǘ' else 3 if c in 'ǎěǐǒǔǚ' else 4 if c in 'àèìòùǜ' else 0)
        
        i += 1
    
    if len1 != len2:
        return -1 if len1 < len2 else 1
    
    if tones1 != tones2:
        return -1 if tones1 < tones2 else 1
    
    u1, u2 = any(c in 'ǖǘǚǜü' for c in w1.lower()), any(c in 'ǖǘǚǜü' for c in w2.lower())
    if u1 != u2:
        return 1 if u1 else -1
    
    alpha1, alpha2 = [c for c in w1 if c.isalpha()], [c for c in w2 if c.isalpha()]
    case1, case2 = sum(c.isupper() for c in alpha1) / len(alpha1) if alpha1 else 0, sum(c.isupper() for c in alpha2) / len(alpha2) if alpha2 else 0
    if case1 != case2:
        return -1 if case1 < case2 else 1
    
    sep1, sep2 = (0 if ' ' not in w1 and '-' not in w1 else 1 if ' ' in w1 else 2), (0 if ' ' not in w2 and '-' not in w2 else 1 if ' ' in w2 else 2)
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
    test_words = ["shīshi", "shīshī", "shīshí", "shīshǐ", "shīshì", "shíshī", "shíshì", "shǐshī", "shìshī",
              "lu", "lú", "lǔ", "lù", "lǘ", "lǚ", "lǜ", "lū", "lōu", "nù", "nǚ", "nà", "na", "nā",
              "biàn", "bǐ’àn", "bi’àn", "hòujìn", "Hòu Jìn", "Hòujìn", "Hòu Jin", "Hòu-Jìn", "HòuJìn",
              "hòumiànpíng’ān", "píng", "pīnyīn", "lìgōng", "lǐ-gōng"]
    print("Sorted strings:")
    for word in pinyin_grok_sort(test_words):
        print(word)
    
    # Test with dictionaries
    test_dicts = [{"pinyin": "duìjù", "meaning": "couplet"}, {"pinyin": "duìjú", "meaning": "opposing sides (in chess etc)"}]
    print("\nSorted dictionaries:")
    for item in pinyin_grok_sort(test_dicts, key="pinyin"):
        print(item)
