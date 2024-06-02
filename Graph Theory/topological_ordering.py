import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
import matplotlib.pyplot as plt
nxpdParams['show'] = 'ipynb'

G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd')])

pos = nx.nx_agraph.pygraphviz_layout(G, prog='circo')
nx.draw(G, pos, with_labels=True)
plt.show()

if nx.is_directed_acyclic_graph(G):
    print("Topological ordering of the nodes:", list(nx.topological_sort(G)))
else:
    print("G contains a cycle, hence it cannot be topologically sorted.")

pos = nx.nx_agraph.pygraphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True)
plt.show()
