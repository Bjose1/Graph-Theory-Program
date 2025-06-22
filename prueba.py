import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()
G.add_edge("X", "Y", relation="amigo", weight=1)
G.add_edge("Y", "X", relation="jefe", weight=3)

# Visualización
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", connectionstyle="arc3,rad=0.2")  # Curva las aristas
edge_labels = {(u, v): f"{d['relation']} ({d['weight']})" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Multigrafo Dirigido con NetworkX")
plt.show()