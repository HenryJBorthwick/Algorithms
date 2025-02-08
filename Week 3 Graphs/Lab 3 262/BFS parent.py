import queue

def bfs(G, start):
    parent = {start: None}
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        for neighbor in G.neighbors(v):
            if neighbor not in parent:
                parent[neighbor] = v
                q.put(neighbor)
    return parent

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
parent = bfs(G, 1)
print(parent)

#EXAMPLE OUTPUT
#{0: None, 4: 0, 3: 2, 2: 4, 5: 4}
#This indicates that the parent of vertex 0 is None, 
#The parent of vertex 4 is 0
#The parent of vertex 3 is 2, 
#The parent of vertex 2 is 4
#The parent of vertex 5 is 4.