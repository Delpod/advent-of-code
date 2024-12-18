# Setup
file = open('adv18.txt', 'r')
lines: list[str] = file.read().splitlines()

start = (0,0)
end = (70,70)
stops = []
bits = 1024

for line in lines[:bits]:
    x, y = [int(n) for n in line.split(',')]
    stops.append((y, x))

def find_best_paths() -> int:
    paths = [[start]]
    smallest_prices = {}
    best_path = []

    def check_cell(path: list[tuple[int]], cell: tuple[int]):
        if cell not in stops and cell not in path:
            pathc = path[::]
            pathc.append(cell)
            price = len(pathc)
            if cell not in smallest_prices or price < smallest_prices[cell]:
                smallest_prices[cell] = price
                new_paths.append(pathc)
                if cell == end:
                    best_path.clear()
                    best_path.extend(pathc)
                    
    while len(paths) > 0:
        new_paths = []
        for path in paths:
            last_cell = path[-1]

            if last_cell[0] - 1 >= 0:
                check_cell(path, (last_cell[0] - 1, last_cell[1]))
            if last_cell[0] + 1 <= end[0]:
                check_cell(path, (last_cell[0] + 1, last_cell[1]))
            if last_cell[1] - 1 >= 0:
                check_cell(path, (last_cell[0], last_cell[1] - 1))
            if last_cell[1] + 1 <= end[1]:
                check_cell(path, (last_cell[0], last_cell[1] + 1))

        paths = new_paths
    
    return smallest_prices[end] if end in smallest_prices else -1

result_p1 = find_best_paths()

path_found = True
while path_found:
    x, y = [int(n) for n in lines[bits].split(',')]
    stops.append((y, x))

    if find_best_paths() < 0:
        break

    bits += 1

result_p2 = lines[bits]

print(f"Part 1: {result_p1 - 1}")
print(f"Part 2: {result_p2}")
