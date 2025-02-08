def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    exp = 1
    
    # Loop through each digit's place value
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Example usage
arr = [31, 22, 131, 44]
radix_sort(arr)
print("Sorted array:", arr)
Explanation: