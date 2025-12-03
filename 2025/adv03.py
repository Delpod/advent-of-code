# Setup
file = open('adv03.txt', 'r')
banks = file.read().splitlines()


def find_biggest_number(full_string, req_digits, compare:str=None):
    largest_digit = full_string[0]
    if req_digits == 1:
        return largest_digit
    
    max_index = len(full_string) - req_digits + 1

    largest_indexes = []
    for i in range(max_index):
        digit = full_string[i]
        if digit > largest_digit:
           largest_digit = full_string[i]
           largest_indexes = [i]
        elif digit == largest_digit:
            largest_indexes.append(i)

    if compare and compare > largest_digit:
        return None

    largest_rest = '0'
    for index in largest_indexes:
        for i in range(index + 1, max_index + 1):
            largest_candidate = find_biggest_number(full_string[i:], req_digits -1, largest_rest)

            if largest_candidate != None and largest_candidate > largest_rest:
                largest_rest = largest_candidate

    return largest_digit + largest_rest


sum_p1 = 0
sum_p2 = 0

for i, bank in enumerate(banks):
    sum_p1 += int(find_biggest_number(bank, 2))
    sum_p2 += int(find_biggest_number(bank, 12))

print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
