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



#Test
in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))  

#Output:
# 4

#TEST:
in_tree = [False, False, False]
distance = [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))

#OUTPUT
# 1

#TEST	
from math import inf
in_tree = [True, True, True, False, True]
distance = [inf, 0, inf, inf, inf]
print(next_vertex(in_tree, distance))

#OUTPUT:
# 3

