const fs = require('fs');

const file = fs.readFileSync('./day04_input');
const lines = file.toString().split('\n');

let validPassports1 = 0;
let validPassports2 = 0;

const fieldSet1 = new Set();
const fieldSet2 = new Set();

for (const line of lines) {
  if (line === '') {
    validPassports1 += Number(fieldSet1.size === 7);
    validPassports2 += Number(fieldSet2.size === 7);
    fieldSet1.clear();
    fieldSet2.clear();
    continue;
  }

  const fields = line.split(' ');
  for (const field of fields) {
    const [fieldName] = field.split(':');
  
    if (fieldName === 'cid') {
      continue;
    }

    fieldSet1.add(fieldName);

    if ((field.match(/^byr:(19[2-8][0-9]|199[0-9]|200[0-2])$/)) // Could be done in one line but that way it's prettier
      || (field.match(/^iyr:20(1[0-9]|20)$/))
      || (field.match(/^eyr:20(2[0-9]|30)$/))
      || (field.match(/^hgt:(((59|6[0-9]|7[0-6])in)|((1[5-8][0-9]|19[0-3])cm))$/))
      || (field.match(/^hcl:#[a-fA-F0-9]{6}$/))
      || (field.match(/^ecl:(amb|blu|brn|gry|grn|hzl|oth)$/))
      || (field.match(/^pid:\d{9}$/)))
    {
      fieldSet2.add(fieldName);
    }
  }
}

console.log(validPassports1);
console.log(validPassports2);
