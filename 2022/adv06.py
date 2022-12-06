# Setup
file = open('adv06.txt', 'r')
line = file.readline()

def detect(chars):
	for i in range(chars, len(line)):
		if len(set([*line[i-chars:i]])) == chars:
			return i

# Part 1 & 2
print(f'Part 1: {detect(4)}')
print(f'Part 2: {detect(14)}')