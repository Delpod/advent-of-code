# Setup
file = open('adv11.txt', 'r')
stones = [int(stone) for stone in file.read().split()]


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

            stonestr = str(key)
            stonelen = len(stonestr)

            if stonelen % 2 == 0:
                div2 = int(stonelen / 2)
                left = int(stonestr[:div2])
                right = int(stonestr[div2:])
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
