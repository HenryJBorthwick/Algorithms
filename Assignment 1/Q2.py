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

def dfs(vertex, visited, adj_list, bubble):
    # Mark the current vertex as visited
    visited[vertex] = True
    # Add the current vertex to the current bubble
    bubble.add(vertex)

    # Iterate through all the neighbors of the current vertex
    for neighbor, _ in adj_list[vertex]:
        # If the neighbor hasn't been visited yet, perform DFS on the neighbor
        if not visited[neighbor]:
            dfs(neighbor, visited, adj_list, bubble)

def bubbles(physical_contact_info):
    # Generate the adjacency list from the input graph string
    adj_list = adjacency_list(physical_contact_info)
    # Initialize the visited list with False for all vertices
    visited = [False] * len(adj_list)
    # Initialize the result list to store the bubbles
    result = []
    
    # Iterate through all the vertices in the graph
    for vertex in range(len(adj_list)):
        # If the vertex hasn't been visited yet, it's a new bubble
        if not visited[vertex]:
            # Initialize a new set to represent the current bubble
            bubble = set()
            # Perform DFS on the current vertex to find all connected vertices (bubble members)
            dfs(vertex, visited, adj_list, bubble)
            # Add the current bubble to the result list
            result.append(bubble)

    # Return the result list containing all bubbles
    return result

#TEST:
# physical_contact_info = """\
# U 2
# 0 1
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#OUPUT:
# [[0, 1]]

# #TEST:
# physical_contact_info = """\
# U 2
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#OUTPUT:
# [[0], [1]]

#TEST
# physical_contact_info = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#OUTPUT:
# [[0], [1, 2, 3, 4, 5, 6]]

#TEST:
# physical_contact_info = """\
# U 0
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#OUTPUT:
# []

#TEST:
# physical_contact_info = """\
# U 1
# """

# print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

#OUTPUT:
# [[0]]