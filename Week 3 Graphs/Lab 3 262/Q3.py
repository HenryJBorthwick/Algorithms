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

#Test:
# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """

# print(adjacency_matrix(graph_string))

#Output:
#[[0, 1, 1], [1, 0, 0], [0, 0, 0]]

#Test:
# graph_string = """\
# D 3 W
# 0 1 7
# 1 0 -2
# 0 2 0
# """
# print(adjacency_matrix(graph_string))

#Output:
#[[None, 7, 0], [-2, None, None], [None, None, None]]

#Test:
# from pprint import pprint

# graph_string = """\
# U 7
# 1 2
# 1 5
# 1 6
# 3 4
# 0 4
# 4 5
# """

# pprint(adjacency_matrix(graph_string))

#Output:
# [[0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 1, 0, 0, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [1, 0, 0, 1, 0, 1, 0],
#  [0, 1, 0, 0, 1, 0, 0],
#  [0, 1, 0, 0, 0, 0, 0]]

#Output:
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

# pprint(adjacency_matrix(graph_string))

#Test:
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
