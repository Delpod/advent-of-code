const fs = require('fs');

const file = fs.readFileSync('./day7_input');
const lines = file.toString().split('\n');

const testName = 'shiny gold';
const bagsContained = {};
const bagsContaining = {};

for (const line of lines) {
  const [left, ...other] = line.split(/ bags?,?\.? ?/);
  bagsContaining[left] = {};
  
  for (let rule of other) {
    rule = rule.replace('contain ', '');

    if (!rule || rule === 'no other') {
      break;
    }

    let [count, ...bag] = rule.split(' ');
    bag = bag.join(' ');
    bagsContained[bag] ? bagsContained[bag].add(left) : bagsContained[bag] = new Set([left]);
    bagsContaining[left][bag] = Number(count);
  }
}

const tested = new Set([...bagsContained[testName]]);
const bagsToTest = [];

while(bagsToTest.length > 0) {
  const bag = bagsToTest[0];
  tested.add(bag);
  bagsToTest.splice(0, 1);

  if (bagsContained[bag]) {
    for (const b of [...bagsContained[bag]]) {
      if (!tested.has(b) && !bagsToTest.includes(b)) {
        bagsToTest.push(b);
      }
    }
  }
}

const nOfBags = (name) => {
  let sum = 1;
  for (const k in bagsContaining[name]) {
    sum += bagsContaining[name][k] * nOfBags(k);
  }
  return sum;
}

console.log(tested.size);
console.log(nOfBags(testName) - 1)
