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

# This function finds all the paths from the source to the destination in a graph.
def all_paths(adj_list, source, destination):
    paths = []  # This list will store all the paths from source to destination.
    
    # The backtracking function is called with the current path (starting with the source vertex).
    dfs_backtrack((source,), adj_list, destination, paths)
    
    return paths


# This function implements the backtracking algorithm.
def dfs_backtrack(current_path, adj_list, destination, paths):
    # If the last vertex in the current path is the destination, we found a path.
    if current_path[-1] == destination:
        paths.append(current_path)  # Add the path to the list of paths.
    else:
        # Get the neighbors of the last vertex in the current path.
        neighbors = adj_list[current_path[-1]]
        
        # Iterate over the neighbors.
        for neighbor, _ in neighbors:
            # If the neighbor is not in the current path, we can visit it (avoid cycles).
            if neighbor not in current_path:
                # Call the backtracking function with the extended path.
                dfs_backtrack(current_path + (neighbor,), adj_list, destination, paths)

#TEST:
# triangle_graph_str = """\
# U 3
# 0 1
# 1 2
# 2 0
# """

# adj_list = adjacency_list(triangle_graph_str)
# print(sorted(all_paths(adj_list, 0, 2)))
# print(all_paths(adj_list, 1, 1))

#OUTPUT:
# [(0, 1, 2), (0, 2)]
# [(1,)]

#TEST:
# graph_str = """\
# U 5
# 0 2
# 1 2
# 3 2
# 4 2
# 1 4
# """

# adj_list = adjacency_list(graph_str)
# print(sorted(all_paths(adj_list, 0, 1)))

#OUTPUT:
# [(0, 2, 1), (0, 2, 4, 1)]

#TEST:
# from pprint import pprint

# # graph used in tracing bfs and dfs
# graph_str = """\
# D 7
# 6 0
# 6 5
# 0 1
# 0 2
# 1 2
# 1 3
# 2 4
# 2 5
# 4 3
# 5 4
# """

# adj_list = adjacency_list(graph_str)
# pprint(sorted(all_paths(adj_list, 6, 3)))

#OUTPUT:
# [(6, 0, 1, 2, 4, 3),
#  (6, 0, 1, 2, 5, 4, 3),
#  (6, 0, 1, 3),
#  (6, 0, 2, 4, 3),
#  (6, 0, 2, 5, 4, 3),
#  (6, 5, 4, 3)]

# pseudocode:
# 1 procedure DFS-Backtrack(candidate, input, output)
# 2 if Is-Solution(candidate, input)
# 3 AddToOutput(candidate, output)
# 4 else
# 5 for child-candidate in Children(candidate, input)
# 6 DFS-Backtrack(child-candidate, input, output)