/*
# PinyinAbcSort - Sort Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:

 This project implements sorting Pīnyīn words into alphabetical word order,
 based on the rules outlined by John DeFrancis in ABC Chinese-English
 Dictionary, Page xiii, Reader’s Guide, I. Arrangement of Entries.

 The sorting algorithm compares words letter by letter, not syllable by
 syllable. This approach reflects the fact that Hànyǔ Pīnyīn is written using
 the Latin alphabet — the key insight and algorithm design choice behind this
 implementation.

## The ordering rules are:

 1. Alphabetical order: Base characters (a–z), compared letter by letter
 2. u before ü, U before Ü
 3. Tones: 0 < 1 < 2 < 3 < 4
 4. Case: lowercase and mixed-case before uppercase
 5. Separators: apostrophe < hyphen < space

 Since no rules for numbers 0–9 were given, they were added first. All other
 characters are appended according to their Unicode value.

## Credits:

 - John DeFrancis: Original Pīnyīn alphabetical word order, in passionate
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

This was much more difficult than expected, and took much, much longer 
than expected. But in the end it looks so simple, almost laughably simple, 
and flies like a SpaceX starship. 🚀
*/

function comparePinyin(w1, w2) {
    const orderedChars = (
        "0123456789aāáǎàAĀÁǍÀbBcCdDeēéěèEĒÉĚÈfFgGhHiīíǐìIĪÍǏÌ" +
        "jJkKlLmMnNoōóǒòOŌÓǑÒpPqQrRsStTuūúǔùUŪÚǓÙ" +
        "üǖǘǚǜÜǕǗǙǛvVwWxXyYzZ'- "
    );
    
    const WEIGHTS = {};
    for (let i = 0; i < orderedChars.length; i++) {
        WEIGHTS[orderedChars[i]] = i;
    }
    const OFFSET = orderedChars.length;

    const seq1 = Array.from(w1).map(c => WEIGHTS[c] ?? (c.charCodeAt(0) + OFFSET));
    const seq2 = Array.from(w2).map(c => WEIGHTS[c] ?? (c.charCodeAt(0) + OFFSET));

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
