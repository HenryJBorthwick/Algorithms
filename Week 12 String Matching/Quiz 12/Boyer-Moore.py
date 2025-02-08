def bad_char_shifts(pattern):
    delta1 = [-1] * 256
    m = len(pattern)
    for i in range(m):
        delta1[ord(pattern[i])] = i
    return delta1

def good_suffix_shifts(pattern): # NOT IN COURSE
    m = len(pattern)
    delta2 = [0] * m
    k = m - 1
    for i in range(m-2, -1, -1):
        if k < i and delta2[m - 1 - (k - i)] < i - k - 1:
            delta2[i] = delta2[m - 1 - (k - i)]
        else:
            if i < k:
                k = i
            while k >= 0 and pattern[k] == pattern[m - 1 - (i - k)]:
                k -= 1
            delta2[i] = i - k
    return delta2

def boyer_moore(text, pattern):
    delta1 = bad_char_shifts(pattern)
    delta2 = good_suffix_shifts(pattern)
    m = len(pattern)
    i = m - 1
    while i < len(text):
        j = m - 1
        while j >= 0 and pattern[j] == text[i]:
            i -= 1
            j -= 1
        if j < 0:
            print(i + 1)
            i += m + 1
        else:
            x = delta2[j] if delta2[j] > delta1[ord(text[i])] else delta1[ord(text[i])]
            i += x

# Testing the function
text = "Hello, this is a sample text."
pattern = "sample"
boyer_moore(pattern, text)

