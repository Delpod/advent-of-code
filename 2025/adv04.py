# Setup
file = open('adv04.txt', 'r')
grid = [list(line) for line in file.read().splitlines()]


def find_rolls(remove_used):
    result = 0
    was_removed = True

    while was_removed:
        was_removed = False

        for i, row in enumerate(grid):
            y_min = max(0, i - 1)
            y_max = min(len(grid), i + 2)
            for j, cell in enumerate(row):
                if cell != '@':
                    continue

                x_min = max(0, j - 1)
                x_max = min(len(row), j + 2)
                
                count = 0

                for in_row in grid[y_min:y_max]:
                    for in_cell in in_row[x_min:x_max]:
                        if in_cell == "@":
                            count += 1

                if count < 5:
                    result += 1
                    if remove_used:
                        grid[i][j] = '.'
                        was_removed = True

    return result

sum_p1 = find_rolls(False)
sum_p2 = find_rolls(True)

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
