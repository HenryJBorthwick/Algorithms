def adjacency_list(campus_map):
    header, *edges = [s.split() for s in campus_map.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list

def next_vertex(in_tree, distance):
    distances_to_consider = []
    for i in range(len(in_tree)):
        if not in_tree[i]:
            distances_to_consider.append(distance[i])
    smallest = min(distances_to_consider)
    return distance.index(smallest)

def min_energy(campus_map):
    n = len(campus_map)
    in_tree = [False] * n
    distance = ['inf'] * n
    parent = [None] * n
    distance[0] = 0 # S = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in campus_map[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u 

    return parent, distance



campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(min_energy(campus_map))
3
campus_map = """\
U 1 W
"""

print(min_energy(campus_map))
0