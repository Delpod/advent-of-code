# Setup
import math
file = open('adv10.txt', 'r')
lines = [l.strip() for l in file.readlines()]

# Part 1 & 2

max_cycle = 240
row_length = 40
drawing = [[] for _ in range(math.ceil((max_cycle/row_length)))]

reg = 1
cycle = 1
sum = 0

for line in lines:
    cycles_now = 1 if line == 'noop' else 2
    
    for _ in range(cycles_now):
        pos = (cycle - 1) % row_length + 1
        row = int((cycle - 1) / row_length)
        drawing[row].append('#' if pos >= reg and pos < reg + 3 else '.')

        if cycle % (row_length / 2) == 0 and cycle % row_length != 0:
            sum += cycle * reg

        cycle += 1
    
    if line.startswith('addx'):
        _, value = line.split(' ')
        reg += int(value)

    if cycle > max_cycle:
        break

drawing = '\n'.join([''.join(row) for row in drawing])

print(f'Part 1: {sum}')
print(f'Part 2:\n{drawing}')
