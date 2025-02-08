def line_edits(s1, s2):
    # Split the input strings into lines
    lines1 = s1.splitlines()
    lines2 = s2.splitlines()

    # Initialize the cost matrix and the operation matrix
    n = len(lines1)
    m = len(lines2)
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    op = [[''] * (m + 1) for _ in range(n + 1)]

    # Fill in the base cases for the cost and operation matrices
    for i in range(1, n + 1):
        cost[i][0] = i
        op[i][0] = 'D'  # Delete operation
    for j in range(1, m + 1):
        cost[0][j] = j
        op[0][j] = 'I'  # Insert operation

    # Fill in the rest of the cost and operation matrices
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delete_cost = cost[i - 1][j] + 1
            insert_cost = cost[i][j - 1] + 1
            if lines1[i - 1] == lines2[j - 1]:
                copy_cost = cost[i - 1][j - 1]
                min_cost = min(delete_cost, insert_cost, copy_cost)
                if min_cost == copy_cost:
                    op[i][j] = 'C'  # Copy operation
                elif min_cost == delete_cost:
                    op[i][j] = 'D'  # Delete operation
                else:
                    op[i][j] = 'I'  # Insert operation
            else:
                substitute_cost = cost[i - 1][j - 1] + 1
                min_cost = min(delete_cost, insert_cost, substitute_cost)
                if min_cost == substitute_cost:
                    op[i][j] = 'S'  # Substitute operation
                elif min_cost == delete_cost:
                    op[i][j] = 'D'  # Delete operation
                else:
                    op[i][j] = 'I'  # Insert operation
            cost[i][j] = min_cost

    # Backtrace through the operation matrix to construct the list of operations
    i, j = n, m
    operations = []
    while i > 0 or j > 0:
        if op[i][j] == 'C':
            operations.append(('C', lines1[i - 1], lines2[j - 1]))
            i -= 1
            j -= 1
        elif op[i][j] == 'S':
            operations.append(('S', lines1[i - 1], lines2[j - 1]))
            i -= 1
            j -= 1
        elif op[i][j] == 'D':
            operations.append(('D', lines1[i - 1], ''))
            i -= 1
        elif op[i][j] == 'I':
            operations.append(('I', '', lines2[j - 1]))
            j -= 1

    # Since we backtraced from the bottom-right, the operations are in reverse order
    operations = operations[::-1]

    return operations

# TEST:
# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line1\nLine3\nLine4\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)

# OUTPUT:
# ('C', 'Line1', 'Line1')
# ('D', 'Line2', '')
# ('C', 'Line3', 'Line3')
# ('C', 'Line4', 'Line4')
# ('I', '', 'Line5')

# TEST:
# s1 = "Line1\nLine2\nLine3\nLine4\n"
# s2 = "Line5\nLine4\nLine3\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)

# OUTPUT:
# ('S', 'Line1', 'Line5')
# ('S', 'Line2', 'Line4')
# ('C', 'Line3', 'Line3')
# ('D', 'Line4', '')