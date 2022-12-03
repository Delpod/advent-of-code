# Setup
file = open("adv03.txt", "r")
lines = [l.strip() for l in file.readlines()]

def get_value(item):
	if item >= 'a' and item <= 'z':
		return ord(item) - ord('a') + 1 
	else:
		return ord(item) - ord('A') + 27

# Part 1
count = 0
for line in lines:
	len_div = int(len(line)/2)
	p1 = set([*line[:len_div]])
	p2 = set([*line[len_div:]])
	for item in p1:
		if item in p2:
			count += get_value(item)
			break

print(f"Part 1: {count}")

# Part 2:
count = 0
for i in range(0, len(lines), 3):
	line1 = [*lines[i]]
	line2 = [*lines[i+1]]
	line3 = [*lines[i+2]]
	for item in line1:
		if item in line2 and item in line3:
			count += get_value(item)
			break

print(f"Part 2: {count}")