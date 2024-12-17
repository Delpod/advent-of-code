# Setup
import math
file = open('adv16.txt', 'r')
lines: list[str] = file.read().splitlines()

map: list[list[int]] = []
start = None
end = None

RIGHT, LEFT, UP, DOWN = 0, 1, 2, 3

for i, line in enumerate(lines):
    map.append([])
    for j, char in enumerate(line):
        map[-1].append(1 if char == '#' else 0)

        if char == "S":
            start = (j, i)
        elif char == "E":
            end = (j, i)

def get_price(path: list[tuple[int]]) -> int:
    price = 0
    side = RIGHT

    for i, cell in enumerate(path):
        if i == 0:
            continue

        if cell[0] > path[i - 1][0]:
            price += 1000 + 1 if side != DOWN else 1
            side = DOWN
        elif cell[0] < path[i - 1][0]:
            price += 1000 + 1 if side != UP else 1
            side = UP
        elif cell[1] > path[i - 1][1]:
            price += 1000 + 1 if side != RIGHT else 1
            side = RIGHT
        elif cell[1] < path[i - 1][1]:
            price += 1000 + 1  if side != LEFT else 1
            side = LEFT

    return price
    

def find_best_paths() -> int:
    paths = [[start]]
    smallest_prices_cell_side = {}
    smallest_price_end = { "value": math.inf }
    best_path_cells = set()

    def check_cell(path: list[tuple[int]], cell: tuple[int]):
        if map[cell[0]][cell[1]] == 0 and cell not in path:
            pathc = path[::]
            pathc.append(cell)
            price = get_price(pathc)
            cell_check = (cell, path[-1])
            if cell_check not in smallest_prices_cell_side or price <= smallest_prices_cell_side[cell_check]:
                smallest_prices_cell_side[cell_check] = price

                if cell == end:
                    if price < smallest_price_end["value"]:
                        smallest_price_end["value"] = price
                        best_path_cells.clear()

                    best_path_cells.update(pathc)
                else:
                    new_paths.append(pathc)
                    

    while len(paths) > 0:
        new_paths = []
        for path in paths:
            last_cell = path[-1]

            check_cell(path, (last_cell[0] - 1, last_cell[1]))
            check_cell(path, (last_cell[0] + 1, last_cell[1]))
            check_cell(path, (last_cell[0], last_cell[1] - 1))
            check_cell(path, (last_cell[0], last_cell[1] + 1))

        paths = new_paths

    return smallest_price_end["value"], len(best_path_cells)

result_p1, result_p2 = find_best_paths()

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
