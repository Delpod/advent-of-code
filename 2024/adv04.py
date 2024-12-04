# Setup
import re
file = open('adv04.txt', 'r')
lines = [l.strip() for l in file.readlines()]

result_p1 = 0
result_p2 = 0

word1 = "XMAS"
word1_reversed = word1[::-1]
len1 = len(word1)

word2 = "MAS"
word2_reversed = word2[::-1]
len2 = len(word2)


# Part 1
for i in range(len(lines)):
    result_p1 += len(re.findall(word1, lines[i])) + len(re.findall(word1_reversed, lines[i]))
    
    if i <= len(lines) - len1:
        for j in range(len(lines[i]) - len1 + 1):
            check = ""
            for k in range(len1):
                check += lines[i + k][j + k]
            
            if check == word1 or check == word1_reversed:
                result_p1 += 1

    if i >= len1 - 1:
        for j in range(len(lines[i]) - len1 + 1):
            check = ""
            for k in range(len1):
                check += lines[i - k][j + k]

            if check == word1 or check == word1_reversed:
                result_p1 += 1


for i in range(len(lines[0])):
    line = ""
    for l in lines:
        line += l[i]

    result_p1 += len(re.findall(word1, line)) + len(re.findall(word1_reversed, line))


# Part 2
for i in range(len(lines) - len2 + 1):
    for j in range(len(lines[i]) - len2 + 1):
        check = ""

        for k in range(len2):
            check += lines[i + k][j + k]
        
        if check != word2 and check != word2_reversed:
            continue

        check = ""
        for k in range(len2):
            check += lines[i - k + 2][j + k]

        if check == word2 or check == word2_reversed:
            result_p2 += 1


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
