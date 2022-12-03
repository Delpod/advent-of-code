# Setup
file = open("adv02.txt", "r")
lines = file.readlines()
scores = {"A X": 1+3, "B X": 1+0, "C X": 1+6, "A Y": 2+6, "B Y": 2+3, "C Y": 2+0, "A Z": 3+0, "B Z": 3+6, "C Z": 3+3}
scores2 = {"A X": 3+0, "B X": 1+0, "C X": 2+0, "A Y": 1+3, "B Y": 2+3, "C Y": 3+3, "A Z": 2+6, "B Z": 3+6, "C Z": 1+6}

# Part 1

count = 0
count2 = 0
for line in lines:
	count += int(scores[line.strip()])
	count2 += int(scores2[line.strip()])

print(f"Part 1: {count}")
print(f"Part 2: {count2}")