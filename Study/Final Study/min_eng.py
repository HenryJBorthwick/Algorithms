def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
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

def next_vertex(in_tree, distances):
    tuples = []

    # GET INDEX AND IF IN TREE BOL
    for count, bol in enumerate(in_tree):
        # IF IN TREE OR BOL = TRUE, ADD
        if not bol:
            tuples.append((count, distances[count]))

    best_distance = float('inf')
    best_index = count

    for count, distance in tuples:
        if distance < best_distance:
            best_distance = distance
            best_index = count

    return best_index

def prim(adj,s):
    n = len(adj)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[s] = 0

    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True

        for v, weight in adj[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    
    return parent, distance

def min_energy(campus_map):
    adj = adjacency_list(campus_map)
    tree, distance = prim(adj, 0)

    return sum(distance)

campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(min_energy(campus_map))
# 3

campus_map = """\
U 1 W
"""

print(min_energy(campus_map))
# 0