def floyd_warshall(distance_matrix, k):
    n = len(distance_matrix)

    # Perform one iteration of Floyd's algorithm for k value
    for i in range(n):
        for j in range(n):
            if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]

    return distance_matrix

# Input distance matrix
distance_matrix = [
    [0,     5,   4,  float('inf')],
    [-4,    0,  -1,  float('inf')],
    [3,     8,   0,       4],
    [float('inf'), float('inf'), 2, 0]
]

# k value
k = 2

# Update the distance matrix using Floyd's algorithm for k value
updated_distance_matrix = floyd_warshall(distance_matrix, k)

# Print the updated distance matrix
for row in updated_distance_matrix:
    print(row)
