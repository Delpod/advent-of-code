# Setup
file = open("adv04.txt", "r")
lines = [l.strip() for l in file.readlines()]

# Part 1
count = 0
count2 = 0
for line in lines:
	elfs = line.split(',')
	elfs = [[int(id) for id in elf.split('-')] for elf in elfs]
	if (elfs[0][0] >= elfs[1][0] and elfs[0][1] <= elfs[1][1]) or (elfs[1][0] >= elfs[0][0] and elfs[1][1] <= elfs[0][1]):
		count += 1
	if (elfs[0][0] <= elfs[1][0] and elfs[0][1] >= elfs[1][0]) or (elfs[1][0] <= elfs[0][0] and elfs[1][1] >= elfs[0][0]):
		count2 += 1

print(f"Part 1: {count}")
print(f"Part 2: {count2}")