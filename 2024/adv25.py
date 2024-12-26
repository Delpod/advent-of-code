file = open('adv25.txt', 'r')
lines: list[str] = file.read().splitlines()

locks = []
keys = []

current = []

is_lock = None
for line in lines:
  if line == '':
    if is_lock == True:
      locks.append(current)
    elif is_lock == False:
      keys.append(current)

    is_lock = None
    continue
  
  if is_lock == None:
    is_lock = line[0] == '#'
    current = [-1] * len(line)

  for i, c in enumerate(line):
    if c == '#':
      current[i] += 1

result_p1 = 0
for lock in locks:
  for key in keys:
    if all(lock[i] + key[i] <= 5 for i in range(len(key))):
      result_p1 += 1

print(f'Part 1: {result_p1}')