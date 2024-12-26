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
        count = len(farm["cells"])
        result_p1 += count * sum(farm["perimeters"])
        min_i, min_j = farm["cells"][0]
        max_i, max_j = farm["cells"][0]

        for cell in farm["cells"]:
            if cell[0] < min_i:
                min_i = cell[0]
            elif cell[0] > max_i:
                max_i = cell[0]

            if cell[1] < min_j:
                min_j = cell[1]
            elif cell[1] > max_j:
                max_j = cell[1]

        if min_i == max_i or min_j == max_j:
            result_p2 += count * 4 # 4 sides
        else:
            for i in range(min_i, max_i + 1):
                is_on_top_edge = False
                is_on_bottom_edge = False
                is_on_left_edge = False
                for j in range(min_j, max_j + 1):
                    if (i, j) in farm["cells"]:
                        if not is_on_top_edge and (i == 0 or (i - 1, j) not in farm["cells"]):
                            result_p2 += count
                            is_on_top_edge = True
                        elif (i - 1, j) in farm["cells"]:
                            is_on_top_edge = False
                    else:
                        is_on_top_edge = False

                    if (i, j) in farm["cells"]:
                        if not is_on_bottom_edge and (i == height - 1 or (i + 1, j) not in farm["cells"]):
                            result_p2 += count
                            is_on_bottom_edge = True
                        elif (i + 1, j) in farm["cells"]:
                            is_on_bottom_edge = False
                    else:
                        is_on_bottom_edge = False

            for j in range(min_j, max_j + 1):
                is_on_left_edge = False
                is_on_right_edge = False
                for i in range(min_i, max_i + 1):
                    if (i, j) in farm["cells"]:
                        if not is_on_left_edge and (j == 0 or (i, j - 1) not in farm["cells"]):
                            result_p2 += count
                            is_on_left_edge = True
                        elif (i, j - 1) in farm["cells"]:
                            is_on_left_edge = False
                    else:
                        is_on_left_edge = False

                    if (i, j) in farm["cells"]:
                        if not is_on_right_edge and (j == width - 1 or (i, j + 1) not in farm["cells"]):
                            result_p2 += count
                            is_on_right_edge = True
                        elif (i, j + 1) in farm["cells"]:
                            is_on_right_edge = False
                    else:
                        is_on_right_edge = False



print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
