const fs = require('fs');

const file = fs.readFileSync('./day6_input');
const lines = file.toString().split('\n');

let sum = 0;
let sum2 = 0;

const letterArray = Array.from({ length: 26 }, (v, k) => String.fromCharCode(97 + k));
const letterSet = new Set();
const userSet = new Set();
let groupSet = new Set(letterArray);

for (const line of lines) {
  if (line === '') {
    sum += letterSet.size;
    sum2 += groupSet.size;
    letterSet.clear();
    groupSet = new Set(letterArray);
    continue;
  }

  for (const letter of line) {
    letterSet.add(letter);
    userSet.add(letter);
  }

  groupSet = new Set([...userSet].filter(l => groupSet.has(l)));
  userSet.clear();
}

console.log(sum);
console.log(sum2);
