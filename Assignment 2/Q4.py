from collections import deque

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: 
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    # Backtrack to find the sequence
    i, j = m, n
    lcs_str = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str = s1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif C[i - 1][j] >= C[i][j - 1]:  # modified condition
            i -= 1
        else:
            j -= 1
    return lcs_str

def lcs_and_mark_extras(s1, s2):
    lcs_str = lcs(s1, s2)
    lcs_deque = deque(lcs_str)
    
    def mark_extras(s, lcs_deque):
        result = []
        for c in s:
            if lcs_deque and lcs_deque[0] == c:
                lcs_deque.popleft()
                result.append(c)
            else:
                result.append(f"[[{c}]]")
        return "".join(result)

    return mark_extras(s1, lcs_deque.copy()), mark_extras(s2, lcs_deque.copy())

def line_edits(s1, s2):
    lines1 = s1.splitlines()
    lines2 = s2.splitlines()

    n = len(lines1)
    m = len(lines2)
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    op = [[''] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost[i][0] = i
        op[i][0] = 'D'
    for j in range(1, m + 1):
        cost[0][j] = j
        op[0][j] = 'I'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delete_cost = cost[i - 1][j] + 1
            insert_cost = cost[i][j - 1] + 1
            if lines1[i - 1] == lines2[j - 1]:
                copy_cost = cost[i - 1][j - 1]
                min_cost = min(delete_cost, insert_cost, copy_cost)
                if min_cost == copy_cost:
                    op[i][j] = 'C'
                elif min_cost == delete_cost:
                    op[i][j] = 'D'
                else:
                    op[i][j] = 'I'
            else:
                substitute_cost = cost[i - 1][j - 1] + 1
                min_cost = min(delete_cost, insert_cost, substitute_cost)
                if min_cost == substitute_cost:
                    op[i][j] = 'S'
                elif min_cost == delete_cost:
                    op[i][j] = 'D'
                else:
                    op[i][j] = 'I'
            cost[i][j] = min_cost

    operations = []
    i, j = n, m
    while i > 0 or j > 0:
        if op[i][j] == 'C':
            operations.append(('C', lines1[i - 1], lines2[j - 1]))
            i -= 1
            j -= 1
        elif op[i][j] == 'S':
            left, right = lcs_and_mark_extras(lines1[i - 1], lines2[j - 1])
            operations.append(('S', left, right))
            i -= 1
            j -= 1
        elif op[i][j] == 'D':
            operations.append(('D', lines1[i - 1], ''))
            i -= 1
        else:  # op[i][j] == 'I'
            operations.append(('I', '', lines2[j - 1]))
            j -= 1

    operations.reverse()
    return operations

# TEST:
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

# OUTPUT:
# ('S', 'Line[[1]]', 'Line[[5]]')
# ('S', '[[L]]ine[[ ]]2[[a]]', '[[l]]ine2')
# ('C', 'Line3', 'Line3')
# ('D', 'Line4', '')