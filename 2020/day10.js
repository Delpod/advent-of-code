const fs = require('fs');

const file = fs.readFileSync('./day10_input');

const jolts = file.toString().split('\n').map(Number).sort((a, b) => a - b);
jolts.unshift(0);
jolts.push(jolts[jolts.length - 1] + 3);
const differences = { 1: 0, 2: 0, 3: 0 };
const ways = { 0: 1 };

for (let i = 0, j = 0; i < jolts.length - 1; ++i, j = i) {
  ++differences[jolts[i + 1] - jolts[i]];

  while (jolts[++j] <= jolts[i] + 3) {
    ways[j] = (ways[j] || 0) + (ways[i] || 0);
  }
}

console.log(differences[1] * differences[3]);
console.log(ways[jolts.length - 1]);
