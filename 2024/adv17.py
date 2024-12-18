# Setup
import math
file = open('adv17.txt', 'r')
lines: list[str] = file.read().splitlines()

O_A = int(lines[0].split(': ')[1])
O_B = int(lines[1].split(': ')[1])
O_C = int(lines[2].split(': ')[1])
instructions = [int(x) for x in lines[4].split()[1].split(',')]
i_count = len(instructions)

A, B, C = O_A, O_B, O_C

def get_combo(value):
    if value == 4:
        return A
    if value == 5:
        return B
    if value == 6:
        return C
    if value == 7:
        raise ValueError("wild 7 appeared")
    else:
        return value

def get_output():
    global A, B, C
    output = []

    index = 0
    while index < i_count:
        i = instructions[index]

        if i == 0:
            A = math.floor(A / (2 ** get_combo(instructions[index + 1])))
        elif i == 1:
            B ^= instructions[index + 1]
        elif i == 2:
            B = get_combo(instructions[index + 1]) % 8
        elif i == 3:
            if A != 0:
                index = instructions[index + 1]
                continue
        elif i == 4:
            B ^= C
        elif i == 5:
            output.append(get_combo(instructions[index + 1]) % 8)
        elif i == 6:
            B = math.floor(A / (2 ** get_combo(instructions[index + 1])))
        elif i == 7:
            C = math.floor(A / (2 ** get_combo(instructions[index + 1])))

        index += 2
    
    return output

result_p1 = ','.join(map(str, get_output()))

O_A = 706740000
is_different = True
while is_different:
    A = O_A
    if A % 10000 == 0:
        print(A)
    output = get_output()
    is_different = len(output) != i_count
    if not is_different:
        for i, out in enumerate(output):
            if instructions[i] != out:
                is_different = True
                break

    if is_different:
        O_A += 1
result_p2 = O_A

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
