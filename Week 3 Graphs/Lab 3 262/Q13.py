def dfs_tree(Adj, s):
    # Number of vertices in the graph
    n = len(Adj)
    # Array to keep track of the state of each vertex during the traversal
    state = ['Undiscovered'] * n
    # Array to store the parent of each vertex in the DFS tree
    parent = [None] * n
    # Mark the starting vertex as discovered
    state[s] = 'Discovered'
    # Traverse the graph starting from the starting vertex
    dfs_loop(Adj, s, state, parent)
    # Return the resulting DFS tree
    return parent

def dfs_loop(Adj, u, state, parent):
    # Explore the adjacent vertices of the current vertex
    for v, _ in Adj[u]:
        # If a vertex v is undiscovered, mark it as discovered and explore it recursively
        if state[v] == 'Undiscovered':
            state[v] = 'Discovered'
            # Set the parent of v to be u in the DFS tree
            parent[v] = u
            dfs_loop(Adj, v, state, parent)
    # Mark the current vertex as processed
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

#Test
# an undirected graph

# adj_list = [
#     [(1, None), (2, None)],
#     [(0, None), (2, None)],
#     [(0, None), (1, None)]
# ]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))
# print(dfs_tree(adj_list, 2))

#Output
# [None, 0, 1]
# [1, None, 0]
# [2, 0, None]

#Test
# a directed graph (note the asymmetrical adjacency list)

# adj_list = [
# [(1, None)],
# []
# ]

# print(dfs_tree(adj_list, 0))
# print(dfs_tree(adj_list, 1))

#Output
# [None, 0]
# [None, None]

#Test
# graph from the textbook example
# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# print(dfs_tree(adjacency_list(graph_string), 1))

#Output
# [None, None, 1, 2, 3, 4, 1]

#Test
# graph_string = """\
# U 4
# 2 3
# 2 1
# 0 3
# 1 0
# """

# print(dfs_tree(adjacency_list(graph_string), 0))

#Output
# [None, 2, 3, 0]

#Q8#
graph_string = """\
U 5
0 1
1 2
1 3
3 4
4 0
"""

print(dfs_tree(adjacency_list(graph_string), 0))