from collections import defaultdict

def change_greedy(V, coinage):
    coinage.sort(reverse=True)  # Sort coinage in descending order
    counts = defaultdict(int)   # Counters of all coins

    while V > 0:
        for ci in coinage:
            if ci <= V:
                counts[ci] += 1
                V -= ci
                break
        else:
            return None  # Exit the loop if no suitable coin found (exact breakdown not possible)

    return counts

# Test cases
print(change_greedy(82, [1, 10, 25, 5]))  # Output: [(3, 25), (1, 5), (2, 1)]
print(change_greedy(80, [1, 10, 25]))    # Output: [(3, 25), (5, 1)]
print(change_greedy(82, [10, 25, 5]))    # Output: None