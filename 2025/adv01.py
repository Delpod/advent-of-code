# Setup
import math
file = open('adv01.txt', 'r')
lines = file.read().splitlines()

dial = 50
sum_p1 = 0
sum_p2 = 0

for line in lines:
    old_dial = dial
    turn = line[0]
    amount = int(line[1:])
    
    sign = -1 if turn == 'L' else 1
    add_value = (amount % 100) * sign

    sum_p2 += amount // 100

    dial += add_value

    if old_dial != 0 and dial <= 0 or dial >= 100:
        sum_p2 += 1

    dial %= 100

    if dial == 0:
        sum_p1 += 1

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
