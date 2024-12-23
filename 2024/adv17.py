# Setup
file = open('adv17.txt', 'r')
lines: list[str] = file.read().splitlines()

O_A = int(lines[0].split(': ')[1])
O_B = int(lines[1].split(': ')[1])
O_C = int(lines[2].split(': ')[1])
instructions = [int(x) for x in lines[4].split()[1].split(',')]
ins_count = len(instructions)

A, B, C = O_A, O_B, O_C

def get_combo(value, a, b, c):
    if value == 4:
        return a
    if value == 5:
        return b
    if value == 6:
        return c
    if value == 7:
        raise ValueError("wild 7 appeared")
    else:
        return value

def get_output(instructions, a, b, c):
    output = []

    index = 0
    while index < ins_count:
        i = instructions[index]

        if i == 0:
            a //= 2 ** get_combo(instructions[index + 1], a, b, c)
        elif i == 1:
            b ^= instructions[index + 1]
        elif i == 2:
            b = get_combo(instructions[index + 1], a, b, c) % 8
        elif i == 3:
            if a != 0:
                index = instructions[index + 1]
                continue
        elif i == 4:
            b ^= c
        elif i == 5:
            output.append(get_combo(instructions[index + 1],  a, b, c) % 8)
        elif i == 6:
            b = a // (2 ** get_combo(instructions[index + 1], a, b, c))
        elif i == 7:
            c = a // (2 ** get_combo(instructions[index + 1], a, b, c))

        index += 2
    
    return output

result_p1 = ','.join(map(str, get_output(instructions, A, B, C)))

A = 0
j = 1
i_start = 0
while j <= ins_count and j >= 0:
    A <<= 3
    for i in range(i_start, 8):
        if instructions[-j:] == get_output(instructions, A + i, B, C):
            break
    else:
        j -= 1
        A >>= 3
        i_start = A % 8 + 1
        A >>= 3
        continue
    j += 1
    A += i
    i_start = 0
    
result_p2 = A

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
