# PinyinGrokSort - Sort words in Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:
This module implements a Pinyin sorting algorithm based on 
rules outlined by John DeFrancis in "ABC Chinese-English Dictionary". 
    
Note：☝️ The sorting algorithm looks at words letter by letter, 
not syllable by syllable, as Pīnyīn is written using the ALPHABET, 
a realisation and algorithm design concept by Alfons Grabher.

## The rules are:
    
1. Alphabetical Order: Base chars (a-z) first, letter-by-letter.
2. u before ü, U before Ü.
3. Tones: 0 < 1 < 2 < 3 < 4
4. Lowercase/mixed before uppercase.
5. Separators: single quote < hyphen < space.
    
The sort handles arrays of plain Pīnyīn strings, or arrays of dictionaries with a specified key.

## Credits:

- John DeFrancis: Original Pinyin sorting rules from "ABC Chinese-English Dictionary".
- Mark Swofford of Banqiao, Taiwan: Preserving and explaining the rules.
- Alfons Grabher: Concept, ideas, prompting, testing, and driving the development.
- Grok (xAI): Coding the implementation with flair and precision.

## Usage 

### Python
    
```python
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
```
### Javascript

```javascript
    // Array of Strings
    const words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"];
    const sortedWords = pinyinGrokSort(words);
    console.log(sortedWords); // ["bǎoyù", "bǎozhàng", "Bǎoyǔ"]

    // Array of Dictionaries
    const dicts = [
        { pinyin: "bǎozhàng", meaning: "guarantee" },
        { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
        { pinyin: "bǎoyù", meaning: "jade" }
    ];
    const sortedDicts = pinyinGrokSort(dicts, item => item.pinyin);
    console.log(sortedDicts);
    // [
    //   { pinyin: "bǎoyù", meaning: "jade" },
    //   { pinyin: "bǎozhàng", meaning: "guarantee" },
    //   { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" }
    // ]

    // Reverse Order (Strings)
    const reverseWords = pinyinGrokSort(words, null, true);
    console.log(reverseWords); // ["Bǎoyǔ", "bǎozhàng", "bǎoyù"]

    // Reverse Order (Dictionaries)
    const reverseDicts = pinyinGrokSort(dicts, item => item.pinyin, true);
    console.log(reverseDicts);
    // [
    //   { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
    //   { pinyin: "bǎozhàng", meaning: "guarantee" },
    //   { pinyin: "bǎoyù", meaning: "jade" }
    // ]
```

## History

This was much more difficult than expected, and took much, much more time than expected. 
But in the end it looks so simple, almost laughable simple, and flies like a 
Raptor SpaceX booster rocket. 🚀
