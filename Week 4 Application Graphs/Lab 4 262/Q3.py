def is_strongly_connected(adj_list):
    # Check if the graph is empty
    if not adj_list:
        return False

    # Perform a DFS from the first vertex
    visited = [False] * len(adj_list)
    dfs(adj_list, 0, visited)

    # Check if all vertices were visited
    if False in visited:
        return False

    # Perform a DFS from a different vertex
    visited = [False] * len(adj_list)
    dfs(adj_list, len(adj_list) - 1, visited)

    # Check if all vertices were visited
    if False in visited:
        return False

    # If both DFS traversals visit all vertices, the graph is strongly connected
    return True

def dfs(adj_list, vertex, visited):
    # Mark the current vertex as visited
    visited[vertex] = True
    
    # Traverse all the neighbors of the current vertex
    for neighbor, weight in adj_list[vertex]:
        # If the neighbor has not been visited, recursively call DFS on it
        if not visited[neighbor]:
            dfs(adj_list, neighbor, visited)

def adjacency_list(graph_str):
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

# Test:
# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """

# print(is_strongly_connected(adjacency_list(graph_string)))

# Output:
# False

# Test:
# graph_string = """\
# D 3
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))

# Output:
# True

# Test:
# graph_string = """\
# D 4
# 0 1
# 1 2
# 2 0
# """

# print(is_strongly_connected(adjacency_list(graph_string)))

# Output:
# False

# Test:
# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

# graph_string = """\
# U 5
# 2 4
# 3 1
# 0 4
# 2 1
# """

# print(is_strongly_connected(adjacency_list(graph_string)))

# Output:
# True