import math

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

def dijkstra(adj_list, s):
    # n is the number of vertices in the graph
    n = len(adj_list)
    
    # in_tree array stores the vertices in the minimum spanning tree (MST)
    in_tree = [False] * n
    
    # distance array stores the shortest distance from the source vertex to each vertex
    distance = [float('inf')] * n
    
    # parent array stores the parent of each vertex in the MST
    parent = [None] * n
    
    # distance from source to itself is 0
    distance[s] = 0
    
    # loop until all vertices have been added to the MST
    while not all(in_tree):
        
        # find the next vertex to add to the MST
        u = next_vertex(in_tree, distance)
        
        # add the next vertex to the MST
        in_tree[u] = True
        
        # loop through each vertex adjacent to u
        for v, weight in adj_list[u]:
            
            # if the vertex v is not in the MST and the distance to v is greater than the distance to u plus the weight of the edge between u and v
            if not in_tree[v] and distance[u] + weight < distance[v]:
                
                # update the distance to v
                distance[v] = distance[u] + weight
                
                # set the parent of v as u
                parent[v] = u
    
    # return the parent and distance arrays
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

def min_capacity(city_map, depot_position):
    # Generate an adjacency list from the given city_map
    adj_list = adjacency_list(city_map)
    
    # Calculate the total number of vertices in the adjacency list
    n = len(adj_list)
    
    # Create a list to store the shortest distances from the depot to each vertex
    # Initialize all distances to infinity
    distances = [float('inf')] * n
    
    # Calculate the shortest paths and their distances using Dijkstra's algorithm
    parent, distance = dijkstra(adj_list, depot_position)

    # Update the distances list with the calculated distances from Dijkstra's algorithm
    for i in range(n):
        distances[i] = distance[i]

    # Find the maximum distance from the depot to any other vertex
    max_distance = max([d for d in distances if d != float('inf')])
    
    # Calculate the minimum battery capacity required
    # We multiply the maximum distance by 2 to account for the round trip (to and from the depot)
    # Then we multiply by (3 / 2) to convert the distance to the equivalent battery capacity
    # Finally, we divide by 0.75 to ensure there's at least 25% charge left in the battery
    min_capacity = (max_distance * 3)
    min_capacity = min_capacity / 0.75
    min_capacity = math.ceil(min_capacity)

    # Return the minimum battery capacity required
    return min_capacity

# TEST:
city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))

# OUTPUT:
# 16
# 0
# 16
# 8

#TEST
city_map = """\
U 3 W
0 1 3
0 2 5
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))

# OUTPUT:
# 20
# 32
# 32

#GET TO REWRITE THE MIN_CAPACITY FUNCTION