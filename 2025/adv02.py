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
        length = len(num_str)
        half_length = int(length / 2)

        if num_str[:half_length] == num_str[half_length:]:
            sum_p1 += num
            sum_p2 += num
            continue
        
        for j in range(1, half_length + 1):
            list = re.findall(num_str[:j], num_str)
            if j * len(list) == length:
                sum_p2 += num
                break

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
