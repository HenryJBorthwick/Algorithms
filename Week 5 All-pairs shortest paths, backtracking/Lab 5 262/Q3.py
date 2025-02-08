import copy

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

def floyd(distance):
    # Make a deep copy of the input distance matrix to avoid mutating it
    dist_matrix = copy.deepcopy(distance)

    # Determine the number of vertices in the distance matrix
    num_vertices = len(dist_matrix)

    # Use three nested loops for the Floyd-Warshall algorithm to compute all-pairs shortest paths
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update the distance matrix if a shorter path is found
                if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]

    return dist_matrix


#TEST:
# graph_str = """\
# D 3 W
# 0 1 1
# 1 2 2
# 2 0 4
# """

# adj_list = adjacency_list(graph_str)
# dist_matrix = distance_matrix(adj_list)
# print("Initial distance matrix:", dist_matrix)
# dist_matrix = floyd(dist_matrix)
# print("Shortest path distances:", dist_matrix)

#OUTPUT:
# Initial distance matrix: [[0, 1, inf], [inf, 0, 2], [4, inf, 0]]
# Shortest path distances: [[0, 1, 3], [6, 0, 2], [4, 5, 0]]

#TEST:
# import pprint

# graph_str = """\
# U 7 W
# 0 1 5
# 0 2 7
# 0 3 12
# 1 2 9
# 2 3 4
# 1 4 7
# 2 4 4
# 2 5 3
# 3 5 7
# 4 5 2
# 4 6 5
# 5 6 2
# """

# pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))

#OUTPUT:
# [[0, 5, 7, 11, 11, 10, 12],
#  [5, 0, 9, 13, 7, 9, 11],
#  [7, 9, 0, 4, 4, 3, 5],
#  [11, 13, 4, 0, 8, 7, 9],
#  [11, 7, 4, 8, 0, 2, 4],
#  [10, 9, 3, 7, 2, 0, 2],
#  [12, 11, 5, 9, 4, 2, 0]]