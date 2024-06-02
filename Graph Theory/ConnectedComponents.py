import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
import matplotlib.pyplot as plt

nxpdParams['show'] = 'ipynb'

G = nx.Graph()
G.add_edges_from([('a', 'b'), ('t', 'c'), ('b', 'x'), ('c', 'q'), ('q', 't')])

pos = nx.nx_agraph.pygraphviz_layout(G, prog='circo')

nx.draw(G, pos, with_labels=True)
plt.show()

print("G has {} connected components".format(nx.number_connected_components(G)))
for cc in nx.connected_components(G):
    print(cc)

