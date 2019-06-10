import networkx as nx
import matplotlib.pyplot as plt
n = 50
p = 0.2

g_erdos = nx.erdos_renyi_graph(n, p, seed = 100)
plt.figure(figsize=(12, 8))
nx.draw(g_erdos, node_size=10)
plt.show()