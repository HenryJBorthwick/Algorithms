from collections import deque

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

def bfs(adjac_list, source_format, destination_format):
    num_formats = len(adjac_list)
    
    # If the source and destination formats are the same, return them directly
    if source_format == destination_format:
        return [source_format]

    # Perform a breadth-first search to find the shortest sequence of formats
    visited = [False] * num_formats
    queue = deque([(source_format, [source_format])])

    while queue:
        current_format, sequence = queue.popleft()

        # If the destination format is found, return the sequence
        if current_format == destination_format:
            return sequence

        if not visited[current_format]:
            visited[current_format] = True
            for next_format, _ in adjac_list[current_format]:
                queue.append((next_format, sequence + [next_format]))

    # If the destination format is not reachable, return "No solution!"
    return "No solution!"

def format_sequence(converters_info, source_format, destination_format):
    # Create an adjacency list using the provided adjacency_list function
    adjac_list = adjacency_list(converters_info)
    
    # Call the BFS function to find the shortest sequence of formats
    sequence = bfs(adjac_list, source_format, destination_format)

    return sequence

#TEST:
# converters_info_str = """\
# D 2
# 0 1
# """

# source_format = 0
# destination_format = 1

# print(format_sequence(converters_info_str, source_format, destination_format))

#OUTPUT:
# [0, 1]

#TEST:
# converters_info_str = """\
# D 2
# 0 1
# """

# print(format_sequence(converters_info_str, 1, 1))

#OUTPUT:
# [1]

# TEST:
# converters_info_str = """\
# D 2
# 0 1
# """

# print(format_sequence(converters_info_str, 1, 0))

#OUTPUT:
# No solution!

#TEST:
# converters_info_str = """\
# D 5
# 1 0
# 0 2
# 2 3
# 1 2
# """

# print(format_sequence(converters_info_str, 1, 2))

#OUTPUT:
# [1, 2]

#TEST:
# converters_info_str = """\
# D 1
# """

# print(format_sequence(converters_info_str, 0, 0))

#OUTPUT:
# [0]