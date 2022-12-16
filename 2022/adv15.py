# Setup
import re
file = open('adv15.txt', 'r')
lines = [l.strip() for l in file.readlines()]

search_value = 2000000
x_values = []
beacons = set()

for line in lines:
    values = [int(v) for v in re.findall('-?\d+', line)]
    sensor = values[:2]
    beacon = values[2:]
    manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    look_x = search_value + manhattan - sensor[1] if sensor[1] > search_value else sensor[1] + manhattan - search_value
    if beacon[1] == search_value:
        beacons.add(beacon[0])
    if look_x >= 0:
        x_values.append({ 'min': sensor[0] - look_x, 'max': sensor[0] + look_x })

x_values.sort(key=lambda x: x['min'])

i = 0
while i < len(x_values) - 1:
    if x_values[i + 1]['max'] < x_values[i]['max']:
        x_values.pop(i + 1)    
        continue

    if x_values[i + 1]['max'] >= x_values[i]['max'] and x_values[i + 1]['min'] <= x_values[i]['max'] + 1:
        x_values[i]['max'] = x_values[i + 1]['max']
        x_values.pop(i + 1)
        continue

    if x_values[i + 1]['min'] > x_values[i]['max']:
        i += 1
        continue

sum = 1
for x in x_values:
    sum += x['max'] - x['min']

print(f'Part 1: {sum - len(beacons)}')

# Part 2

min_v = 0
max_v = 4000000
x_values = []
beacons = set()
x, y = None, None

for it in range(min_v, max_v + 1):
    x_values.clear()
    beacons.clear()

    for line in lines:
        values = [int(v) for v in re.findall('-?\d+', line)]
        sensor = values[:2]
        beacon = values[2:]
        manhattan = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        look_x = it + manhattan - sensor[1] if sensor[1] > it else sensor[1] + manhattan - it
        if beacon[1] == search_value:
            beacons.add(beacon[0])
        if look_x >= 0:
            x_values.append({ 'min': max(0, sensor[0] - look_x), 'max': min(4000000, sensor[0] + look_x) })
    
    x_values.sort(key=lambda x: x['min'])

    i = 0
    while i < len(x_values) - 1:
        if x_values[i + 1]['max'] < x_values[i]['max']:
            x_values.pop(i + 1)    
            continue

        if x_values[i + 1]['max'] >= x_values[i]['max'] and x_values[i + 1]['min'] <= x_values[i]['max'] + 1:
            x_values[i]['max'] = x_values[i + 1]['max']
            x_values.pop(i + 1)
            continue

        if x_values[i + 1]['min'] > x_values[i]['max']:
            i += 1
            continue

    if len(x_values) > 1:
        y = it
        break
    if it % 100000 == 0:
        print(it)

x = x_values[0]['max'] + 1

print(f'Part 2: {x * 4000000 + y}')
