# Setup
file = open('adv20.txt', 'r')
lines: list[str] = file.read().splitlines()

map: list[list[int]] = []
start = None
end = None
cheats = set()
tested_cheats = set()

NOTHING, WALL = 0, 1

for i, line in enumerate(lines):
    map.append([])
    for j, char in enumerate(line):
        map[-1].append(WALL if char == '#' else NOTHING)

        if char == "S":
            start = (j, i)
        elif char == "E":
            end = (j, i)

width = len(map[0])
height = len(map)

def get_path() -> int:
    positions = [start]
    costs = { start: 0 }

    def check_cell(last_cell: tuple[int], cell: tuple[int]):
        if map[cell[1]][cell[0]] == NOTHING and cell not in positions:
            positions.append(cell)
            costs[cell] = costs[last_cell] + 1
            return True
        return False
                    
    while True:
        last_cell = positions[-1]

        if last_cell[0] - 1 >= 1         and check_cell(last_cell, (last_cell[0] - 1, last_cell[1])):
            continue
        if last_cell[0] + 1 < height - 1 and check_cell(last_cell, (last_cell[0] + 1, last_cell[1])):
            continue
        if last_cell[1] - 1 >= 1         and check_cell(last_cell, (last_cell[0], last_cell[1] - 1)):
            continue
        if last_cell[1] + 1 < width - 1  and check_cell(last_cell, (last_cell[0], last_cell[1] + 1)):
            continue

        break
    
    return positions, costs

positions, costs = get_path()

result_p1 = 0
result_p2 = 0
lenght = len(positions)
for i, p1 in enumerate(positions):
    # print(i / lenght)
    for p2 in positions:
        if p1 == p2:
            continue

        diff = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        if diff > 20:
            continue

        if (costs[p2] - costs[p1] - diff) >= 100:
            if diff <= 2:
                result_p1 += 1
            if diff <= 20:
                result_p2 += 1

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
