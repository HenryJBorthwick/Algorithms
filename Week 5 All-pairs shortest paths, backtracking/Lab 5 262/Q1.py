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

def distance_matrix(adj_list):
    # Determine the number of vertices in the adjacency list
    num_vertices = len(adj_list)

    # Create an empty distance matrix filled with infinity values
    dist_matrix = []
    for i in range(num_vertices):
        row = []
        for j in range(num_vertices):
            if i == j:
                # Set the main diagonal elements to 0
                row.append(0)
            else:
                # Set the other elements to infinity
                row.append(float('inf'))
        dist_matrix.append(row)

    # Loop through the adjacency list and update the distance matrix with edge weights
    for i in range(num_vertices):
        # Get the list of edges for vertex i
        edges = adj_list[i]

        # Loop through the edges
        for edge in edges:
            # Get the destination vertex and weight from the edge tuple
            j, weight = edge

            # Update the distance matrix with the edge weight
            dist_matrix[i][j] = weight

    return dist_matrix


#TEST:
# graph_str = """\
# U 3 W
# 0 1 5
# 2 1 7
# """

# adj_list = adjacency_list(graph_str)
# print(distance_matrix(adj_list))

# # more readable output (less readable code):
# print("\nEach row on a new line:")
# print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

#OUTPUT:
# [[0, 5, inf], [5, 0, 7], [inf, 7, 0]]

# Each row on a new line:
# [0, 5, inf]
# [5, 0, 7]
# [inf, 7, 0]

#TEST:
# graph_str = """\
# D 2 W
# 0 1 4
# """

# adj_list = adjacency_list(graph_str)
# print(distance_matrix(adj_list))

#OUTPUT:
# [[0, 4], [inf, 0]]