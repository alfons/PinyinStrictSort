# PinyinAbcSort - Sort Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:

This project implements sorting Pīnyīn words into alphabetical word order, inspired by the rules outlined by John DeFrancis in ABC Chinese-English Dictionary, Page xiii, Reader’s Guide, I. Arrangement of Entries.

The sorting algorithm compares words letter by letter, not syllable by syllable. This approach reflects the fact that Hànyǔ Pīnyīn is written using the Latin alphabet — the key insight and algorithm design choice behind this implementation.

## The ordering rules are:

 1. Alphabetical order: base letters (a–z) including tones
 2. Tones 0 < 1 < 2 < 3 < 4 (for example a < ā < á < ǎ < à)
 3. u before ü, U before Ü
 4. lowercase and mixed-case before uppercase
 5. Separators: apostrophe < hyphen < space

Since no rules for numbers 0–9 were given, they were added first. All other characters are appended according to their Unicode value.

Link to Wiki about the differences in word order between PinyinAbcSort and the ABC Chinese-English Dictionary: [PinyinAbcSort Wiki](https://github.com/alfons/PinyinAbcSort/wiki)

## Credits:

 - John DeFrancis (1911-2009): Original Pīnyīn alphabetical word order, in passionate
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

### Python

```python
# Array of Strings
words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"]
sorted_words = pinyin_abc_sort(words)
print(sorted_words)

# Array of Dictionaries
dicts = [
    {"pinyin": "bǎozhàng", "meaning": "guarantee"},
    {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
    {"pinyin": "bǎoyù", "meaning": "jade"}
]
sorted_dicts = pinyin_abc_sort(dicts, key="pinyin")
print(sorted_dicts)

# Reverse Order (Strings)
reverse_words = pinyin_abc_sort(words, reverse=True)
print(reverse_words)  # ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']

# Reverse Order (Dictionaries)
reverse_dicts = pinyin_abc_sort(dicts, key="pinyin", reverse=True)
print(reverse_dicts)
```

### Javascript

```javascript
// Array of Strings
const testWords = ["bǎoyù", "Bǎoyù", "Bǎoyǔ", "bǎozhàng"];
console.log(pinyinAbcSort(testWords));
console.log(pinyinAbcSort(testWords, null, true)); //reverse

// Array of Dictionaries with default key 'pinyin'
const testDicts = [
    { pinyin: "bǎozhàng", meaning: "guarantee" },
    { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
    { pinyin: "bǎoyù", meaning: "jade" }
];
console.log(pinyinAbcSort(testDicts, "pinyin"));
console.log(pinyinAbcSort(testDicts, "pinyin", true)); //reverse
```

## History

This was much more difficult than expected, and took much longer than expected. 
But in the end it looks simple, and flies like a SpaceX starship. 🚀
