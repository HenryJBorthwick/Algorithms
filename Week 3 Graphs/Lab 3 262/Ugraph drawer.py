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

input_str = """
U 4
0 1
0 2
0 3
1 2
1 3
"""
G = create_graph_from_string(input_str)

# plot the graph
pos = nx.spring_layout(G)  # compute node positions using spring layout
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()


input_str = """
U 4
0 1
0 2
0 3
1 2
1 3
"""
G = create_graph_from_string(input_str)
print(G.nodes())
print(G.edges())
