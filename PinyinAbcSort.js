/*
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

*/

function comparePinyin(w1, w2) {
    const orderedChars = "aāáǎàAĀÁǍÀbBcCdDeēéěèEĒÉĚÈfFgGhHiīíǐìIĪÍǏÌjJkKlLmMnNoōóǒòOŌÓǑÒpPqQrRsStTuūúǔùUŪÚǓÙüǖǘǚǜÜǕǗǙǛvVwWxXyYzZ'- ";
    const WEIGHTS = Object.fromEntries([...orderedChars].map((ch, i) => [ch, i]));

    const seq1 = Array.from(w1).map(c => WEIGHTS[c] ?? 999);
    const seq2 = Array.from(w2).map(c => WEIGHTS[c] ?? 999);

    const len = Math.min(seq1.length, seq2.length);
    for (let i = 0; i < len; i++) {
        if (seq1[i] !== seq2[i]) return seq1[i] - seq2[i];
    }
    return seq1.length - seq2.length;
}


function pinyinAbcSort(items, key = null, reverse = false) {
    const extractor = key ? x => x[key] : x => x;
    const sorted = [...items];
    sorted.sort((a, b) => comparePinyin(extractor(a), extractor(b)));
    return reverse ? sorted.reverse() : sorted;
}
