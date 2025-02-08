def key_positions(A, key):
    # Find the maximum key value in the input list A
    k = max(key(a) for a in A)
    
    # Create a new list C of length k+1, initialized with zeros
    C = [0] * (k + 1)
    
    # Iterate through the range from 0 to k (inclusive) and set each value in C to 0
    # Note: This step is actually redundant, as we have already initialized C with zeros
    for i in range(0, k + 1):
        C[i] = 0
    
    # Iterate through the elements in A
    for a in A:
        # Increment the count of the key value at the corresponding index in C
        C[key(a)] = C[key(a)] + 1
    
    # Initialize a variable to store the cumulative sum
    sum_ = 0
    
    # Iterate through the range from 0 to k (inclusive)
    for i in range(0, k + 1):
        # Update the value of C[i] to the cumulative sum, and update the sum_ variable
        C[i], sum_ = sum_, sum_ + C[i]
    
    # Return the modified list C
    return C

def counting_sort(A, key):
    # Function to perform counting sort on the input array A using the key function.

    # Create an output array B with the same size as A.
    B = [0] * len(A)

    # Call key_positions function to get the prefix sum array P.
    P = key_positions(A, key)

    # Iterate through each element in the input array A.
    for a in A:
        # Compute the key value for the current element.
        key_value = key(a)

        # Place the current element into the output array B based on the key value and the corresponding position in P.
        B[P[key_value]] = a

        # Increment the position value in P for the current key value.
        P[key_value] += 1

    # Return the sorted output array B.
    return B

# Example usage:
A = [2, -2, 1]
key = lambda x: x * x
sorted_array = counting_sort(A, key)
print(sorted_array)