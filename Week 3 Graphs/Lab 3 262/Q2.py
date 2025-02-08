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

# #TEST
# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """
# print(adjacency_list(graph_string))

#OUTPUT:
#[[(1, None), (2, None)], [(0, None)], []]

#TEST
# graph_string = """\
# D 3 W
# 0 1 7
# 1 0 -2
# 0 2 0
# """
# print(adjacency_list(graph_string))

#OUTPUT
#[[(1, 7), (2, 0)], [(0, -2)], []]

# # #TEST
# from pprint import pprint

# # undirected graph in the textbook example
# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 2 3
# 2 5
# 3 4
# 4 5
# """

# pprint(adjacency_list(graph_string))

#OUTPUT:
#[[],
# [(2, None), (5, None), (6, None)],
# [(1, None), (3, None), (5, None)],
# [(2, None), (4, None)],
# [(3, None), (5, None)],
# [(1, None), (2, None), (4, None)],
# [(1, None)]]

# #TEST
# from pprint import pprint

# graph_string = """\
# U 17
# 1 2
# 1 15
# 1 6
# 12 13
# 2 15
# 13 4
# 4 5
# """

# pprint(adjacency_list(graph_string))

#OUTPUT:
#[[],
# [(2, None), (15, None), (6, None)],
# [(1, None), (15, None)],
# [],
# [(13, None), (5, None)],
# [(4, None)],
# [(1, None)],
# [],
# [],
# [],
# [],
# [],
# [(13, None)],
# [(12, None), (4, None)],
# [],
# [(1, None), (2, None)],
# []]