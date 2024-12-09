# Setup
file = open('adv09.txt', 'r')
line = file.read()

file_list = []

findex = 0
for i, char in enumerate(line):
    n = int(char)
    if i % 2 == 0:
        file_list += [findex] * n
        findex += 1
    else:
        file_list += [-1] * n
        
def part_1():
    defrag_list = file_list[::]
    lindex, rindex = 0, len(defrag_list) - 1

    while True:
        while defrag_list[lindex] != -1:
            lindex += 1
        while defrag_list[rindex] == -1:
            rindex -= 1

        if lindex >= rindex:
            break

        defrag_list[lindex] = defrag_list[rindex]
        defrag_list[rindex] = -1

    result = 0

    for i, f in enumerate(defrag_list):
        if f < 0:
            break

        result += f * i
    
    return result


def part_2():
    file_groups = [{ "id": 0, "size": 0 }]
    
    for id in file_list:
        if file_groups[-1]["id"] != id:
            file_groups.append({ "id": id, "size": 0 })

        file_groups[-1]["size"] += 1
    
    rindex = len(file_groups) - 1
    while rindex != 0:
        rgroup = file_groups[rindex]
        if rgroup["id"] != -1:
            lindex = 0
            while lindex < rindex:
                lgroup = file_groups[lindex]
                if lgroup["id"] != -1 or lgroup["size"] < rgroup["size"]:
                    lindex += 1
                    continue

                diff = lgroup["size"] - rgroup["size"]

                lgroup["id"] = rgroup["id"]
                rgroup["id"] = -1

                if diff > 0:
                    file_groups.insert(lindex + 1, { "id": -1, "size": diff })
                    lgroup["size"] = rgroup["size"]

                rindex += 1
                break
        rindex -= 1
    
    defrag_list = []

    for group in file_groups:
        defrag_list += [group["id"]] * group["size"]

    result = 0

    for i, f in enumerate(defrag_list):
        if f > 0:
            result += f * i
    
    return result


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
