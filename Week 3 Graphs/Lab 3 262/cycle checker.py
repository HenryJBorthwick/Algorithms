def has_cycle_dfs(G):
    visited = set()
    for v in G.nodes():
        if v not in visited:
            if dfs_helper(G, v, visited, None):
                return True
    return False

def dfs_helper(G, v, visited, parent):
    visited.add(v)
    for neighbor in G.neighbors(v):
        if neighbor not in visited:
            if dfs_helper(G, neighbor, visited, v):
                return True
        elif neighbor != parent:
            return True
    return False

import networkx as nx
import matplotlib.pyplot as plt

def create_graph_from_string(input_str):
    # split input into lines
    lines = input_str.strip().split('\n')

    # extract graph type and number of nodes from first line
    graph_type, num_nodes = lines[0].split()

    # create empty graph of the specified type
    if graph_type == 'U':
        G = nx.Graph()
    elif graph_type == 'D':
        G = nx.DiGraph()
    else:
        raise ValueError('Invalid graph type')

    # add nodes to graph
    for i in range(int(num_nodes)):
        G.add_node(i)

    # add edges to graph
    for line in lines[1:]:
        u, v = line.split()
        G.add_edge(int(u), int(v))

    return G

input_str = """U 6
0 4
5 4
4 2
2 3
3 0
3 4
"""
G = create_graph_from_string(input_str)
print(has_cycle_dfs(G))  # True
