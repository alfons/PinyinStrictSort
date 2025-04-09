# PinyinAbcSort (first working version)

I include the first working version for anyone who's interested
how the implementation looked like in the beginning. I had quite
a few versions before I arrived at the final implementation,
within 4 days.

Have fun studying Chinese with Pīnyīn!

Alfons

## Code

```python
def compare_pinyin(word1, word2):
    """Compare two Pinyin words letter by letter."""
    len1, len2 = len(word1), len(word2)
    i = 0
    tones1, tones2 = [], []
    
    # Step 1: Letter-by-letter comparison
    while i < min(len1, len2):
        c1, c2 = word1[i].lower(), word2[i].lower()
        
        # Stop at separators for tone/base
        if c1 in ' -' or c2 in ' -':
            break
        
        # Base comparison (strip tones)
        base1 = c1.replace('ā', 'a').replace('á', 'a').replace('ǎ', 'a').replace('à', 'a')\
                 .replace('ē', 'e').replace('é', 'e').replace('ě', 'e').replace('è', 'e')\
                 .replace('ī', 'i').replace('í', 'i').replace('ǐ', 'i').replace('ì', 'i')\
                 .replace('ō', 'o').replace('ó', 'o').replace('ǒ', 'o').replace('ò', 'o')\
                 .replace('ū', 'u').replace('ú', 'u').replace('ǔ', 'u').replace('ù', 'u')\
                 .replace('ǖ', 'ü').replace('ǘ', 'ü').replace('ǚ', 'ü').replace('ǜ', 'ü')
        base2 = c2.replace('ā', 'a').replace('á', 'a').replace('ǎ', 'a').replace('à', 'a')\
                 .replace('ē', 'e').replace('é INVISIBLE SPACE HERE', 'e').replace('ě', 'e').replace('è', 'e')\
                 .replace('ī', 'i').replace('í', 'i').replace('ǐ', 'i').replace('ì', 'i')\
                 .replace('ō', 'o').replace('ó', 'o').replace('ǒ', 'o').replace('ò', 'o')\
                 .replace('ū', 'u').replace('ú', 'u').replace('ǔ', 'u').replace('ù', 'u')\
                 .replace('ǖ', 'ü').replace('ǘ', 'ü').replace('ǚ', 'ü').replace('ǜ', 'ü')
        
        if base1 != base2:
            print(f"Comparing {word1} vs {word2}: Base diff at pos {i} ({base1} vs {base2})")
            return -1 if base1 < base2 else 1
        
        # Collect tones for vowels
        if c1 in 'aeiouüāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ':
            tone1 = 0
            if c1 in 'āēīōūǖ': tone1 = 1
            elif c1 in 'áéíóúǘ': tone1 = 2
            elif c1 in 'ǎěǐǒǔǚ': tone1 = 3
            elif c1 in 'àèìòùǜ': tone1 = 4
            tones1.append(tone1)
        if c2 in 'aeiouüāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ':
            tone2 = 0
            if c2 in 'āēīōūǖ': tone2 = 1
            elif c2 in 'áéíóúǘ': tone2 = 2
            elif c2 in 'ǎěǐǒǔǚ': tone2 = 3
            elif c2 in 'àèìòùǜ': tone2 = 4
            tones2.append(tone2)
        
        i += 1
    
    # Step 2: Length check (before separators)
    if len1 != len2:
        print(f"Comparing {word1} vs {word2}: Length diff ({len1} vs {len2})")
        return -1 if len1 < len2 else 1
    
    # Step 3: Compare tones
    if tones1 != tones2:
        print(f"Comparing {word1} vs {word2}: Tone diff ({tones1} vs {tones2})")
        return -1 if tones1 < tones2 else 1
    
    # Step 4: u vs ü
    u1 = any(c in 'ǖǘǚǜü' for c in word1.lower())
    u2 = any(c in 'ǖǘǚǜü' for c in word2.lower())
    if u1 != u2:
        print(f"Comparing {word1} vs {word2}: u/ü diff ({u1} vs {u2})")
        return 1 if u1 else -1
    
    # Step 5: Case (lowercase/mixed before all uppercase)
    alpha1 = [c for c in word1 if c.isalpha()]
    alpha2 = [c for c in word2 if c.isalpha()]
    case1 = sum(1 for c in alpha1 if c.isupper()) / len(alpha1) if alpha1 else 0
    case2 = sum(1 for c in alpha2 if c.isupper()) / len(alpha2) if alpha2 else 0
    if case1 != case2:
        print(f"Comparing {word1} vs {word2}: Case diff ({case1} vs {case2})")
        return -1 if case1 < case2 else 1
    
    # Step 6: Separators ('' < ' ' < '-')
    sep1 = 0 if ' ' not in word1 and '-' not in word1 else 1 if ' ' in word1 else 2
    sep2 = 0 if ' ' not in word2 and '-' not in word2 else 1 if ' ' in word2 else 2
    if sep1 != sep2:
        print(f"Comparing {word1} vs {word2}: Separator diff ({sep1} vs {sep2})")
        return -1 if sep1 < sep2 else 1
    
    print(f"Comparing {word1} vs {word2}: Equal")
    return 0

def pinyin_bubble_sort(words):
    """Bubble sort implementation for Pinyin."""
    n = len(words)
    words = words.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_pinyin(words[j], words[j + 1]) > 0:
                words[j], words[j + 1] = words[j + 1], words[j]
    return words

# Test list
test_words = [
    "shīshi", "shīshī", "shīshí", "shīshǐ", "shīshì",
    "shíshī", "shíshì", "shǐshī", "shìshī",
    "lu", "lú", "lǔ", "lù", "lǘ", "lǚ", "lǜ", "lū", "lōu",
    "nù", "nǚ", "nà", "na", "nā",
    "biàn", "bǐ’àn", "bi’àn",
    "hòujìn", "Hòu Jìn", "Hòujìn", "Hòu Jin", "Hòu-Jìn", "HòuJìn",
    "hòumiànpíng’ān", "píng", "pīnyīn",
    "lìgōng", "lǐ-gōng"
]

sorted_words = pinyin_bubble_sort(test_words)
print("Sorted output:")
for word in sorted_words:
    print(word)
```
