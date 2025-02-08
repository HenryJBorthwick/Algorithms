def lcs(s1, s2):
    # Create the DP table, initialized to 0
    dp_table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # Fill in the DP table
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    # Now, we'll trace back through the table to find the LCS
    lcs_string = ''
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_string = s1[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp_table[i - 1][j] > dp_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_string

# TEST
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2)) 

# OUTPUT
# Look at ,  a fly

# TEST
s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

# OUTPUT

# TEST
s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))

# OUTPUT
# balderdash!

# TEST
s1 = 1500 * 'x'
s2 = 1500 * 'y'
print(lcs(s1, s2))

# OUTPUT