def key_positions(seq, key):
    # Find the maximum key value in the input list A
    k = max(key(a) for a in seq)
    
    # Create a new list C of length k+1, initialized with zeros
    C = [0] * (k + 1)
    
    # Iterate through the range from 0 to k (inclusive) and set each value in C to 0
    # Note: This step is actually redundant, as we have already initialized C with zeros
    for i in range(0, k + 1):
        C[i] = 0
    
    # Iterate through the elements in A
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

# Test case 1
print(key_positions([0, 1, 2], lambda x: x))
# Expected output: [0, 1, 2]

# Test case 2
print(key_positions(range(-3, 3), lambda x: x**2))
# Expected output: [0, 1, 3, 3, 3, 5, 5, 5, 5, 5]

# Q3
print(key_positions([2, -2, 1], lambda x: x*x))
# Expected output: [0, 0, 1, 1, 1]

#Seq is the input array
#Key is a lamba function. Key(x) = x^2
#K is the result of the largest value from the key being applied to each item in Seq
#C is an array of 0 of length k+1
