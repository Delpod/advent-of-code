# Setup
file = open('adv05.txt', 'r')
lines = [l.strip() for l in file.readlines()]

result_p1 = 0
result_p2 = 0

pages = {}
mode = "P"

# Part 1 & 2
for line in lines:
    if mode == "P":
        if line == "":
            mode = "U"
            continue

        x, y = [int(n) for n in line.split('|')]

        if x not in pages:
            pages[x] = set()

        pages[x].add(y)

    else:
        update = [int(n) for n in line.split(',')]
        sorted = []

        is_valid_order = True
        i = 0
        while len(update) > 0:
            requires_page = False
            for u in update:
                if u == update[i]:
                    continue

                if u in pages and update[i] in pages[u]:
                    requires_page = True
                    break
            
            if not requires_page:
                sorted.append(update[i])
                update.pop(i)
                i = 0
                continue
            else:
                is_valid_order = False

            i += 1

        if is_valid_order:
            result_p1 += sorted[int(len(sorted) / 2)]
        else:
            result_p2 += sorted[int(len(sorted) / 2)]


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")
