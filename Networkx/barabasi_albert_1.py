import networkx as nx
import matplotlib.pyplot as plt

n = 150
m = 3
g_barabasi = nx.barabasi_albert_graph(n, m)

plt.figure(figsize=(12, 8))
nx.draw(g_barabasi, node_size=10)
plt.show()