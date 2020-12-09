const fs = require('fs');

const file = fs.readFileSync('./day9_input');
const lines = file.toString().split('\n');

const allNumbers = [];
const lastNumbers = [];
let missingNumber = null;

for (const line of lines) {
  const num = Number(line);
  if (lastNumbers.length === 25) {
    let found = false;
    for (let idx = 0; idx < lastNumbers.length; ++idx) {
      found = lastNumbers.find((e, i, a) => i !== idx && a[i] + a[idx] === num);
      if (found) {
        found = true;
        lastNumbers.splice(0, 1);
        break;
      }
    }

    if (!found) {
      missingNumber = num;
      break;
    }
  }

  lastNumbers.push(num);
  allNumbers.push(num);
}

console.log(missingNumber);

for (let i = 0; i < allNumbers.length; ++i) {
  let sum = 0;
  let j = i;
  while (sum < missingNumber) {
    sum += allNumbers[j++];
  }

  if (sum === missingNumber) {
    const slice = allNumbers.slice(i, j);
    console.log(Math.min(...slice) + Math.max(...slice));
    break;
  }
}
