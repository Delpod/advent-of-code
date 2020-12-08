const fs = require('fs');

const file = fs.readFileSync('./day8_input');
const lines = file.toString().split('\n');

const checkLines = (lines) => {
  let acc = 0;
  let i = 0;
  const executedLines = {};

  while (i < lines.length) {
    if (executedLines[i]) {
      break;
    }

    const [inst, val] = lines[i].split(' ');

    if (inst === 'nop') {
      executedLines[i++] = true;
    } else if (inst === 'acc') {
      executedLines[i++] = true;
      acc += Number(val);
    } else if (inst === 'jmp') {
      executedLines[i] = true;
      i += Number(val);
    }
  }

  return { acc, i, executedLines };
}

const { executedLines, acc } = checkLines(lines);

console.log(acc);

for (const k in executedLines) {
  const [inst, val] = lines[k].split(' ');

  if (inst !== 'acc') {
    lines[k] = `${inst === 'jmp' ? 'nop' : 'jmp'} ${val}`;
    const { acc, i } = checkLines(lines);

    if (i >= lines.length) {
      console.log(acc);
      break;
    }

    lines[k] = `${inst} ${val}`;
  }
}
