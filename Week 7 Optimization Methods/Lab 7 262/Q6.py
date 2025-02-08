def fractional_knapsack(capacity, items):
    # Sort items in descending order of value-to-weight ratio (bi/wi)
    # key does the computation and sorts according to that value
    # reverse=True means decending order
    sorted_items = sorted(items, key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0
    for item in sorted_items:
        name, value, weight = item

        # If the item can fit entirely into the remaining capacity, add it
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            # If only a fraction of the item can fit, add the fraction and break the loop
            fraction = capacity / weight
            total_value += value * fraction
            break #Finished no longer needs to run

    return total_value

# Test
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))  # Output: 45.0
