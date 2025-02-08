# Function to transpose a graph's adjacency list
def transpose(adj_list):
    """DOCSTRING"""
    # Create an empty list for the transposed adjacency list
    transposed_adj_list = []
    
    # Iterate through the nodes in the original adjacency list
    for _ in range(len(adj_list)):
        # Create an empty set to store the reversed edges for each node
        empty_set = set()
        # Append the empty set to the transposed adjacency list
        transposed_adj_list.append(empty_set)

    # Iterate through each node (source_node) and its edges in the original adjacency list
    for source_node in range(len(adj_list)):
        # Iterate through the edges of the source_node
        for target_node, weight in adj_list[source_node]:
            # Add the reverse edge to the transposed adjacency list
            # For a directed edge (source_node -> target_node), add (source_node, weight) to target_node's edges
            transposed_adj_list[target_node].add((source_node, weight))
            
    # Return the transposed adjacency list
    return transposed_adj_list




def adjacency_list(graph_string):
    # Split the input string into lines and process the first line to get graph properties
    lines = graph_string.strip().split('\n')
    header = lines[0].split()
    directed = header[0] == "D"
    num_nodes = int(header[1])

    # Create an empty adjacency list
    adj_list = [set() for _ in range(num_nodes)]

    # Process the edges from the remaining lines
    for line in lines[1:]:
        edge_info = line.split()
        source = int(edge_info[0])
        target = int(edge_info[1])
        weight = int(edge_info[2]) if len(edge_info) > 2 else None

        # Add the edge to the adjacency list
        adj_list[source].add((target, weight))

        # If the graph is undirected, also add the reverse edge
        if not directed:
            adj_list[target].add((source, weight))

    return adj_list


#Test:
# graph_string = """\
# D 3
# 0 1
# 1 0
# 0 2
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

#Output:
# 0 [(1, None)]
# 1 [(0, None)]
# 2 [(0, None)]

#Input:
# graph_string = """\
# D 3 W
# 0 1 7
# 1 0 -2
# 0 2 0
# """

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

#Output:
# 0 [(1, -2)]
# 1 [(0, 7)]
# 2 [(0, 0)]

#Input:
# It should also work undirected graphs.
# The output will be the same as input.

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

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

#Output:
# 0 []
# 1 [(2, None), (5, None), (6, None)]
# 2 [(1, None), (3, None), (5, None)]
# 3 [(2, None), (4, None)]
# 4 [(3, None), (5, None)]
# 5 [(1, None), (2, None), (4, None)]
# 6 [(1, None)]

#Input:
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

# graph_adj_list = adjacency_list(graph_string)
# graph_transposed_adj_list = transpose(graph_adj_list)
# for i in range(len(graph_transposed_adj_list)):
#     print(i, sorted(graph_transposed_adj_list[i]))

#Output:
# 0 []
# 1 [(2, None), (6, None), (15, None)]
# 2 [(1, None), (15, None)]
# 3 []
# 4 [(5, None), (13, None)]
# 5 [(4, None)]
# 6 [(1, None)]
# 7 []
# 8 []
# 9 []
# 10 []
# 11 []
# 12 [(13, None)]
# 13 [(4, None), (12, None)]
# 14 []
# 15 [(1, None), (2, None)]
# 16 []