def key_positions(seq, key):
    # Find the maximum key value in the input list seq
    k = max(key(a) for a in seq)

    # Create a new list C of length k+1, initialized with zeros
    C = [0] * (k + 1)

    # Iterate through the elements in seq
    for a in seq:
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

def sorted_array(seq, key, positions): #ESSENTIALLY COUNTING-SORT
    # Create an output array B with the same size as seq
    B = [0] * len(seq)

    # Iterate through each element in the input sequence
    for a in seq:
        # Compute the key value for the current element
        key_value = key(a)

        # Place the current element into the output array B based on the key value and the corresponding position in positions
        B[positions[key_value]] = a

        # Increment the position value in positions for the current key value
        positions[key_value] += 1

    # Return the sorted output array B
    return B

def counting_sort(iterable, key):
    # Generate the positions array using the key_positions function
    positions = key_positions(iterable, key)

    # Sort the iterable using the sorted_array function and return the sorted result
    return sorted_array(iterable, key, positions)


# Test cases
print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
# Output: [1, 2, 3]

print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
# Output: [1, 2, 2, 2, 3]

print(sorted_array([100], lambda x: x, [0] * 101))
# Output: [100]

import operator

objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

key = operator.itemgetter(1)
print(", ".join(object[0] for object in counting_sort(objects, key)))
# Output: d, b, c, a
