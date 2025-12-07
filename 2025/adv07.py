# Setup
from functools import cache
file = open('adv07.txt', 'r')
lines = file.read().splitlines()

sum_p1 = 0
sum_p2 = 0

start_ray = None
for i, s in enumerate(lines[0]):
    if s == 'S':
        start_ray = i
        break

rays = {start_ray}

for i in range(1, len(lines)):
    line = lines[i]
    new_rays = set()
    rays_to_remove = set()
    new_rays2 = []
    for r in rays:
        if line[r] == '^':
            rays_to_remove.add(r)
            new_rays.add(r-1)
            new_rays.add(r+1)
            sum_p1 += 1

    rays = (rays - rays_to_remove) | new_rays

@cache
def p2(line_index, ray_pos):
    if line_index == len(lines) - 1:
        return 1

    if lines[line_index][ray_pos] == '^':
        return p2(line_index + 1, ray_pos - 1) + p2(line_index + 1, ray_pos + 1)
    else:
        return p2(line_index + 1, ray_pos)

sum_p2 = p2(1, start_ray)

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
