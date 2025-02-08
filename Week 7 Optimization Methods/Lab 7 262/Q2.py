from collections import defaultdict

def change_greedy(amount, coinage):
    # Sort the coinage list in descending order.
    coinage.sort(reverse=True)
    
    # Initialize a defaultdict to store the count of each coin used.
    counts = defaultdict(int)

    # Continue the loop until the amount becomes 0.
    while amount > 0:
        # Initialize the variable found_coin as False.
        found_coin = False
        
        # Set a coin_index variable to keep track of the current coin index in the coinage list.
        coin_index = 0
        
        # Continue the inner loop until a suitable coin is found or we reach the end of the coinage list.
        while not found_coin and coin_index < len(coinage):
            # Get the current coin from the coinage list using the coin_index.
            coin = coinage[coin_index]
            
            # Check if the coin is less than or equal to the remaining amount.
            if coin <= amount:
                # If the coin is suitable, increase its count in the counts dictionary.
                counts[coin] += 1
                
                # Decrease the amount by the value of the coin.
                amount -= coin
                
                # Set found_coin as True since we found a suitable coin.
                found_coin = True
            else:
                # If the coin is not suitable, move to the next coin in the coinage list.
                coin_index += 1

        # If no suitable coin is found, return None (exact breakdown not possible).
        if not found_coin:
            return None

    # Get the items (key-value pairs) from the 'counts' dictionary.
    coin_count_pairs = counts.items()

    # Initialize an empty list to store (count, coin) tuples.
    count_coin_tuples = []

    # Iterate through the items (key-value pairs) in the 'counts' dictionary.
    for coin, count in coin_count_pairs:
        # Check if the count is greater than 0.
        if count > 0:
            # If the count is greater than 0, create a (count, coin) tuple and append it to the list.
            count_coin_tuple = (count, coin)
            count_coin_tuples.append(count_coin_tuple)

   # Sort the list of tuples based on the second element (coin value) in descending order.
    sorted_count_coin_tuples = sorted(count_coin_tuples, key=lambda x: x[1], reverse=True)

    # Return the sorted list of tuples.
    return sorted_count_coin_tuples

# Test cases
print(change_greedy(82, [1, 10, 25, 5]))  # Output: [(3, 25), (1, 5), (2, 1)]
print(change_greedy(80, [1, 10, 25]))    # Output: [(3, 25), (5, 1)]
print(change_greedy(82, [10, 25, 5]))    # Output: None
