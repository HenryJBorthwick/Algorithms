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

def adjacency_matrix(graph_string):
    lines = graph_string.strip().split('\n')

    #Check if directed
    directed = lines[0].startswith('D')
   #Check if weighted
    weighted = 'W' in lines[0]
    #Convert vertexs to integer from string
    num_vertexs = int(lines[0].split()[1])
   
    #if weighted graph
    if not weighted:
        #Create matrix
        matrix = [[0] * num_vertexs for row in range(num_vertexs)]

        for line in lines[1:]:
           #Get vertexs
            vertex_1,vertex_2 = line.split()

            #Convert Vertex to integers
            vertex_1,vertex_2 = int(vertex_1), int(vertex_2)

            matrix[vertex_1][vertex_2] = 1
           
            if not directed:
                matrix[vertex_2][vertex_1] = 1
        #If graph weighted
    else:
        #Create matirx
        matrix = [[None] * num_vertexs for row in range(num_vertexs)]
        for line in lines[1:]:

            vertex_1, vertex_2, weight = line.split()

            vertex_1, vertex_2 = int(vertex_1), int(vertex_2)

            matrix[vertex_1][vertex_2] = int(weight)
           
            if not directed:
                matrix[vertex_2][vertex_1] = int(weight)

    return matrix

converters_info_str = """\
U 4
1 3
0 3
1 0
"""

print(adjacency_list(converters_info_str))