/*
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

## History

This was much more difficult than expected, and took much, much more time than expected. 
But in the end it looks so simple, almost laughable simple, and flies like a 
Raptor SpaceX booster rocket. 🚀

Alfons, alfonsgrabher.com
*/

function comparePinyin(w1, w2) {
    const WEIGHTS = {
        'a': 0, 'ā': 1, 'á': 2, 'ǎ': 3, 'à': 4, 'A': 5, 'Ā': 6, 'Á': 7, 'Ǎ': 8, 'À': 9,
        'b': 10, 'B': 11, 'c': 12, 'C': 13, 'd': 14, 'D': 15,
        'e': 16, 'ē': 17, 'é': 18, 'ě': 19, 'è': 20, 'E': 21, 'Ē': 22, 'É': 23, 'Ě': 24, 'È': 25,
        'f': 26, 'F': 27, 'g': 28, 'G': 29, 'h': 30, 'H': 31,
        'i': 32, 'ī': 33, 'í': 34, 'ǐ': 35, 'ì': 36, 'I': 37, 'Ī': 38, 'Í': 39, 'Ǐ': 40, 'Ì': 41,
        'j': 42, 'J': 43, 'k': 44, 'K': 45, 'l': 46, 'L': 47,
        'm': 48, 'M': 49, 'n': 50, 'N': 51,
        'o': 52, 'ō': 53, 'ó': 54, 'ǒ': 55, 'ò': 56, 'O': 57, 'Ō': 58, 'Ó': 59, 'Ǒ': 60, 'Ò': 61,
        'p': 62, 'P': 63, 'q': 64, 'Q': 65, 'r': 66, 'R': 67,
        's': 68, 'S': 69, 't': 70, 'T': 71,
        'u': 72, 'ū': 73, 'ú': 74, 'ǔ': 75, 'ù': 76, 'U': 77, 'Ū': 78, 'Ú': 79, 'Ǔ': 80, 'Ù': 81,
        'ü': 82, 'ǖ': 83, 'ǘ': 84, 'ǚ': 85, 'ǜ': 86, 'Ü': 87, 'Ǖ': 88, 'Ǘ': 89, 'Ǚ': 90, 'Ǜ': 91,
        'v': 92, 'V': 93, 'w': 94, 'W': 95, 'x': 96, 'X': 97,
        'y': 98, 'Y': 99, 'z': 100, 'Z': 101,
        "'": 102, '-': 103, ' ': 104
    };

    const seq1 = Array.from(w1).map(c => WEIGHTS[c] !== undefined ? WEIGHTS[c] : 999);
    const seq2 = Array.from(w2).map(c => WEIGHTS[c] !== undefined ? WEIGHTS[c] : 999);
    const len = Math.min(seq1.length, seq2.length);
    for (let i = 0; i < len; i++) {
        if (seq1[i] !== seq2[i]) {
            return seq1[i] - seq2[i];
        }
    }
    return seq1.length - seq2.length;
}

function pinyinGrokSort(items, key = null, reverse = false) {
    const extractor = key ? x => x[key] : x => x;
    const sorted = [...items];
    sorted.sort((a, b) => comparePinyin(extractor(a), extractor(b)));
    return reverse ? sorted.reverse() : sorted;
}
