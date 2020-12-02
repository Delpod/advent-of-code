const input = require('./day1_input.json');

let r1 = null;
let r2 = null;

for (let i = 0; i < input.length  ; ++i) {
  for (let j = 0; j < input.length; ++j) {
    if (i !== j && input[i] + input[j] === 2020) {
      r1 = [input[i], input[j], input[i] * input[j]];
      break;
    }
  }
  if (r1) {
    break;
  }
}


for (let i = 0; i < input.length; ++i) {
  for (let j = 0; j < input.length; ++j) {
    for (let k = 0; k < input.length; ++k) {
      if (i !== j && i !== k && j !== k && input[i] + input[j] + input[k] === 2020) {
        r2 = [input[i], input[j], input[k], input[i] * input[j] * input[k]];
        break;
      }
    }
    if (r2) {
      break;
    }
  }
  if (r2) {
    break;
  }
}

console.log(r1);
console.log(r2);