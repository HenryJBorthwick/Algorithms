def key_positions(a, key):
    k = max(key(a) for a in a)
    c = [0] * (k + 1)
    
    for a in a:
        c[key(a)] = c[key(a)] + 1
    sum = 0

    for i in range(k + 1):
        c[i], sum = sum, (sum + c[i])
    
    return c

def sorted_array(A, key):
    # Create an output array B with the same size as A
    B = [None] * len(A)
    
    # Get positions array
    P = key_positions(A, key)
    
    # Populate the output array with elements from A in sorted order
    for a in reversed(A):  # Reverse to maintain stability
        B[P[key(a)]] = a
        P[key(a)] = P[key(a)] + 1

    # Return the sorted array
    return B

# Include key_positions function here (from previous example)

# Example usage:
print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))