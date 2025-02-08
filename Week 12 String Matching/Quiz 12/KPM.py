def border_lengths(p):
    """Computes lengths of p-segment borders"""
    b = [0] * (len(p) + 1)
    b[0:2] = [-1, 0]
    j, bj = 1, 0
    while j < len(p):
        while bj >= 0 and (p[j] != p[bj]):
            bj = b[bj]
        j, bj = j + 1, bj + 1
        b[j] = bj
    return b

def KMP_search(pattern, text):
    b = border_lengths(pattern)
    i, j = 0, 0
    while i < len(text):
        while j >= 0 and text[i] != pattern[j]:
            j = b[j]
        i, j = i + 1, j + 1
        if j == len(pattern):
            # Match found. Print position.
            print(i - j)
            j = b[j]

# Testing the function
text = "Hello, this is a sample text."
pattern = "sample"
KMP_search(pattern, text)
