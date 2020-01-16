%https://github.com/swatijais57/semi-streaming-matching-algo.git
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from networkx import nx

n = 10  # 10 nodes
m = 20  # 20 edges

G = nx.gnm_random_graph(n, m)

# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print('%s %d %f' % (v, nx.degree(G, v), nx.clustering(G, v)))

# print the adjacency list
for line in nx.generate_adjlist(G):
    print(line)

nx.draw(G)
plt.show()
