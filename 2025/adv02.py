# Setup
import re
file = open('adv02.txt', 'r')
line = file.read().splitlines()[0]

sum_p1 = 0
sum_p2 = 0

for bounds in line.split(','):
    l_bound, r_bound = [int(x) for x in bounds.split('-')]

    for num in range(l_bound, r_bound + 1, 1):
        num_str = str(num)

        if re.match("^(\\d+)\\1$", num_str):
            sum_p1 += num
        
        if re.match("^(\\d+)\\1+$", num_str):
            sum_p2 += num

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
