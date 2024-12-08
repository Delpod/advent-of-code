# Setup
from collections import Counter
file = open('adv01.txt', 'r')
lines = file.read().splitlines()

left_orig = []
left = []
right = []
right_counted = {}

for line in lines:
    l, r = [int(n) for n in line.split('   ')]
    left.append(l)
    right.append(r)

right_counted = Counter(right)
left_orig = left.copy()
left.sort()
right.sort()

sum_p1 = 0
sum_p2 = 0

for i in range(len(left)):
    sum_p1 += abs(left[i] - right[i])
    sum_p2 += left_orig[i] * right_counted[left_orig[i]]

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
