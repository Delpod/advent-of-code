# Setup
import re
import copy
file = open('adv05.txt', 'r')
lines = file.readlines()

# Part 1 & 2
towers = []
towers2 = None

for line in lines:
	if '[' in line:
		for i in range(1, len(line), 4):
			if len(towers) < i/4:
				towers.append([])
			if line[i] != ' ':
				towers[int((i-1)/4)].append(line[i])

	elif 'move' in line:
		if towers2 is None:
			towers2 = copy.deepcopy(towers)

		_count, _from, _to = [int(n) for n in re.findall(r'\d+', line)]
		_from -= 1
		_to -= 1

		towers[_to] = towers[_from][:_count][::-1] + towers[_to]
		towers2[_to] = towers2[_from][:_count] + towers2[_to]

		towers[_from] = towers[_from][_count:]
		towers2[_from] = towers2[_from][_count:]

p1 = ''.join([t[0] for t in towers])
p2 = ''.join([t[0] for t in towers2])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
