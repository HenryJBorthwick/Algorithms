# The function Next-Vertex(in-tree, distance) returns a closest vertex
# that is not yet part of the tree; 

# 
def next_vertex(in_tree, distances):
    tuples = []

    # FROM IN TREE GET THE INDEX AND IF IN TREE (BOL TYPE)
    for index, bol in enumerate(in_tree):
        # IF THE VERTEX STATE IS FALSE, SO NOT IN TREE ADD IT 
        if not bol:
            tuples.append((index, distances[index]))
    

    best_distance = float('inf')
    best_index = None

    # LOOK THROUGH INDEX AND DISTACE IN THE TUPLE OF VERTIECES NOT ADDED
    for index, distance in tuples:
        # IF DISTANCE IN TUPLE IS BETTER, UPDATE BEST DISTANCE AND INDEX
        if distance < best_distance:
            best_distance = distance
            best_index = index

    # RETURN INDEX OF THE VERTICE WITH LARGEST DISTANCE
    return best_index


def next_vertex(in_tree, distance):
    distance_of_not_in_tree = []

    # CHECK THROUGH INDEX AND BOL TYPE OF EACH ITEM IN TREE
    for index, bol in enumerate(in_tree):
        # IF NOT FALSE, OR IF NOT IN TREE, ADD INDEX AND DISTACE TO
        if not bol:
            distance_of_not_in_tree.append((index, distance[index]))

    # CHECK THROUGH FOR BEST INDEX AND DISTANCE

    best_index = None
    best_distance = float('inf')

    for index, distance in distance_of_not_in_tree:
        if distance < best_distance:
            best_distance = distance
            best_index = index

    return best_index

def next_vertex(in_tree, distance):
    index_distance_tuples = []

    for index, bol in enumerate(in_tree):
        if not bol:
            index_distance_tuples.append((index, distance[index]))

    best_index = None
    best_distance = float('inf')

    for index, distance in index_distance_tuples:
        if distance < best_distance:
            best_distance = distance
            best_index = index

    return best_index