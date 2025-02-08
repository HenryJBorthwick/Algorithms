def dfs_tree(adj,s):
    n = len(adj)    
    state = ['Undiscovered'] * n 
    parent = [None] * n
    state[s] = 'Discovered'
    dfs_loop(adj,s, state, parent)
    return parent

def dfs_loop(adj,u,state,parent):
    for v, w in adj[u]:
        if state[v] == 'Undiscovered':
            state[v] = 'Discovered'
            parent[v] = u
            dfs_loop(adj,v,state,parent)
    state[u] = 'Processed'



def adjacency_list(graph_str):
    """DOCSTRING"""
    # Split the string into a list of lines
    lines = graph_str.strip().splitlines()

    # Get the type of the graph (directed or undirected) 
    graph_type, num_vertices, *is_weighted = lines[0].split()

    #Convert the number of vertices from string to integer
    num_vertices = int(num_vertices)

    # Initialize the adjacency list with empty lists
    adj_list = [[] for _ in range(num_vertices)]

    # Parse the edges and populate the adjacency list
    for line in lines[1:]:
        #Split line into two vertices
        parts = line.split()
        #Store each vertex
        vertex_one = int(parts[0])
        vertex_two = int(parts[1])

        #Check if weighted, have to use in for the * element is a list
        if 'W' in is_weighted:
            #Store weight of vertex 
            edge_weight = int(parts[2])
        else:
            #No give no weight
            edge_weight = None

        #Add edge to adjacency 
        adj_list[vertex_one].append((vertex_two, edge_weight))

        #Check if undirected to add the other edge connection
        if graph_type == 'U':
            adj_list[vertex_two].append((vertex_one, edge_weight))

    return adj_list


# an undirected graph

adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))
# [None, 0, 1]
# [1, None, 0]
# [2, 0, None]


# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
# [None, 0]
# [None, None]


# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(dfs_tree(adjacency_list(graph_string), 1))
# [None, None, 1, 2, 3, 4, 1]


graph_string = """\
U 4
2 3
2 1
0 3
1 0
"""

print(dfs_tree(adjacency_list(graph_string), 0))
# [None, 2, 3, 0]