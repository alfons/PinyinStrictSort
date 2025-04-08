/*
PinyinGrokSort - Sort words in Hànyǔ Pīnyīn in alphabetical order (fast)

Description:
    This module implements a Pinyin sorting algorithm based on rules outlined by John DeFrancis in
    "ABC Chinese-English Dictionary". It sorts Pinyin strings considering base characters, tones,
    umlauts (u vs ü), case sensitivity, and separators. The rules are:
    1. Sort by base characters (ignoring tones, case, and separators) alphabetically.
    2. For identical bases, sort by tones (0=no tone, 1=ā, 2=á, 3=ǎ, 4=à) per syllable.
    3. For identical tones, sort u before ü.
    4. For identical u/ü, sort lowercase/mixed case before all uppercase (proportion-based).
    5. For identical case, sort by separators: no separator < space < hyphen.

    The sort can handle plain Pinyin strings or lists of dictionaries with a specified key.

Credits:
    - John DeFrancis: Original Pinyin sorting rules from "ABC Chinese-English Dictionary".
    - Mark Swofford: Preserving and explaining the rules via pinyin.info blog.
    - Grok (xAI): Coding the implementation with flair and precision.
    - Alfons Grabher: Prompting, testing, and driving the development.

Usage:
    - For an array of strings: pinyinGrokSort(listOfWords);
    - In reverse order: pinyinGrokSort(listOfWords, { reverse: true });
    - For an array of dictionaries: pinyinGrokSort(listOfdicts, { key: "pinyin" });
    
    with, for example: 
    const listOfWords = ["shīshi", "shīshí", "bōli"];
    const listOfdicts = [{ pinyin: "ér", meaning: "two" }, { pinyin: "yī", meaning: "one" }];
*/

function comparePinyin(w1, w2) {
    // Helper function to process base characters and tones
    function getBaseAndTones(word) {
        const toneMap = {
            'ā': 'a1', 'á': 'a2', 'ǎ': 'a3', 'à': 'a4',
            'ē': 'e1', 'é': 'e2', 'ě': 'e3', 'è': 'e4',
            'ī': 'i1', 'í': 'i2', 'ǐ': 'i3', 'ì': 'i4',
            'ō': 'o1', 'ó': 'o2', 'ǒ': 'o3', 'ò': 'o4',
            'ū': 'u1', 'ú': 'u2', 'ǔ': 'u3', 'ù': 'u4',
            'ǖ': 'ü1', 'ǘ': 'ü2', 'ǚ': 'ü3', 'ǜ': 'ü4'
        };
        
        let base = '';
        const tones = [];
        let syllable = '';
        const lowerWord = word.toLowerCase();

        for (const c of lowerWord) {
            if (c === ' ' || c === '-') {
                if (syllable) {
                    tones.push(0);
                    base += syllable.replace(/[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]/g, 
                        m => toneMap[m][0]);
                    syllable = '';
                }
                continue;
            }
            syllable += c;
            if (c in toneMap) {
                tones.push(parseInt(toneMap[c][1]));
            }
        }
        
        if (syllable) {
            base += syllable.replace(/[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]/g, 
                m => toneMap[m][0]);
            tones.push(tones.length && /[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]/.test(syllable) 
                ? tones[tones.length - 1] : 0);
        }
        
        return [base, tones];
    }

    const [base1, tones1] = getBaseAndTones(w1);
    const [base2, tones2] = getBaseAndTones(w2);

    // Compare base strings
    if (base1 !== base2) {
        return base1 < base2 ? -1 : 1;
    }

    // Compare tones
    const tones1Str = tones1.join('');
    const tones2Str = tones2.join('');
    if (tones1Str !== tones2Str) {
        return tones1Str < tones2Str ? -1 : 1;
    }

    // Compare ü presence
    const u1 = w1.toLowerCase().includes('ü');
    const u2 = w2.toLowerCase().includes('ü');
    if (u1 !== u2) {
        return u1 ? 1 : -1;
    }

    // Compare case ratio
    const alpha1 = w1.split('').filter(c => /[a-zA-Z]/.test(c));
    const alpha2 = w2.split('').filter(c => /[a-zA-Z]/.test(c));
    const case1 = alpha1.length ? alpha1.filter(c => /[A-Z]/.test(c)).length / alpha1.length : 0;
    const case2 = alpha2.length ? alpha2.filter(c => /[A-Z]/.test(c)).length / alpha2.length : 0;
    if (case1 !== case2) {
        return case1 < case2 ? -1 : 1;
    }

    // Compare separators
    const sep1 = !w1.includes(' ') && !w1.includes('-') ? 0 : w1.includes(' ') ? 1 : 2;
    const sep2 = !w2.includes(' ') && !w2.includes('-') ? 0 : w2.includes(' ') ? 1 : 2;
    return sep1 < sep2 ? -1 : sep1 > sep2 ? 1 : 0;
}

function pinyinGrokSort(items, options = {}) {
    const { key = null, reverse = false } = options;
    const extractor = key ? (item => item[key]) : (item => item);
    
    return [...items].sort((a, b) => {
        const result = comparePinyin(extractor(a), extractor(b));
        return reverse ? -result : result;
    });
}

// Example usage:
if (typeof module === 'undefined') {
    // Test with strings
    const testWords = ["shīshi", "shīshī", "shīshí", "hòujìn", "Hòu Jìn", "Hòujìn", "bólì", "bōli", "HòuJìn"];
    console.log("Sorted strings:");
    console.log(pinyinGrokSort(testWords));

    // Test with objects
    const testDicts = [
        { pinyin: "bólì", meaning: "later Jin" },
        { pinyin: "bōli", meaning: "Later Jin dynasty" }
    ];
    console.log("\nSorted dictionaries:");
    console.log(pinyinGrokSort(testDicts, { key: "pinyin" }));
}

// Export for Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { pinyinGrokSort, comparePinyin };
}