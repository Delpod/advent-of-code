from functools import cache
from itertools import permutations
from math import inf
file = open('adv21.txt', 'r')
lines: list[str] = file.read().splitlines()


numeric = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2),
}

directions = {
    ('A', 'A'): 'A',
    ('^', '^'): 'A',
    ('>', '>'): 'A',
    ('v', 'v'): 'A',
    ('<', '<'): 'A',
    ('A', '^'): '<A',
    ('^', 'A'): '>A',
    ('A', '>'): 'vA',
    ('>', 'A'): '^A',
    ('v', '^'): '^A',
    ('^', 'v'): 'vA',
    ('v', '<'): '<A',
    ('<', 'v'): '>A',
    ('v', '>'): '>A',
    ('>', 'v'): '<A',
    ('A', 'v'): '<vA',
    ('v', 'A'): '^>A',
    ('A', '<'): 'v<<A',
    ('<', 'A'): '>>^A',
    ('>', '<'): '<<A',
    ('<', '>'): '>>A',
    ('<', '^'): '>^A',
    ('^', '<'): 'v<A',
    ('>', '^'): '<^A',
    ('^', '>'): 'v>A',
}


@cache
def resolve_robot(cur: int, max: int, input: str):
    cur_pos = 'A'

    ires = 0
    for c in input:
        result = directions[(cur_pos, c)]

        cur_pos = c
        
        if cur == max:
            ires += len(result)
        else:
            res = resolve_robot(cur + 1, max, result)
            ires += res

    return ires


@cache
def dir_to_numeric(cur: str, new: str, depth: int):
    cy, cx = numeric[cur]
    ny, nx = numeric[new]
    xdiff, ydiff = abs(cx - nx), abs(cy - ny)
    xch, ych = '<' if nx < cx else '>', '^' if ny < cy else 'v'

    start = ''
    test_input = ''
    if cy == 3 and nx == 0:
        start = '^'
        test_input += ych * (ydiff - 1) + xch * xdiff
    elif ny == 3 and cx == 0:
        start = '>'
        test_input += ych * ydiff + xch * (xdiff - 1)
    else:
        test_input += ych * ydiff + xch * xdiff

    possibles = [f"{start}{''.join(x)}A" for x in set(permutations(test_input))]

    best_result = inf
    best_input = None

    for inp in possibles:
        result = resolve_robot(0, depth, inp)
        if result < best_result:
            best_result = result
            best_input = inp

    return best_input


def solve(depth: int):
    num_cur = 'A'

    ret_value = 0
    for line in lines:
        val = int(line[:3])

        for c in line:
            result = dir_to_numeric(num_cur, c, depth)
            ret_value += resolve_robot(1, depth, result) * val

            num_cur = c

    return ret_value


result_p1 = solve(2)
result_p2 = solve(25)

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")