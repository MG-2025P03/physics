import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph for the circuit
G = nx.Graph()

# Define nodes to represent junctions
G.add_nodes_from(["A", "B", "C", "D"])

# Define edges with weights to represent resistors and their resistance values
# Edges between nodes represent resistors, with weights as resistance values in ohms
resistors = {
    ("A", "B"): 5,   # Resistor between A and B with 5 ohms
    ("B", "C"): 10,  # Resistor between B and C with 10 ohms
    ("C", "D"): 15,  # Resistor between C and D with 15 ohms
    ("A", "D"): 20   # Resistor between A and D with 20 ohms
}

# Add edges to the graph with the respective resistance weights
for (node1, node2), resistance in resistors.items():
    G.add_edge(node1, node2, weight=resistance)

# Define positions for a clear layout
pos = {
    "A": (0, 1),
    "B": (1, 2),
    "C": (2, 1),
    "D": (3, 0),
}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')

# Draw edge labels to indicate resistance values
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})

plt.title("Graph Representation of Circuit with Resistances")
plt.axis('off')
plt.show()