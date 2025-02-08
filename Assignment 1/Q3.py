def adjacency_list(graph_str):
    # Split the string into a list of lines
    lines = graph_str.strip().splitlines()

    # Get the type of the graph (directed or undirected) 
    graph_type, num_vertices, *is_weighted = lines[0].split()

    # Convert the number of vertices from string to integer
    num_vertices = int(num_vertices)
    
    # Initialize the adjacency list with empty lists
    adj_list = [[] for _ in range(num_vertices)]

    # Parse the edges and populate the adjacency list
    for line in lines[1:]:
        # Split line into two vertices
        parts = line.split()
        # Store each vertex
        vertex_one = int(parts[0])
        vertex_two = int(parts[1])

        # Check if weighted, have to use in for the * element is a list
        if 'W' in is_weighted:
            # Store weight of vertex 
            edge_weight = int(parts[2])
        else:
            # No give no weight
            edge_weight = None

        # Add edge to adjacency 
        adj_list[vertex_one].append((vertex_two, edge_weight))

        # Check if undirected to add the other edge connection
        if graph_type == 'U':
            adj_list[vertex_two].append((vertex_one, edge_weight))

    return adj_list

def dfs_topo(vertex, state, adj_list, stack):
    # Mark the vertex as discovered (1)
    state[vertex] = 1

    # Iterate through all the neighbors of the current vertex
    for neighbor, _ in adj_list[vertex]:
        # If the neighbor is undiscovered (0), perform DFS on the neighbor
        if state[neighbor] == 0:
            dfs_topo(neighbor, state, adj_list, stack)

    # Mark the vertex as processed (2)
    state[vertex] = 2

    # Add the processed vertex to the stack
    stack.append(vertex)

def build_order(dependencies):
    # Generate the adjacency list from the input graph string
    adj_list = adjacency_list(dependencies)
    num_programs = len(adj_list)

    # Initialize the state array
    state = [0] * num_programs

    # Initialize an empty stack
    stack = []

    # Iterate over all programs in the graph
    for program in range(num_programs):
        # If the program is undiscovered, start the modified DFS on the program
        if state[program] == 0:
            dfs_topo(program, state, adj_list, stack)

    # Return the content of the stack from top to bottom as a topological ordering
    stack.reverse()
    return stack

# TEST:
# dependencies = """\
# D 2
# 0 1
# """

# print(build_order(dependencies))

# OUTPUT:
# [0, 1]

# TEST:
# dependencies = """\
# D 3
# 1 2
# 0 2
# """

# print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])

# OUTPUT:
# True

# TEST:
# dependencies = """\
# D 3
# """
# # any permutation of 0, 1, 2 is valid in this case.
# solution = build_order(dependencies)
# if solution is None:
#     print("Wrong answer!")
# else:
#     print(sorted(solution))

# OUTPUT:
# [0, 1, 2]
