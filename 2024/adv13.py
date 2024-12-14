# Setup
import re
file = open('adv13.txt', 'r')
lines = file.read().splitlines()

ax, ay, bx, by, x, y = None, None, None, None, None, None

def calculate(plus_value = 0):
    result = 0

    for i, line in enumerate(lines):
        if i % 4 == 0:
            numbers = re.findall(r'\d+', line)
            ax = int(numbers[0])
            ay = int(numbers[1])
        elif i % 4 == 1:
            numbers = re.findall(r'\d+', line)
            bx = int(numbers[0])
            by = int(numbers[1])
        elif i % 4 == 2:
            numbers = re.findall(r'\d+', line)
            x = int(numbers[0]) + plus_value
            y = int(numbers[1]) + plus_value

            a = (x * (bx - by) - bx * (x - y)) / (ax * (bx - by) + bx * (ay - ax))
            b = (x - ax * a) / bx

            if int(a) == a and int(b) == b:
                result += int(a * 3 + b)

    return result

print(f"Part 1: {calculate(0)}")
print(f"Part 2: {calculate(10000000000000)}")
