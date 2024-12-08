# Setup
file = open('adv02.txt', 'r')
lines = file.read().splitlines()

result_p1 = 0
result_p2 = 0

def are_levels_correct(levels):
    sign = levels[0] - levels[1]

    if sign == 0:
        return False

    sign /= abs(sign)

    for i in range(1, len(levels)):
        diff = levels[i - 1] - levels[i]
        if abs(diff) < 1 or abs(diff) > 3 or diff / sign < 0:
            return False

    return True

for report in lines:
    levels = [int(n) for n in report.split(' ')]
    are_correct = are_levels_correct(levels)

    if are_correct:
        result_p1 += 1
        result_p2 += 1
    if not are_correct:
        for i in range(len(levels)):
            if are_levels_correct(levels[:i] + levels[i+1:]):
                result_p2 += 1
                break

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
