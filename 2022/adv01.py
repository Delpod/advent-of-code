# Setup
file = open("adv01.txt", "r")
lines = file.readlines()
lines.append('')

# Part 1, 2
currentCount = 0
elfCounts = []
for line in lines:
	if line.strip() == '':
		elfCounts.append(currentCount)
		currentCount = 0
	else:
		currentCount += int(line)

elfCounts = sorted(elfCounts)

print(f"Part 1: {elfCounts[-1]}")
print(f"Part 2: {sum(elfCounts[-3:])}")