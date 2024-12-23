from collections import defaultdict
file = open('adv23.txt', 'r')
lines: list[str] = file.read().splitlines()

connections = defaultdict(set)

for line in lines:
    c1, c2 = line.split('-')

    connections[c1].add(c2)
    connections[c2].add(c1)

sets: set[tuple[str]] = set()

for key in connections:
    c1 = connections[key]
    for key2 in c1:
        if key == key2:
            continue

        c2 = connections[key2]

        for key3 in c2:
            if key == key3:
                continue
        
            if key3 in c1:
                sets.add(tuple(sorted([key, key2, key3])))

triples = set()
for s in sets:
    if s[0].startswith('t') or s[1].startswith('t') or s[2].startswith('t'):
        triples.add(s)

result_p1 = len(triples)

# Thanks DSrcl
def grow_clique(clique: set, connections: defaultdict[str, set]):
    clique = set(clique)
    while True:
        for x in clique:
            for y in connections[x]:
                if connections[y].issuperset(clique):
                    clique.add(y)
                    break
            else:
                continue
            break
        else:
            break
    return clique

max_clique = set()
visited = set()
for triple in triples:
    if triple[0] in visited:
        continue

    clique = grow_clique(triple, connections)
    visited.update(clique)

    if len(clique) > len(max_clique):
        max_clique = clique

result_p2 = ','.join(sorted(max_clique))


print(f"Part 1: {result_p1}")
print(f"Part 2: {result_p2}")