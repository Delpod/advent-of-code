# Setup
file = open('adv14.txt', 'r')
lines = [l.strip() for l in file.readlines()]

def get_occupied_and_y_min():
    full_y_max = 0
    occupied = {}
    for line in lines:
        positions = line.split(' -> ')
        for i in range(len(positions) - 1):
            x0, y0 = [int(v) for v in positions[i].split(',')]
            x1, y1 = [int(v) for v in positions[i + 1].split(',')]

            y_max = y0 if y0 > y1 else y1

            if y_max > full_y_max:
                full_y_max = y_max

            if x0 != x1:
                x_min = x0 if x0 < x1 else x1
                x_max = x0 if x0 > x1 else x1

                for x in range(x_min, x_max + 1):
                    occupied[(x, y0)] = True
            if y0 != y1:
                y_min = y0 if y0 < y1 else y1

                for y in range(y_min, y_max + 1):
                    occupied[(x0, y)] = True

    return occupied, full_y_max

start_x = 500

# Part 1

count = 0
occupied, full_y_max = get_occupied_and_y_min()
finished = False

while not finished:
    pos = (start_x, 0)
    while True:
        if pos[1] >= full_y_max:
            finished = True
            break
        
        try_pos = (pos[0], pos[1] + 1)
        if try_pos not in occupied:
            pos = try_pos
            continue
        try_pos = (pos[0] - 1, pos[1] + 1)
        if try_pos not in occupied:
            pos = try_pos
            continue
        try_pos = (pos[0] + 1, pos[1] + 1)
        if try_pos not in occupied:
            pos = try_pos
            continue

        occupied[pos] = True
        count += 1
        break

print(f'Part 1: {count}')

# Part 2

count = 0
occupied, floor_level = get_occupied_and_y_min()
floor_level += 1
finished = False

while not finished:
    pos = (start_x, 0)
    while True:
        try_pos = (pos[0], pos[1] + 1)
        if try_pos not in occupied and pos[1] != floor_level:
            pos = try_pos
            continue
        try_pos = (pos[0] - 1, pos[1] + 1)
        if try_pos not in occupied and pos[1] != floor_level:
            pos = try_pos
            continue
        try_pos = (pos[0] + 1, pos[1] + 1)
        if try_pos not in occupied and pos[1] != floor_level:
            pos = try_pos
            continue

        occupied[pos] = True
        count += 1

        if pos == (start_x, 0):
            finished = True

        break

print(f'Part 2: {count}')
