# Setup
import re
file = open('adv06.txt', 'r')
lines = file.read().splitlines()

sums = []
symbols = []

for s in lines[-1].replace(" ", ""):
    symbols.append(s)
    sums.append(0 if s == "+" else 1)

for i in range(len(lines) - 1):
    line = lines[i].strip()
    for j, num in enumerate(re.split(r'\s+', line)):
        #print(num)
        if symbols[j] == "*":
            sums[j] *= int(num)
        else:
            sums[j] += int(num)

sum_p1 = sum(sums)


current_symbol = None
current_sum = 0
sum_p2 = 0
for i, s in enumerate(lines[-1]):
    if s != ' ':
        sum_p2 += current_sum
        current_sum = 0 if s == '+' else 1
        current_symbol = s

    num = ''
    for j in range(len(lines) - 1):
        num += lines[j][i]

    if num.strip() != '':
        if current_symbol == '*':
            current_sum *= int(num)
        else:
            current_sum += int(num)

sum_p2 += current_sum

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
