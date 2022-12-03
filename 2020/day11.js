const fs = require('fs');

const file = fs.readFileSync('./day11_input');
let seats = file.toString().split('\n').map(l => l.split(''));
let seats2 = [];
let changes = null;

while (changes !== 0) {
  changes = 0;
  for (let i = 0; i < seats.length; ++i) {
    seats2.push([]);
    for (let j = 0; j < seats[i].length; ++j) {
      if (seats[i][j] === '.') {
        seats2[i].push('.');
        continue;
      }

      const [start1, end1] = [Math.max(i - 1, 0), Math.min(i + 1, seats.length - 1)];
      const [start2, end2] = [Math.max(j - 1, 0), Math.min(j + 1, seats[i].length - 1)];
      let count = 0;
      let c2 = 0;
      for (let k = start1; k <= end1; ++k) {
        for (let l = start2; l <= end2; ++l) {
          ++c2;
          if (!(k === i && l === j) && seats[k][l] === '#') {
            ++count;
          }
        } 
      }

      if (seats[i][j] === 'L' && count === 0) {
        seats2[i].push('#');
        ++changes;
      } else if (seats[i][j] === '#' && count >= 4) {
        seats2[i].push('L');
        ++changes;
      } else {
        seats2[i].push(seats[i][j]);
      }
    }
  }
  seats = seats2;
  seats2 = [];
}

console.log(seats.map(r => r.join('')).join('').match(/#/g).length);