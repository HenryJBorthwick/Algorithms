from collections import deque
"""TAKE adjacency list and starting vertex and perofrms a BFS return parent array"""

def bfs_tree(adj_list, s):
    # Get the number of vertices in the graph
    n = len(adj_list)
    
    # Initialize arrays for the state and parent of each vertex
    state = ['Undiscovered'] * n
    parent = [None] * n

    # Initialize an empty queue
    Q = deque()
    
    # Set the starting vertex as discovered and enqueue it
    state[s] = 'Discovered'
    Q.append(s)
    
    # Call the BFS loop to search the graph and return the resulting tree
    return bfs_loop(adj_list, Q, state, parent)

def bfs_loop(adj_list, Q, state, parent):
    # Continue while there are vertices in the queue
    while Q:
        # Dequeue the next vertex to process
        u = Q.popleft()
        
        # Loop over the adjacent vertices of u
        for v, w in adj_list[u]:
            # If v is undiscovered, set it as discovered, set its parent as u, and enqueue it
            if state[v] == 'Undiscovered':
                state[v] = 'Discovered'
                parent[v] = u
                Q.append(v)
        
        # Mark u as processed
        state[u] = 'Processed'
    
    # Return the resulting tree
    return parent

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
#     [(1, None)],
#     [(0, None), (2, None)],
#     [(1, None)]
# ]

# bfs_tree(adj_list, 0)
# bfs_tree(adj_list, 1)

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))

#Output
# [None, 0, 1]
# [1, None, 1]

#Test
# a directed graph (note the asymmetrical adjacency list)

# adj_list = [
# [(1, None)],
# []
# ]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))

#Output
# [None, 0]
# [None, None]

#Test
# graph_string = """\
# D 2
# 0 1
# """

# print(bfs_tree(adjacency_list(graph_string), 0))

#Output
# [None, 0]

#Test
# graph_string = """\
# D 2
# 0 1
# 1 0
# """

# print(bfs_tree(adjacency_list(graph_string), 1))

#Output
# [1, None]

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

# print(bfs_tree(adjacency_list(graph_string), 1))

#Output
# [None, None, 1, 2, 5, 1, 1]

#Test
# graph_string = """\
# D 2 W
# 0 1 99
# """

# print(bfs_tree(adjacency_list(graph_string), 0))

#Output
#[None, 0]

#Q6#
graph_string = """\
U 6
0 4
5 4
4 2
2 3
3 0
3 4
"""

print(bfs_tree(adjacency_list(graph_string), 2))