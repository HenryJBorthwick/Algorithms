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
            bset_index = index

    return best_index