BASE = 256
Q = 15487469  # Any largish prime

def rabin_karp_search(pat, text):
    m, n = len(pat), len(text)
    hash_p = 0  # hash value for pattern
    hash_t = 0  # hash value for text
    h = 1  # For calculating BASE^m % Q

    # Compute BASE^m % Q
    for i in range(m):
        h = (h * BASE) % Q

    # Computing pattern hash
    for i in range(m):
        hash_p = (BASE * hash_p + ord(pat[i])) % Q

    # Computing window hash for i = 0
    for i in range(m):
        hash_t = (BASE * hash_t + ord(text[i])) % Q

    # For each window position
    for i in range(n - m + 1):
        # Char-by-char comparison only on a hash hit
        if hash_p == hash_t:
            if pat == text[i : i + m]:
                print("Pattern found at index " + str(i))

        # To prevent index error at end
        if i < n - m:
            hash_t = (Q + BASE * hash_t - ord(text[i]) * h + ord(text[i + m])) % Q  # Update hash

# Testing the function
text = "Hello, this is a sample text."
pattern = "sample"
rabin_karp_search(pattern, text)
