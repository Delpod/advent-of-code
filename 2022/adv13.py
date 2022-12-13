# Setup
file = open('adv13.txt', 'r')
lines = [l.strip() for l in file.readlines()]

# Part 1
values = []
pair = []
pair_index = 1
index_sum = 0

def check_pair(pair: list | int, index: int = 0):
    if len(pair[0]) <= index and len(pair[1]) > index:
        return True
    elif len(pair[0]) > index and len(pair[1]) <= index:
        return False
    elif len(pair[0]) <= index and len(pair[1]) <= index:
        return None

    if isinstance(pair[0][index], int) and isinstance(pair[1][index], int):
        if pair[0][index] == pair[1][index]:
            return check_pair(pair, index + 1)
        else:
            return pair[0][index] < pair[1][index]
    elif isinstance(pair[0][index], list) and isinstance(pair[1][index], int):
        pair[1][index] = [pair[1][index]]
        return check_pair(pair, index)
    elif isinstance(pair[0][index], int) and isinstance(pair[1][index], list):
        pair[0][index] = [pair[0][index]]
        return check_pair(pair, index)
    else:
        p2 = [pair[0][index], pair[1][index], index]
        res = check_pair(p2, 0)
        if res != None:
            return res

        return check_pair(pair, index + 1)

for line in lines:
    if line.startswith('['):
        val = eval(line)
        pair.append(val)
        values.append(val)
        if len(pair) == 2:
            if check_pair(pair, 0):
                index_sum += pair_index
            pair_index += 1
            pair = []

print(f'Part 1: {index_sum}')

# Part 2

divider_packets = [[[2]], [[6]]]

values.append(divider_packets[0])
values.append(divider_packets[1])

i = 0
while i + 1 != len(values):
    pair = [values[i], values[i + 1]]
    if not check_pair(pair, 0):
        tmp = values[i]
        values[i] = values[i + 1]
        values[i + 1] = tmp
        i = max(0, i - 1)
    else:
        i += 1

decoder_key = 1
for i, val in enumerate(values):
    if val in divider_packets:
        decoder_key *= i + 1

print(f'Part 2: {decoder_key}')
