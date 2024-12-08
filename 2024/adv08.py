# Setup
file = open('adv08.txt', 'r')
lines = file.read().splitlines()

antennas = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != '.':
            if char not in antennas:
                antennas[char] = []
            
            antennas[char].append((i, j))

height = len(lines)
width = len(lines[0])

def check_positions(calculate_resonant_harmonics):
    antinodes = set()
    for i, (key, values) in enumerate(antennas.items()):
        for value in values:
            for test_value in values:
                if value == test_value:
                    continue

                diff = (value[0] - test_value[0], value[1] - test_value[1])
                test_position = value
                position_found = False
                while calculate_resonant_harmonics or not position_found:
                    test_position = (test_position[0] - diff[0], test_position[1] - diff[1])

                    if test_position[0] < 0 or test_position[0] >= height or test_position[1] < 0 or test_position[1] >= width:
                        break
                    
                    if calculate_resonant_harmonics or lines[test_position[0]][test_position[1]] != key:
                        antinodes.add(test_position)
                        position_found = True

    return len(antinodes)

result_p1 = check_positions(False)
result_p2 = check_positions(True)

print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
