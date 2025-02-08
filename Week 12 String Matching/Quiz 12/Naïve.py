def naive_string_search(T, P):
    n = len(T)
    m = len(P)

    for shift in range (0, n-m +1):
        j = 0
        while j < m and T[shift+j] == P[j]:
            j = j+1
        if j == m:
            print (shift)

text = "Hello, this is a sample text."
pattern = "sample"
naive_string_search(text, pattern)
