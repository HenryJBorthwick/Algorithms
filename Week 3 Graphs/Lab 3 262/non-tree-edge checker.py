from collections import deque

# input graph as a string
graph_str = """
U 6
0 4
5 4
4 2
2 3
3 0
3 4
"""

# starting vertex
start_vertex = 1

# parse graph string
lines = graph_str.strip().split('\n')
n = int(lines[0].split()[1])
adj_list = [[] for _ in range(n)]
for line in lines[1:]:
    u, v = map(int, line.split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# perform BFS
# visited = [False] * n
# parent = [-1] * n
# queue = deque([start_vertex])
# visited[start_vertex] = True
# while queue:
#     u = queue.popleft()
#     for v in adj_list[u]:
#         if not visited[v]:
#             visited[v] = True
#             parent[v] = u
#             queue.append(v)

# perform DFS
visited = [False] * n
parent = [-1] * n
stack = [start_vertex]
visited[start_vertex] = True
while stack:
    u = stack.pop()
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            stack.append(v)

# check for non-tree edges
count_non_tree_edges = 0
for u in range(n):
    for v in adj_list[u]:
        if parent[u] != v and parent[v] != u:
            print(f"{u} - {v} is a non-tree edge")
            count_non_tree_edges += 1

print(f"The number of non-tree edges starting from vertex {start_vertex} is {count_non_tree_edges}.")