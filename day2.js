const input = require('./day2_input.json');

let policy1Count = 0
let policy2Count = 0

for (let i of input) {
  const parts = i.split(' ');
  const match = parts[0].match(/\d+/g);

  const num1 = Number(match[0]);
  const num2 = Number(match[1]);
  const letter = parts[1][0];
  const password = parts[2];

  const test = password.match(new RegExp(letter, 'g'));

  if (test && test.length >= num1 && test.length <= num2) {
    ++policy1Count;
  }

  if (
      (password[num1 - 1] && password[num1 - 1] === letter && (password.length < (num2 - 1) || password[num2 - 1] !== letter)) ||
      (password[num1 - 1] && password[num1 - 1] !== letter && password.length >= (num2 -1) && password[num2 - 1] === letter)
     )
  {
    ++policy2Count;
  }
}

console.log(policy1Count);
console.log(policy2Count);