const fs = require('fs');

const file = fs.readFileSync('./day05_input');
const lines = file.toString().split('\n');

const seatIds = [];

for (const line of lines) {
  let id = 0;
  for (let i = 0; i < line.length; ++i) {
    if (line[i] === 'B') {
      id += 8 * 2 ** (6 - i);
    } else if (line[i] === 'R') {
      id += 2 ** (2 - (i - 7));
    }
  }

  seatIds.push(id);
}

seatIds.sort((a, b) => a - b);

console.log(seatIds[seatIds.length - 1]);
console.log(seatIds.find((s, i, a) => s + 1 !== a[i + 1]) + 1);
