# Setup
file = open('adv07.txt', 'r')
lines = [l.strip() for l in file.readlines()]


def get_values(array, goal, concat_op):
    if len(array) == 2:
        yield array[0] * array[1]
        yield array[0] + array[1]
        if concat_op:
            yield int(str(array[0]) + str(array[1]))
    else:
        for v in get_values(array[:-1], goal, concat_op):
            if v <= goal:
                yield v * array[-1]
                yield v + array[-1]
                if concat_op:
                    yield int(str(v) + str(array[-1]))


result_p1 = 0
result_p2 = 0
for line in lines:
    value, equation = line.split(": ")
    value = int(value)
    parts = [int(v) for v in equation.split(" ")]

    # Part 1
    for test_value in get_values(parts, value, False):
        if value == test_value:
            result_p1 += value
            break

    # Part 2
    for test_value in get_values(parts, value, True):
        if value == test_value:
            result_p2 += value
            break

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
