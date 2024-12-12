# Setup
file = open('adv12.txt', 'r')
lines = file.read().splitlines()

height = len(lines)
width = len(lines[0])

farms:dict[list[dict]] = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char not in farms:
            farms[char] = []

        farms_tup = [(k, farm) for k, farm in enumerate(farms[char]) if (i - 1, j) in farm["cells"] or (i, j - 1) in farm["cells"]]

        farm = None

        if len(farms_tup) == 0:
            farm = { "cells": [], "perimeters": [] }
            farms[char].append(farm)
        elif len(farms_tup) == 1:
            farm = farms_tup[0][1]
        elif len(farms_tup) == 2:
            farm = { "cells": [], "perimeters": [] }

            for f in farms_tup:
                farm["cells"] += f[1]["cells"]
                farm["perimeters"] += f[1]["perimeters"]

            farms[char].pop(farms_tup[1][0])
            farms[char].pop(farms_tup[0][0])
            farms[char].append(farm)

        perimeters = 0
        sides = 0

        if i == 0 or lines[i - 1][j] != char:
            perimeters += 1

        if i == height - 1 or lines[i + 1][j] != char:
            perimeters += 1

        if j == 0 or lines[i][j - 1] != char:
            perimeters += 1
        
        if j == width - 1 or lines[i][j + 1] != char:
            perimeters += 1

        farm["cells"].append((i, j))
        farm["perimeters"].append(perimeters)


result_p1 = 0
result_p2 = 0
for _, farmgroup in enumerate(farms.values()):
    for farm in farmgroup:
        result_p1 += len(farm["cells"]) * sum(farm["perimeters"])

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
