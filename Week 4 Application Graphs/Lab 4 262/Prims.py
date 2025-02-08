# Define a function for Prim's algorithm
def Prim(adj_list, s):
    
    # Find the number of vertices in the graph
    n = len(adj_list)
    
    # Initialize arrays to store which vertices are in the MST, their distances, and their parents
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    
    # Set the distance of the starting vertex to 0
    distance[s] = 0
    
    # Continue until all vertices are in the MST
    while not all(in_tree):
        
        # Find the next vertex to add to the MST based on its distance from the current tree
        u = next_vertex(in_tree, distance)
        
        # Add the vertex to the MST
        in_tree[u] = True
        
        # Update the distances and parents of neighboring vertices if they're not already in the MST
        for v, weight in adj_list[u]:
            if not in_tree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
                
    # Return the parent and distance arrays representing the MST
    return parent, distance

# Define a helper function to find the next vertex to add to the MST
def next_vertex(in_tree, distance):
    # Initialize minimum distance and vertex to None
    min_dist = None
    min_vertex = None
    
    # Loop through all vertices
    for v in range(len(in_tree)):
        # If the vertex is not already in the tree and its distance is less than the current minimum
        if not in_tree[v] and (min_dist is None or distance[v] < min_dist):
            # Update the minimum distance and vertex
            min_dist = distance[v]
            min_vertex = v
    
    # Return the vertex with the minimum distance
    return min_vertex

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

#TEST:
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(Prim(adjacency_list(graph_string), 1))
print(Prim(adjacency_list(graph_string), 2))

#OUTPUT:
# ([2, None, 1], [2, 0, 1])
# ([2, None, None], [1, inf, 0])

#TEST:
graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(Prim(adjacency_list(graph_string), 0))
print(Prim(adjacency_list(graph_string), 2))

#OUTPUT:
# ([None, None, 3, 0], [0, inf, 4, 2])
# ([3, None, None, 2], [4, inf, 0, 2])