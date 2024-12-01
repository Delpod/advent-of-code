# Setup
file = open('adv17.txt', 'r')
line = file.readline().strip()

rocks = [
    [[True, True, True, True]],
    [[False, True, False],
    [True, True, True],
    [False, True, False]],
    [[True, True, True], 
    [False, False, True],
    [False, False, True]],
    [[True],
    [True],
    [True],
    [True]],
    [[True, True],
    [True, True]]
]

rocks_left_right_indexes = [
    [[0, 3]],
    [[1, 1], [0, 2], [1, 1]],
    [[0, 2], [2, 2], [2, 2]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 1], [0, 1]]
]

line_index = 0
rock_index = 0
number_of_rocks = 3

tower = []

for i in range(number_of_rocks):
    rock = rocks[rock_index]
    rock_index = rock_index + 1 if rock_index < len(rocks) - 1 else 0
    x_pos = 2
    x_min = 0
    x_max = 7 - len(rock[0])
    y_pos = len(tower) + 2 + len(rock)
    rock_stopped = False
    gas_pushing = True
    tower_y = y_pos - len(rock)

    while not rock_stopped:
        if gas_pushing:
            if line[line_index] == '<':
                block_movement = False
                for r, row in enumerate(rock):
                    print(len(tower))
                    print(tower_y - r)
                    if len(tower) >= (tower_y - r) and x_min <= x_pos - 1 - rocks_left_right_indexes[rock_index][r][0] and tower[tower_y - r - 1][x_pos - 1 + rocks_left_right_indexes[rock_index][r][0]]:
                        block_movement = True
                if not block_movement:
                    x_pos = max(x_pos - 1, 0)
            else:
                block_movement = False
                for r, row in enumerate(rock):
                    if len(tower) >= (tower_y - r) and x_max >= x_pos + 1 + rocks_left_right_indexes[rock_index][r][1] and tower[tower_y - r - 1][x_pos + 1 + rocks_left_right_indexes[rock_index][r][1]]:
                        block_movement = True
                            
                if not block_movement:
                    x_pos = min(x_pos + 1, x_max)

            if len(tower) > tower_y:
                print(rock[tower_y])

            line_index = line_index + 1 if line_index < len(line) - 1 else 0
            gas_pushing = False
        else:
            for r, row in enumerate(rock):
                if rock_stopped:
                    break

                tower_y = y_pos - r

                for c, cell in enumerate(row):
                    if cell == False:
                        continue

                    if len(tower) >= tower_y and (tower_y == 0 or tower[tower_y - 1][x_pos + cell]):
                        rock_stopped = True
                        break

            if rock_stopped:
                for r in range(0, len(rock)):
                    if len(tower) <= tower_y:
                        tower.append([False, False, False, False, False, False, False])

                    for c, cell in enumerate(rock[r]):
                        if cell:
                            tower[tower_y][x_pos + c] = True

                    tower_y += 1
            else:
                y_pos -= 1
                gas_pushing = True
    for t in range(-1, -len(tower)-1, -1):
        print(''.join(['#' if c else '.' for c in tower[t]]))
    print('')
