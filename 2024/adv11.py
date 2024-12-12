# Setup
file = open('adv11.txt', 'r')
stones = [int(stone) for stone in file.read().split()]
key_cache = {}
len_cache = {}
left_cache = {}
right_cache = {}


def get_after_iterations(stones, iterations):
    stones_dict = {}

    for stone in stones:
        stones_dict[stone] = stones_dict[stone] + 1 if stone in stones_dict else 1

    for _ in range(iterations):
        new_stones = {}
        for _, (key, value) in enumerate(stones_dict.items()):
            if key == 0:
                new_stones[1] = new_stones[1] + value if 1 in new_stones else value
                continue

            if key not in len_cache:
                key_cache[key] = str(key)
                len_cache[key] = len(key_cache[key])
                if len_cache[key] % 2 == 0:
                    div2 = int(len_cache[key] / 2)
                    left_cache[key] = int(key_cache[key][:div2])
                    right_cache[key] = int(key_cache[key][div2:])
                else:
                    del key_cache[key]

            if len_cache[key] % 2 == 0:
                left = left_cache[key]
                right = right_cache[key]
                new_stones[left] = new_stones[left] + value if left in new_stones else value
                new_stones[right] = new_stones[right] + value if right in new_stones else value
                continue

            new_value = key * 2024
            new_stones[new_value] = new_stones[new_value] + value if new_value in new_stones else value

        stones_dict = new_stones

    sum = 0
    for _, value in enumerate(stones_dict.values()):
        sum += value

    return sum


result_p1 = get_after_iterations(stones, 25)
print(f"Part 1: {result_p1}")

result_p2 = get_after_iterations(stones, 75)
print(f"Part 2: {result_p2}")
