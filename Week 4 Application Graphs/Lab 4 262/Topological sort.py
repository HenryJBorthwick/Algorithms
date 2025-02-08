def topological_sort(graph_str):
    # parse graph string
    lines = graph_str.strip().split('\n')
    n = int(lines[0].split()[1])
    adj_list = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v = map(int, line.split())
        adj_list[u].append(v)

    # initialize state and parent arrays
    state = ["U"] * n
    parent = [-1] * n
    stack = []

    # modified version of DFSLoop
    def dfs(u):
        state[u] = "D"
        for v in adj_list[u]:
            if state[v] == "U":
                parent[v] = u
                dfs(v)
        state[u] = "P"
        stack.append(u)

    # iterate over all vertices of the graph
    for u in range(n):
        if state[u] == "U":
            dfs(u)

    # return the content of the stack from top to bottom as a topological ordering
    return stack[::-1]


graph_str = "D 4\n0 3"
ordering = topological_sort(graph_str)
print(ordering)
