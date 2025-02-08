def adjacency_list(graph_string):
    lines = graph_string.strip().split('\n')
    header = lines[0].split()
    directed = header[0] == "D"
    num_nodes = int(header[1])
    adj_list = [set() for _ in range(num_nodes)]

    for line in lines[1:]:
        edge_info = line.split()
        source = int(edge_info[0])
        target = int(edge_info[1])
        adj_list[source].add(target)

        if not directed:
            adj_list[target].add(source)

    return adj_list

def dfs(adj_list, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in adj_list[node])

    return visited

def is_strongly_connected(adj_list):
    directed = all(len(edge) == len(adj_list) - 1 for edge in adj_list)
    
    if directed:
        for start_node in range(len(adj_list)):
            visited_nodes = dfs(adj_list, start_node)

            if len(visited_nodes) != len(adj_list):
                return False
    else:
        visited_nodes = dfs(adj_list, 0)

        if len(visited_nodes) != len(adj_list):
            return False

    return True


# Test case
graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))  

# Output: False
