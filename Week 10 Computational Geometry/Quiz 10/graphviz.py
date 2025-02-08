from graphviz import Graph

g = Graph()
g.node('Root', '23')
g.node('Leaf1', '13', shape='box')
g.node('Leaf2', '99', shape='box')
g.edge('Root', 'Leaf1')
g.edge('Root', 'Leaf2')
g.render('graph', format='png', view=True)