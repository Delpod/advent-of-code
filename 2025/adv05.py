# Setup
file = open('adv05.txt', 'r')
lines = file.read().splitlines()


sum_p1 = 0
sum_p2 = 0

bounds = []

def merge_bounds():
    i = 0
    while i < len(bounds):
        b1 = bounds[i]
        for b2_i, b2 in enumerate(bounds):
            if b1 is not b2 and ((b1[0] >= b2[0] and b1[0] <= b2[1]) or (b1[1] <= b2[0] and b1[1] >= b2[1])):
                b1[0] = min(b1[0], b2[0])
                b1[1] = max(b1[1], b2[1])
                bounds.pop(b2_i)
                i = 0
                break
        i += 1


read_bounds = True
bounds_merged = False
for line in lines:
    if line == "":
        read_bounds = False
        continue

    if read_bounds:
        bounds.append([int(x) for x in line.split('-')])
    else:
        if not bounds_merged:
            merge_bounds()
            bounds_merged = True

        num = int(line)
        for bound in bounds:
            if num >= bound[0] and num <= bound[1]:
                sum_p1 += 1
                break

for bound in bounds:
    sum_p2 += bound[1] - bound[0] + 1

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
