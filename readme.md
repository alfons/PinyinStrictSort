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

### Python

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

### Javascript

```javascript
// Array of Strings
const words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"];
const sortedWords = pinyinAbcSort(words);
console.log(sortedWords); // ["bǎoyù", "bǎozhàng", "Bǎoyǔ"]

// Array of Dictionaries
const dicts = [
    { pinyin: "bǎozhàng", meaning: "guarantee" },
    { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
    { pinyin: "bǎoyù", meaning: "jade" }
];
const sortedDicts = pinyinAbcSort(dicts, item => item.pinyin);
console.log(sortedDicts);
// [
//   { pinyin: "bǎoyù", meaning: "jade" },
//   { pinyin: "bǎozhàng", meaning: "guarantee" },
//   { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" }
// ]

// Reverse Order (Strings)
const reverseWords = pinyinAbcSort(words, null, true);
console.log(reverseWords); // ["Bǎoyǔ", "bǎozhàng", "bǎoyù"]

// Reverse Order (Dictionaries)
const reverseDicts = pinyinAbcSort(dicts, item => item.pinyin, true);
console.log(reverseDicts);
// [
//   { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
//   { pinyin: "bǎozhàng", meaning: "guarantee" },
//   { pinyin: "bǎoyù", meaning: "jade" }
// ]
```

## History

This was much more difficult than expected, and took much, much more time than expected. 
But in the end it looks so simple, almost laughably simple, and flies like a 
Raptor SpaceX booster rocket. 🚀
