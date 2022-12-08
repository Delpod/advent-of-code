# Setup
file = open('adv07.txt', 'r')
lines = [l.strip() for l in file.readlines()]

# Part 1 & 2
count = 0
max_score = 0
for i, line in enumerate(lines):
	if i == 0 or i == len(lines) - 1:
		count += len(line)
		continue

	for j, letter in enumerate(line):
		if j == 0 or j == len(line) - 1:
			count += 1
			continue

		score = 1
		count_start = count

		is_visible, p_score = True, 0
		for x in range(i - 1, -1, -1):
			p_score += 1
			if lines[x][j] >= letter:
				is_visible = False
				break
		score *= p_score
		if is_visible:
			count += 1

		is_visible, p_score = True, 0
		for x in range(i + 1, len(lines)):
			p_score += 1
			if lines[x][j] >= letter:
				is_visible = False
				break
		score *= p_score
		if is_visible and count_start == count:
			count += 1

		is_visible, p_score = True, 0
		for y in range(j - 1, -1, -1):
			p_score += 1
			if lines[i][y] >= letter:
				is_visible = False
				break
		score *= p_score
		if is_visible and count_start == count:
			count += 1

		is_visible, p_score = True, 0
		for y in range(j + 1, len(line)):
			p_score += 1
			if lines[i][y] >= letter:
				is_visible = False
				break
		score *= p_score
		if is_visible and count_start == count:
			count += 1

		if score > max_score:
			max_score = score

print(f'Part 1: {count}')
print(f'Part 2: {max_score}')
