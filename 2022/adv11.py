# Setup
import math
file = open('adv11.txt', 'r')
lines = [l.strip() for l in file.readlines()]

# Part 1 & 2
def count_monkey_business(iterations, divider):
    monkeys = []
    modulo = 1

    for line in lines:
        if line.startswith('Monkey'):
            monkeys.append({'inspections': 0})
        elif line.startswith('Starting'):
            _, values = line.split(': ')
            monkeys[-1]['items'] = [int(v) for v in values.split(', ')]
        elif line.startswith('Operation'):
            _, operation = line.split(' = ')
            first, operator, second = operation.split(' ')
            monkeys[-1]['op_first'] = int(first) if first.isnumeric() else first
            monkeys[-1]['op'] = operator
            monkeys[-1]['op_second'] = int(second) if second.isnumeric() else second
        elif line.startswith('Test'):
            _, value = line.split(' by ')
            monkeys[-1]['test_value'] = int(value)
            modulo *= int(value)
        elif line.startswith('If true'):
            _, target_monkey = line.split(' monkey ')
            monkeys[-1]['true_monkey'] = int(target_monkey)
        elif line.startswith('If false'):
            _, target_monkey = line.split(' monkey ')
            monkeys[-1]['false_monkey'] = int(target_monkey)

    for _ in range(iterations):
        for m in monkeys:
            for i in m['items']:
                w = i
                p1 = w if m['op_first'] == 'old' else m['op_first']
                p2 = w if m['op_second'] == 'old' else m['op_second']
                if m['op'] == '*':
                    w = p1 * p2
                else:
                    w = p1 + p2

                w = w % modulo
                w = w // divider

                if w % m['test_value'] == 0:
                    monkeys[m['true_monkey']]['items'].append(w)
                else:
                    monkeys[m['false_monkey']]['items'].append(w)
                m['inspections'] += 1
            m['items'] = []

    monkey_business = 1
    for m in sorted(monkeys, key= lambda m: m['inspections'])[-2:]:
        monkey_business *= m['inspections']

    return monkey_business

print(f'Part 1: {count_monkey_business(20, 3)}')
print(f'Part 2: {count_monkey_business(10000, 1)}')
