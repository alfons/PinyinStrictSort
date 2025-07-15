// Load pinyinStrictSort.js (assumes it's in the same directory)
require('./pinyinStrictSort.js');

// Test 1: Sort strings
const words = ['bǎozhàng', 'Bǎoyǔ', 'bǎoyù'];
console.log('Sorted strings:', pinyinStrictSort(words));
console.log('Reverse sorted strings:', pinyinStrictSort(words, null, true));

// Test 2: Sort objects
const dicts = [
  { pinyin: 'bǎozhàng', meaning: 'guarantee' },
  { pinyin: 'Bǎoyǔ', meaning: 'Bao Yu (name)' },
  { pinyin: 'bǎoyù', meaning: 'jade' }
];
console.log('Sorted objects:', pinyinStrictSort(dicts, 'pinyin'));
console.log('Reverse sorted objects:', pinyinStrictSort(dicts, 'pinyin', true));

// Test 3: Extended test cases
const extendedWords = [
  'baozi', 'báozi', 'bǎozi', 'bàozi', 'bāozi',
  'lù', 'lú', 'lü', 'Lù', 'Lǚ',
  'bǎo', 'bǎo an', 'bāo', 'bǎo-an', 'bǎo\'an'
];
console.log('Extended sorted strings:', pinyinStrictSort(extendedWords));
