# strongly connected components

import networkx as nx
import pygraphviz as pgv
from matplotlib import pyplot as plt
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd'), ('e', 'd'), ('f', 'a'), ('b', 'f')])
pos = nx.nx_agraph.graphviz_layout(G, prog='circo')
nx.draw(G, pos=pos, with_labels=True)
plt.show()

print("Strongly connected components:")
for scc in nx.strongly_connected_components(G):
    print(scc)

