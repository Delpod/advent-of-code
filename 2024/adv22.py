import math
file = open('adv22.txt', 'r')
lines: list[str] = file.read().splitlines()

result_p1 = 0
prices: list[list[int]] = []
changes: list[list[int]] = []
for line in lines:
    x = int(line)
    prices.append([])
    changes.append([])
    for i in range(2000):
        x2 = x
        x = ((x * 64) ^ x) % 16777216
        x = (int(x / 32) ^ x) % 16777216
        x = ((x * 2048) ^ x) % 16777216

        prev_price = x2 % 10
        price = x % 10
        prices[-1].append(price)
        changes[-1].append(price - prev_price)

    result_p1 += x

print(f"Part 1: {result_p1}")

occurences: dict = {}

for ci, c in enumerate(changes):
    for i in range(len(c) - 4):
        tup = (c[i], c[i+1], c[i+2], c[i+3])
        
        if tup in occurences:
            can_add = True
            for key in occurences[tup]:
                if key[0] == ci:
                    can_add = False
                    break
            if can_add:
                occurences[tup].append((ci, i + 3))
        else:
            occurences[tup] = [(ci, i + 3)]

keys = list(occurences.keys())
keys.sort(key = lambda k: len(occurences[k]), reverse=True)

result_p2 = 0
min_cells = 0
for key in keys:
    if len(occurences[key]) < min_cells:
        break

    summa = 0
    for c in occurences[key]:
        summa += prices[c[0]][c[1]]
    
    if summa > result_p2:
        result_p2 = summa
        min_cells = math.floor(result_p2 / 9)


print(f"Part 2: {result_p2}")
