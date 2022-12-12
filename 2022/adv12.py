# Setup
file = open('adv12.txt', 'r')
lines = [l.strip() for l in file.readlines()]

def get_shortest_path(rows: list, edges: list, start: tuple):
    vertices = len(rows) * len(rows[0])
    previous = [[None for _ in row] for row in rows]
    distance = [[float('inf') for _ in row] for row in rows]

    distance[start[0]][start[1]] = 0

    for _ in range(vertices):
        for u, v in edges:
            new_distance = distance[u[0]][u[1]] + 1

            if distance[v[0]][v[1]] > new_distance:
                distance[v[0]][v[1]] = new_distance
                previous[v[0]][v[1]] = u
    
    return { 'distance': distance, 'previous': previous }


def construct_shortest_path(previous, start, end, result = None):
    if result == None:
        result = []

    if start == end:
        pass
    elif previous[end[0]][end[1]] == None:
        return None
    else:
        construct_shortest_path(previous, start, previous[end[0]][end[1]], result)
        result.append(end)

    return result


def create_edges(rows: list):
    edges = []

    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            if j > 0 and row[j - 1] >= cell - 1:
                edges.append([(i, j), (i, j - 1)])
            if j < len(row) - 1 and row[j + 1] >= cell - 1:
                edges.append([(i, j), (i, j + 1)])
            if i > 0 and rows[i - 1][j] >= cell - 1:
                edges.append([(i, j), (i - 1, j)])
            if i < len(rows) - 1 and rows[i + 1][j] >= cell - 1:
                edges.append([(i, j), (i + 1, j)])

    return edges


# Part 1

rows = [[] for _ in lines]
start = None
starts = []
end = None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)
            starts.append((i, j))
            rows[i].append(ord('a'))
        elif char == 'E':
            end = (i, j)
            rows[i].append(ord('z'))
        else:
            if char == 'a':
                starts.append((i, j))
            rows[i].append(ord(char))

edges = create_edges(rows)
result = get_shortest_path(rows, edges, end)
path = construct_shortest_path(result['previous'], end, start)

print(f'Part 1: {len(path)}')

# Part 2

shortest_path = float('inf')

for i, s in enumerate(starts):
    path = construct_shortest_path(result['previous'], end, s)
    if path != None and shortest_path > len(path):
        shortest_path = len(path)

print(f'Part 2: {shortest_path}')
