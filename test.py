from pinyin_strict_sort import pinyin_strict_sort

test_words = [
    "bāozi", "baozi", "báozi", "bǎozi", "bàozi",
    "bǎozi", "Bǎozi", "BǍOZI",
    "lù", "lü", "Lù", "Lǚ",
    "bǎo", "bǎo an", "bǎo-an", "bǎo'an",
    "bǎozhǎng", "bǎozhàng", "bǎozhàngjiāndū",
    "bǎoyù", "bǎozàng", "bǎpa", "bǎshǐ",
    "bǎOYÙ", "Bǎoyù", "bĀozì", "Bǎoyǔ",
    "ǎ", "à", "a", "á", "ā",
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
