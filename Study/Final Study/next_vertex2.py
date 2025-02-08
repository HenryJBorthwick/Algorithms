# The function Next-Vertex(in-tree, distance) returns a closest vertex
# that is not yet part of the tree; 


def next_vertex(in_tree, distances):
    tuples = []

    for count, bol in enumerate(in_tree):
        if not bol:
            tuples.append((count, distances[count]))
    
    best_distance = float('inf')
    best_index = None

    for count, distance in tuples:
        if distance < best_distance:
            best_distance = distance
            best_index = count

    return best_index