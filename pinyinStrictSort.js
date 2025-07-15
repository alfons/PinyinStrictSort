/**
 * Strict alphabetical sorting for Hànyǔ Pīnyīn words.
 *
 * Sorts Pīnyīn strings or objects letter by letter, treating tone marks as integral
 * to letters (e.g., a < ā < á < ǎ < à). Inspired by, but stricter than, the ABC
 * Chinese-English Dictionary. See https://github.com/alfons/PinyinStrictSort/wiki for details.
 */

/**
 * Compare two Pīnyīn strings for strict alphabetical ordering.
 * @param {string} w1 - First Pīnyīn string.
 * @param {string} w2 - Second Pīnyīn string.
 * @returns {number} - Negative if w1 < w2, positive if w1 > w2, zero if equal.
 */
function comparePinyin(w1, w2) {
  const orderedChars =
    '0123456789aāáǎàAĀÁǍÀbBcCdDeēéěèEĒÉĚÈfFgGhHiīíǐìIĪÍǏÌ' +
    'jJkKlLmMnNoōóǒòOŌÓǑÒpPqQrRsStTuūúǔùUŪÚǓÙüǖǘǚǜÜǕǗǙǛvVwWxXyYzZ\'- ';

  const WEIGHTS = {};
  for (let i = 0; i < orderedChars.length; i++) {
    WEIGHTS[orderedChars[i]] = i;
  }
  const OFFSET = orderedChars.length;

  // Step 1: Compare lowercase versions first (tones intact)
  const lowerW1 = w1.toLowerCase();
  const lowerW2 = w2.toLowerCase();
  const seq1Lower = Array.from(lowerW1).map(c => (WEIGHTS[c] !== undefined ? WEIGHTS[c] : c.charCodeAt(0) + OFFSET));
  const seq2Lower = Array.from(lowerW2).map(c => (WEIGHTS[c] !== undefined ? WEIGHTS[c] : c.charCodeAt(0) + OFFSET));

  const lenLower = Math.min(seq1Lower.length, seq2Lower.length);
  for (let i = 0; i < lenLower; i++) {
    if (seq1Lower[i] !== seq2Lower[i]) return seq1Lower[i] - seq2Lower[i];
  }
  if (seq1Lower.length !== seq2Lower.length) return seq1Lower.length - seq2Lower.length;

  // Step 2: Tiebreaker with original case
  const seq1Orig = Array.from(w1).map(c => (WEIGHTS[c] !== undefined ? WEIGHTS[c] : c.charCodeAt(0) + OFFSET));
  const seq2Orig = Array.from(w2).map(c => (WEIGHTS[c] !== undefined ? WEIGHTS[c] : c.charCodeAt(0) + OFFSET));
  const lenOrig = Math.min(seq1Orig.length, seq2Orig.length);
  for (let i = 0; i < lenOrig; i++) {
    if (seq1Orig[i] !== seq2Orig[i]) return seq1Orig[i] - seq2Orig[i];
  }
  return seq1Orig.length - seq2Orig.length;
}

/**
 * Sort Pīnyīn strings or objects in strict alphabetical order.
 * @param {Array<string|Object>} items - Array of Pīnyīn strings or objects.
 * @param {string|null} [key=null] - Object key for Pīnyīn strings.
 * @param {boolean} [reverse=false] - If true, sort in descending order.
 * @returns {Array} Sorted array.
 * @example
 * const words = ['bǎozhàng', 'Bǎoyǔ', 'bǎoyù'];
 * console.log(pinyinStrictSort(words)); // ['bǎoyù', 'bǎozhàng', 'Bǎoyǔ']
 * const dicts = [{ pinyin: 'bǎozhàng' }, { pinyin: 'bǎoyù' }];
 * console.log(pinyinStrictSort(dicts, 'pinyin'));
 */
function pinyinStrictSort(items, key = null, reverse = false) {
  const extractor = typeof key === 'string' ? x => x[key] : (key || (x => x));
  const sorted = [...items];
  sorted.sort((a, b) => comparePinyin(extractor(a), extractor(b)));
  return reverse ? sorted.reverse() : sorted;
}

// Make pinyinStrictSort globally available for use in node via command line
//globalThis.pinyinStrictSort = pinyinStrictSort;
