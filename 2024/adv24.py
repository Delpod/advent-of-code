file = open('adv24.txt', 'r')
lines: list[str] = file.read().splitlines()


gates = {}
check_gates = []
highest_z = 'z00'

initial_gates = True
for line in lines:
    if line == '':
        initial_gates = False
        continue

    if initial_gates:
        gate, value = line.split(': ')
        gates[gate] = int(value)
    else:
        gate1, op, gate2, _, vgate = line.split(' ')
        check_gates.append([gate1, gate2, op, vgate])
        if vgate > highest_z:
            highest_z = vgate


def check_arrangement(gates, check_gates):
    index = 0
    req_len = len(gates) + len(check_gates)

    while len(gates) != req_len:
        c = check_gates[index]
        if c[0] in gates and c[1] in gates and c[3] not in gates:
            if c[2] == 'AND':
                gates[c[3]] = gates[c[0]] & gates[c[1]]
            elif c[2] == 'OR':
                gates[c[3]] = gates[c[0]] | gates[c[1]]
            else:
                gates[c[3]] = gates[c[0]] ^ gates[c[1]]

            index = 0
            continue

        index += 1

        if index >= len(check_gates):
            return -1

    result = 0

    for g in gates:
        if g.startswith('z') and gates[g] == 1:
            result += 1 << int(g[1:])

    return result

# Thanks lscddit
def find_invalid():
    invalid = set()

    for gate1, gate2, op, vgate in check_gates:
        if vgate[0] == 'z' and op != 'XOR' and vgate != highest_z:
            invalid.add(vgate)

        if op == 'XOR' and vgate[0] not in ['x', 'y', 'z'] and gate1[0] not in ['x', 'y', 'z'] and gate2[0] not in ['x', 'y', 'z']:
            invalid.add(vgate)

        if op == 'AND' and 'x00' not in [gate1, gate2]:
            for b_gate1, b_gate2, b_op, _ in check_gates:
                if (vgate == b_gate1 or vgate == b_gate2) and b_op != 'OR':
                    invalid.add(vgate)

        if op == 'XOR':
            for b_gate1, b_gate2, b_op, _ in check_gates:
                if (vgate == b_gate1 or vgate == b_gate2) and b_op == 'OR':
                    invalid.add(vgate)

    return ','.join(sorted(list(invalid)))


result_p1 = check_arrangement(gates, check_gates)
print(f'Part 1: {result_p1}')
result_p2 = find_invalid()
print(f'Part 2: {result_p2}')
