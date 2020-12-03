const input = require('./day3_input.json');
const checks = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];

let answer = 1;

for (let c of checks) {
  let treesCount = 0;
  let i = 0;
  let j = 0;

  while (i < input.length) {
    if (input[i][j] === '#') {
      ++treesCount;
    }

    j = (j + c[0]) % input[i].length;
    i += c[1];
  }

  console.log(`r${c[0]} d${c[1]}:`, treesCount);
  answer *= treesCount;
}

console.log('mul: ', answer);
