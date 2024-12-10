# Setup
file = open('adv10.txt', 'r')
lines: list[str] = file.read().splitlines()

trail_map: list[list[int]] = []

for line in lines:
    trail_map.append([-1 if x == '.' else int(x) for x in line])

height = len(trail_map)
width = len(trail_map[0])

def find_paths(search_value: int, path: list[tuple[int]], ends: set[tuple[int]]) -> int:
    last_cell = path[-1]

    if search_value >= 10:
        ends.add(last_cell)
        return 1
        
    cell_before = None if len(path) == 1 else path[-2]

    number_of_paths: int = 0

    def add_element_and_find_paths(new_element: tuple[int]):
        pathc = path[::]
        pathc.append(new_element)
        return find_paths(search_value + 1, pathc, ends)

    if last_cell[0] > 0 and (cell_before == None or last_cell[0] - 1 != cell_before[0]) and trail_map[last_cell[0] - 1][last_cell[1]] == search_value:
        number_of_paths += add_element_and_find_paths((last_cell[0] - 1, last_cell[1]))

    if last_cell[0] < height - 1 and (cell_before == None or last_cell[0] + 1 != cell_before[0]) and trail_map[last_cell[0] + 1][last_cell[1]] == search_value:
        number_of_paths += add_element_and_find_paths((last_cell[0] + 1, last_cell[1]))

    if last_cell[1] > 0 and (cell_before == None or last_cell[1] - 1 != cell_before[1]) and trail_map[last_cell[0]][last_cell[1] - 1] == search_value:
        number_of_paths += add_element_and_find_paths((last_cell[0], last_cell[1] - 1))

    if last_cell[1] < width - 1 and (cell_before == None or last_cell[1] + 1 != cell_before[1]) and trail_map[last_cell[0]][last_cell[1] + 1] == search_value:
        number_of_paths += add_element_and_find_paths((last_cell[0], last_cell[1] + 1))
    
    return number_of_paths


result_p1: int = 0
result_p2: int = 0

for i, row in enumerate(trail_map):
    for j, cell in enumerate(row):
        if cell == 0:
            ends = set()
            result_p2 += find_paths(1, [(i, j)], ends)
            result_p1 += len(ends)


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
