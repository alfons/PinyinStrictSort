# PinyinStrictSort - Sort Hànyǔ Pīnyīn in alphabetical order (fast)

## Description:

Sort Chinese (Hànyǔ) Pīnyīn words into strict alphabetical order.

1. Compare words letter by letter, not syllable by syllable. 
2. Respect diacritics (tone marks) as part of the letter, not merely 
as tiebreaker.

This approach reflects **the fact that Hànyǔ Pīnyīn is written using the Latin 
alphabet** — the key insight behind this implementation.

## The ordering rules are:

 1. Alphabetical order, including diacritics (tone marks)
 2. Tone marks sorting order 0 < 1 < 2 < 3 < 4 (for example, a < ā < á < ǎ < à)
 3. u before ü, U before Ü
 4. lowercase and mixed-case before uppercase
 5. Separators: apostrophe < hyphen < space
 6. Numbers sort before letters.
 7. All other characters sort behind, according to their Unicode value.

This project was initially inspired by by John DeFrancis in ABC Chinese-English 
Dictionary, Page xiii, Reader’s Guide, I. Arrangement of Entries, but sorting
by PinyinStrictSort is much stricter and more straightforward.

Link to Wiki about the differences in word order between PinyinStrictSort and the 
ABC Chinese-English Dictionary: 
[PinyinStrictSort Wiki](https://github.com/alfons/PinyinStrictSort/wiki)

## Acknowledgements and Credits:

 - John DeFrancis (1911-2009), in passionate acknowledgment of the advocates 
of writing reform Lù Zhuāngzhāng (陆璋章,1854–1928), Lǔ Xùn (鲁迅, 1881–1936), 
Máo Dùn (Shěn Yànbīng, 茅盾, 沈雁冰, 1896–1981), Wáng Lì (王力, 1900–1988) and 
Lù Shūxiāng (吕叔湘, 1904–1998), and Zhōu Yǒuguāng (周有光, 1905–2017).
 - Mark Swofford of Bǎnqiáo, Táiwān: summarised the rules outlined by 
John DeFrancis on his blog, thus keeping them available to the world.
 - Alfons Grabher: Idea, concept, coding, prompting, testing, and driving the 
development of PinyinStrictSort.
 - Grok (xAI), ChatGPT 4o: Coding the implementation with flair and precision.

## Usage 

### Python

```python
from pinyin_strict_sort import pinyin_strict_sort

# Sort strings
words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"]
print(pinyin_strict_sort(words))  # ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']

# Sort dictionaries
dicts = [
    {"pinyin": "bǎozhàng", "meaning": "guarantee"},
    {"pinyin": "Bǎoyǔ", "meaning": "Bao Yu (name)"},
    {"pinyin": "bǎoyù", "meaning": "jade"}
]
print(pinyin_strict_sort(dicts, key="pinyin"))

# Reverse order
print(pinyin_strict_sort(words, reverse=True))  # ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']
```

### Javascript

```javascript
// Sort strings
const words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"];
console.log(pinyinStrictSort(words)); // ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']

// Sort objects
const dicts = [
    { pinyin: "bǎozhàng", meaning: "guarantee" },
    { pinyin: "Bǎoyǔ", meaning: "Bao Yu (name)" },
    { pinyin: "bǎoyù", meaning: "jade" }
];
console.log(pinyinStrictSort(dicts, "pinyin"));

// Reverse order
console.log(pinyinStrictSort(words, null, true)); // ['Bǎoyǔ', 'bǎozhàng', 'bǎoyù']
```

### HTML
```html
<script src="pinyinStrictSort.js"></script>
<script>
    const words = ["bǎozhàng", "Bǎoyǔ", "bǎoyù"];
    console.log(pinyinStrictSort(words)); // ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']
</script>
```

## Sorting Philosophy

PinyinStrictSort implements strict, character-by-character alphabetical ordering. This means sorting is performed exactly the way most programming languages compare strings: the first differing character determines the order. No syllable/morpheme segmentation is applied.

For example:

- `chéngjiù` < `chénjiù`

This result follows directly from strict alphabetical comparison.

```
chéngjiù
chénjiù
    ^
```

the comparison is **g < j**, therefore `chéngjiù` sorts before `chénjiù`.

### Why this may look unusual

One might expect:

```
chénjiù
chéngjiù
```

because we look at the syllables, effectively treating **chén** and **chéng** as complete units, and in our minds perform the following segmentation:

```
chén + jiù
chéng + jiù
```

PinyinStrictSort deliberately does not perform syllable segmentation.

### Example

```python
words = ['chéngjiù', 'chénjiù', 'chéng', 'chén']
print(pinyin_strict_sort(words))
```

Output:

```
['chén', 'chéng', 'chéngjiù', 'chénjiù']
```

## Comparison with other sort methods

### Hand picked word list

| PinyinStrictSort | DeFrancis | Apple Numbers | Apple Numbers |
|------------------|-----------|---------------|---------------|
| chén | chén | chen | chén |
| chéng | chéng | cheng | chéng |
| chéngjiù | chéngjiù | chengjiu | chéngjiù |
| chénjiù | chénjiù | chenjiu | chénjiù |

### Continuous entries

|   PinyinStrictSort   |   John DeFrancis et.al.  |   Apple Numbers      |
|----------------------|--------------------------|----------------------|
|   zhuānzhí           |   zhuānzhí               |   zhuǎnzhí           |
|   zhuānzhí bǎomǔ     |   zhuānzhǐ               |   zhuǎnzhì           |
|   zhuānzhí shūjì     |   zhuānzhì               |   zhuānzhí           |
|   zhuānzhǐ           |   zhuānzhì               |   zhuānzhì           |
|   zhuānzhì           |   zhuǎnzhí               |   zhuānzhì           |
|   zhuānzhì           |   zhuǎnzhì               |   zhuānzhǐ           |
|   zhuānzhìzhǔyì      |   zhuānzhí bǎomǔ         |   zhuānzhí bǎomǔ     |
|   zhuānzhì júnzhǔ    |   zhuānzhì júnzhǔ        |   zhuānzhì júnzhǔ    |
|   zhuānzhì qǐlai     |   zhuānzhì qǐlai         |   zhuānzhì qǐlai     |
|   zhuānzhì réngé     |   zhuānzhì réngé         |   zhuānzhì réngé     |
|   zhuānzhì xìnggé    |   zhuānzhí shūjì         |   zhuānzhí shūjì     |
|   zhuānzhì zhēngzhì  |   zhuānzhì xìnggé        |   zhuānzhì xìnggé    |
|   zhuānzhì zhèngfǔ   |   zhuānzhì zhèngfǔ       |   zhuānzhì zhèngfǔ   |
|   zhuānzhì zhèngtǐ   |   zhuānzhì zhèngtǐ       |   zhuānzhì zhèngtǐ   |
|   zhuǎnzhí           |   zhuānzhì zhēngzhì      |   zhuānzhì zhēngzhì  |
|   zhuǎnzhì           |   zhuānzhìzhǔyì          |   zhuānzhìzhǔyì      |

## History

This was much more difficult than expected, and took much longer than 
expected. But in the end it looks simple. 🚀
