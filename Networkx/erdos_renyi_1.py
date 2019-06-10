import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

n = 50
p = 0.2

g_erdos = nx.erdos_renyi_graph(n, p, seed = 100)

degree = list(g_erdos.degree())
print(degree)
print(np.array(degree))
print(np.array(degree)[:, 1])
print(max(np.array(degree)[:, 1]))
edges = len(g_erdos.edges())
print(f"edges: {edges}")

plt.figure(figsize=(12, 8))
nx.draw(g_erdos, node_size=10)
plt.show()