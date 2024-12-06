# Setup
file = open('adv06.txt', 'r')
lines = [l.strip() for l in file.readlines()]

x_start, y_start = None, None
print_enabled = True

for i in range(len(lines)):
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            y_start, x_start = (i, j)
            break

def check_guard_path(check_lines):
    x, y = x_start, y_start
    x_mov, y_mov = 0, -1
    distinct_tiles = set()
    moves = {}

    while True:
        distinct_tiles.add((x, y))

        new_x = x + x_mov
        new_y = y + y_mov
        
        if new_x < 0 or new_x >= len(check_lines[0]) or new_y < 0 or new_y >= len(check_lines):
            return True, len(distinct_tiles)

        if check_lines[new_y][new_x] == "#":
            if x_mov != 0:
                y_mov = x_mov
                x_mov = 0
            elif y_mov != 0:
                x_mov = -y_mov
                y_mov = 0

            move = (x, y, x_mov, y_mov)

            if move not in moves:
                moves[move] = True
            else:
                return False, len(distinct_tiles)

            continue

        x, y = new_x, new_y

        if print_enabled:
            for i in range(len(check_lines) + 1):
                print("\r\033[A", end='')

            for i in range(len(check_lines)):
                line = ""
                for j in range(len(check_lines[i])):
                    if (y, x) == (i, j):
                        line += "\033[92mO\033[00m"
                    elif (j, i) in distinct_tiles:
                        line += "\033[93mX\033[00m"
                    elif check_lines[i][j] != ".":
                        line += check_lines[i][j]
                    else:
                        line += " " 
                print(line)
            print(f"x = {x}, y = {y}        ")


# Part 1
_, result_p1 = check_guard_path(lines)

# Part 2
result_p2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '.':
            lines[i][j] = '#'
            did_get_out, _ = check_guard_path(lines)
            lines[i][j] = '.'
            
            if not did_get_out:
                result_p2 += 1


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
