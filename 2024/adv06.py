# Setup
file = open('adv06.txt', 'r')
lines = file.read().splitlines()

size = len(lines)
x_start, y_start = None, None
print_enabled = False

for i in range(size):
    line = []
    for j in range(size):
        if lines[i][j] == "^":
            y_start, x_start = (i, j)
        
        line.append(lines[i][j] == '#')
    lines[i] = line


def check_guard_path():
    x, y = x_start, y_start
    x_mov, y_mov = 0, -1
    distinct_tiles = set()
    moves = {}

    while True:
        distinct_tiles.add((x, y))

        x += x_mov
        y += y_mov
        
        if x < 0 or x >= size or y < 0 or y >= size:
            return True, distinct_tiles

        if lines[y][x]:
            x -= x_mov
            y -= y_mov

            if x_mov != 0:
                y_mov = x_mov
                x_mov = 0
            elif y_mov != 0:
                x_mov = -y_mov
                y_mov = 0

            move = (x, y, x_mov, y_mov)

            if move in moves:
                return False, distinct_tiles

            moves[move] = True
            continue

        if print_enabled:
            for i in range(size + 1):
                print("\r\033[A", end='')

            for i in range(size):
                line = ""
                for j in range(size):
                    if (y, x) == (i, j):
                        line += "\033[92mO\033[00m"
                    elif (j, i) in distinct_tiles:
                        line += "\033[93mX\033[00m"
                    elif lines[i][j]:
                        line += '#'
                    else:
                        line += " " 
                print(line)
            print(f"x = {x}, y = {y}    ")


# Part 1
_, distinct_tiles = check_guard_path()
result_p1 = len(distinct_tiles)

# Part 2
result_p2 = 0
for j, i in distinct_tiles:
    lines[i][j] = True
    did_get_out, _ = check_guard_path()
    lines[i][j] = False
    
    if not did_get_out:
        result_p2 += 1

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
