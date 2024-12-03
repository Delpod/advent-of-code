# Setup
import re
file = open('adv03.txt', 'r')
line = ' '.join([l.strip() for l in file.readlines()])

result_p1 = 0
result_p2 = 0


def sum_muls(string):
    result = 0

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", string)
    for mul in muls:
        x, y = [int(n) for n in mul[4:-1].split(",")]
        result += x * y

    return result


result_p1 = sum_muls(line)

line_p2 = re.sub(r"don\'t\(\)(.*?do\(\)|.*)", " ", line)
result_p2 = sum_muls(line_p2)


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
