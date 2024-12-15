# Setup
file = open('adv15.txt', 'r')
lines = file.read().splitlines()

NOTHING, WALL, BOX, LBOX, RBOX = 0, 1, 2, 3, 4
characters = { NOTHING: '.', WALL: '#', BOX: 'O', LBOX: '[', RBOX: ']' }

rx, ry = None, None
map = []
instructions = ''

def x_move(value):
    global rx, ry
    if map[ry][rx + value] == NOTHING:
        rx += value
    elif map[ry][rx + value] == WALL:
        pass
    else:
        x = rx + value
        while map[ry][x] >= BOX:
            x += value
        
        if map[ry][x] == NOTHING:
            while x != rx:
                map[ry][x] = map[ry][x - value]
                x -= value
                
            rx += value

def y_move(value):
    global rx, ry
    if map[ry + value][rx] == NOTHING:
        ry += value
    elif map[ry + value][rx] != WALL:
        y = ry + value
        cell = map[y][rx]
        check = [(y, rx, NOTHING)]
        move = []
        if cell == LBOX:
            check.append((y, rx + 1, NOTHING))
        elif cell == RBOX:
            check.append((y, rx - 1, NOTHING))

        while len(check) > 0:
            cell = map[check[0][0]][check[0][1]]
            if cell == NOTHING:
                move.append(check.pop(0))
                continue
            if cell == WALL:
                break
            else:
                if cell == LBOX:
                    right = (check[0][0], check[0][1] + 1, NOTHING)
                    if right not in check and right not in move:
                        check.append(right)
                elif cell == RBOX:
                    left = (check[0][0], check[0][1] - 1, NOTHING)
                    if left not in check and left not in move:
                        check.append(left)

                above = (check[0][0] + value, check[0][1], cell)
                if above not in check and above not in move:
                    check.append(above)

                move.append(check.pop(0))
        
        if len(check) == 0:
            while len(move) > 0:
                y, x, tile = move.pop()
                map[y][x] = tile

            ry += value

def calculate() -> int:
    global rx, ry, map, instructions, characters
    for i in instructions:
        if i == '<':
            x_move(-1)
        elif i == '>':
            x_move(1)
        elif i == '^':
            y_move(-1)
        else:
            y_move(1)

    result = 0
    for i, line in enumerate(map):
        for j, cell in enumerate(line):
            if j == rx and i == ry:
                print('@', end='')
            else:
                print(characters[cell], end='')

            if cell == BOX:
                result += i * 100 + j
            elif cell == LBOX:
                result += i * 100 + j
        print('')

    print('\n')
    return result


reading_map = True
for i, line in enumerate(lines):
    if line == '':
        reading_map = False
    elif reading_map:
        map.append([])
        for j, char in enumerate(line):
            if char == '#':
                map[-1].append(WALL)
            elif char == 'O':
                map[-1].append(BOX)
            else:
                map[-1].append(NOTHING)

            if char == '@':
                rx, ry = j, i
    else:
        instructions += line

result_p1 = calculate()

map.clear()
for i, line in enumerate(lines):
    if line == '':
        break

    map.append([])
    for j, char in enumerate(line):
        if char == '#':
            map[-1].append(WALL)
            map[-1].append(WALL)
        elif char == 'O':
            map[-1].append(LBOX)
            map[-1].append(RBOX)
        else:
            map[-1].append(NOTHING)
            map[-1].append(NOTHING)

        if char == '@':
            rx, ry = j * 2, i

result_p2 = calculate()


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")