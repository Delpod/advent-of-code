# Setup
file = open('adv09.txt', 'r')
lines = [l.strip() for l in file.readlines()]

# Part 1 & 2
def simulate(line_len):
    if line_len < 2:
        return

    parts = [[0, 0] for _ in range(line_len)]
    visited = set(["0-0"])

    for line in lines:
        side, value = line.split(' ')
        value = int(value)

        for i in range(value):
            if side == 'R' or side == 'L':
                parts[0][0] += 1 if side == 'R' else -1
            elif side == 'U' or side == 'D':
                parts[0][1] += 1 if side == 'U' else -1
            
            for i in range(1, line_len):
                if abs(parts[i-1][0] - parts[i][0]) <= 1 and abs(parts[i-1][1] - parts[i][1]) <= 1:
                    continue

                if parts[i-1][0] - parts[i][0]:
                    parts[i][0] += 1 if parts[i-1][0] > parts[i][0] else -1

                if parts[i-1][1] - parts[i][1]:
                    parts[i][1] += 1 if parts[i-1][1] > parts[i][1] else -1
                

            visited.add(f'{parts[-1][0]}-{parts[-1][1]}')
    return len(visited)

print(f'Part 1: {simulate(2)}')
print(f'Part 2: {simulate(10)}')
