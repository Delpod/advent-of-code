from functools import cache
file = open('adv21.txt', 'r')
lines: list[str] = file.read().splitlines()

numeric = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}
directional = {
                 '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}

@cache
def dir_to_numeric(cur: str, new: str):
    result = ''
    c = numeric[cur]
    n = numeric[new]

    if c[0] == 3 and n[1] == 0:
        if c[0] > n[0]:
            result += '^' * (c[0] - n[0])
    else:
        if c[0] < n[0]:
            result += 'v' * (n[0] - c[0])

    if c[1] < n[1]:
        result += '>' * (n[1] - c[1])
    elif c[1] > n[1]:
        result += '<' * (c[1] - n[1])

    if c[0] == 3 and n[1] == 0:
        if c[0] < n[0]:
            result += 'v' * (n[0] - c[0])
    else:
        if c[0] > n[0]:
            result += '^' * (c[0] - n[0])

    result += 'A'

    return result

@cache
def dir_to_dir(cur: str, new: str):
    result = ''

    c = directional[cur]
    n = directional[new]

    if c[0] < n[0]:
        result += 'v' * (n[0] - c[0])

    if c[1] < n[1]:
        result += '>' * (n[1] - c[1])
    elif c[1] > n[1]:
        result += '<' * (c[1] - n[1])

    if c[0] > n[0]:
        result += '^' * (c[0] - n[0])

    result += 'A'

    return result

robots_cur = {}
lenr2 = 0
lenr25 = 0
def resolve_robot(cur, max, input):
    global lenr2, lenr25
    if cur > max:
        return

    if cur not in robots_cur:
        robots_cur[cur] = 'A'

    for c in input:
        result = dir_to_dir(robots_cur[cur], c)
        resolve_robot(cur + 1, max, result)

        robots_cur[cur] = c

        if cur == 2:
            lenr2 += len(result)
        elif cur == 25:
            lenr25 += len(result)


num_cur = 'A'

result_p1 = 0
result_p2 = 0
for line in lines:
    print('\n', line)
    val = int(line[:3])

    for c in line:
        print(c)
        robots_cur.clear()
        result = dir_to_numeric(num_cur, c)
        resolve_robot(1, 25, result)

        num_cur = c

    result_p1 += lenr2 * val
    result_p2 += lenr25
    lenr2 = 0
    lenr25 = 0

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")