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

def radix_sort(A, d):
    # Function to extract the i-th digit of a number
    def get_digit(number, i):
        # Divide the number by 10^(i-1) and take the remainder when divided by 10 to get the i-th digit
        return (number // (10 ** (i - 1))) % 10

    # Define the counting sort algorithm for a stable sort
    def counting_sort(iterable, key):
        positions = key_positions(iterable, key)
        return sorted_array(iterable, key, positions)

    # Main loop: Iterate through each digit from 1 to d
    for i in range(1, d + 1):
        # Perform a stable sort (using counting sort) on the i-th digit of each element in A
        A = counting_sort(A, lambda x: get_digit(x, i))

    # Return the sorted array A
    return A

# Test cases
input_list = [329, 457, 657, 839, 436, 720, 355]
output_list = radix_sort(input_list, 3)
print(input_list)
print(output_list)

# Output: [329, 457, 657, 839, 436, 720, 355]
#         [329, 355, 436, 457, 657, 720, 839]

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))

# Output: [720, 355, 436, 457, 657, 329, 839]

print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))

# Output: [720, 329, 436, 839, 355, 457, 657]