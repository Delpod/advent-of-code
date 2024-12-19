# Setup
from functools import cache
file = open('adv19.txt', 'r')
lines: list[str] = file.read().splitlines()

towels = set(lines[0].split(', '))
patterns = []

@cache
def get_valid_count(word):    
    if not word:
        return 1
    
    count = 0
    for i in range(1, len(word) + 1):
        w1 = word[:i]
        w2 = word[i:]
        
        if w1 in towels:
            count += get_valid_count(w2)       
    
    return count

result_p1 = 0
result_p2 = 0
for i, line in enumerate(lines[2:]):
    count = get_valid_count(line)
    if count > 0:
        result_p1 += 1
        result_p2 += count

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
