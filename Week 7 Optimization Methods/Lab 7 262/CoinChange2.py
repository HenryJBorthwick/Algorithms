from collections import defaultdict

def change_greedy(V, coinage):
    coinage.sort()  # Sort coinage in ascending order
    counts = defaultdict(int)   # Coin counters
    imax = len(coinage) - 1

    while V > 0:
        while coinage[imax] > V:
            imax -= 1
            if imax < 0:
                return None  # Exit the loop if no suitable coin found (exact breakdown not possible)
        cimax = coinage[imax]
        counts[cimax] += 1
        V -= cimax

    return counts

# Test cases
print(change_greedy(82, [1, 10, 25, 5]))  # Output: [(3, 25), (1, 5), (2, 1)]
print(change_greedy(80, [1, 10, 25]))    # Output: [(3, 25), (5, 1)]
print(change_greedy(82, [10, 25, 5]))    # Output: None