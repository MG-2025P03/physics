# List of Codes

### Sample Circuit

```python
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
````

### Series Connection

````python
import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph for the series circuit
G = nx.Graph()

# Define nodes to represent junctions
G.add_nodes_from(["A", "B", "C", "D"])

# Define edges with weights to represent resistors in series
# Each pair of nodes is connected by a resistor, representing a series connection
resistors = {
    ("A", "B"): 5,   # Resistor between A and B with 5 ohms
    ("B", "C"): 10,  # Resistor between B and C with 10 ohms
    ("C", "D"): 15   # Resistor between C and D with 15 ohms
}

# Add edges to the graph with the respective resistance weights
for (node1, node2), resistance in resistors.items():
    G.add_edge(node1, node2, weight=resistance)

# Define positions for a linear layout to represent series connection
pos = {
    "A": (0, 1),
    "B": (1, 1),
    "C": (2, 1),
    "D": (3, 1),
}

# Draw the graph
plt.figure(figsize=(8, 4))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')

# Draw edge labels to show resistance values
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})

plt.title("Graph Representation of Series Circuit")
plt.axis('off')
plt.show()
````

### Parallel Connection

````python
import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph for the parallel circuit
G = nx.Graph()

# Define nodes to represent junctions
G.add_nodes_from(["A", "B", "C", "D"])

# Define edges with weights to represent resistors in parallel
# Each resistor shares the same two nodes (A and B), illustrating parallel connection
resistors = {
    ("A", "B"): 5,   # Resistor R1 between A and B with 5 ohms
    ("A", "C"): 10,  # Resistor R2 between A and C with 10 ohms
    ("A", "D"): 15   # Resistor R3 between A and D with 15 ohms
}

# Add edges to the graph with the respective resistance weights
for (node1, node2), resistance in resistors.items():
    G.add_edge(node1, node2, weight=resistance)

# Define a position layout to represent the parallel connection
pos = {
    "A": (0, 1),
    "B": (1, 2),
    "C": (1, 1),
    "D": (1, 0),
}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')

# Draw edge labels to show resistance values
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})

plt.title("Graph Representation of Parallel Circuit")
plt.axis('off')
plt.show()
````

### Recursive

````python
import networkx as nx
import matplotlib.pyplot as plt

def equivalent_resistance_series(resistances):
    """Calculate equivalent resistance for resistors in series."""
    return sum(resistances)

def equivalent_resistance_parallel(resistances):
    """Calculate equivalent resistance for resistors in parallel."""
    return 1 / sum(1 / r for r in resistances if r != 0)  # Protect against division by zero

def draw_graph(G, title):
    """Helper function to draw the graph."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})
    plt.title(title)
    plt.axis('off')
    plt.show()

def reduce_graph(G, step=0):
    """Recursive reduction of the graph."""
    nodes_to_remove = []
    keys_to_remove = []

    # Check for series connections:
    for node in list(G.nodes):
        if G.degree[node] == 2:  # A series node has exactly two connections
            neighbors = list(G.neighbors(node))
            if len(neighbors) == 2:
                n1, n2 = neighbors
                # Calculate equivalent resistance for this series connection
                resistances = [data['weight'] for _, _, data in G.edges(node, data=True)]
                series_resistance = equivalent_resistance_series(resistances)

                # Add a direct edge between n1 and n2
                if G.has_edge(n1, n2):
                    # Accumulate the resistance in an existing edge
                    edge_keys = list(G[n1][n2])
                    G[n1][n2][edge_keys[0]]['weight'] += series_resistance
                else:
                    # Add a new edge
                    G.add_edge(n1, n2, weight=series_resistance)

                nodes_to_remove.append(node)

    G.remove_nodes_from(nodes_to_remove)

    # Check for parallel connections:
    edges_to_check = list(G.edges(keys=True, data=True))
    for u, v, key, data in edges_to_check:
        parallel_resistances = []

        # Look for parallel edges
        if G.number_of_edges(u, v) > 1:
            # Gather all parallel resistances
            for k in G[u][v]:
                parallel_resistances.append(G[u][v][k]['weight'])
                keys_to_remove.append((u, v, k))

            # Calculate equivalent resistance
            parallel_resistance = equivalent_resistance_parallel(parallel_resistances)

            # Remove all parallel edges and add a single equivalent one
            for u, v, k in keys_to_remove:
                G.remove_edge(u, v, k)

            G.add_edge(u, v, weight=parallel_resistance)

    # Visualize current graph state
    draw_graph(G, f"Graph After Step {step}")

    # If any reductions were made, continue to reduce recursively
    if nodes_to_remove or keys_to_remove:
        reduce_graph(G, step + 1)

def print_graph(G):
    """Helper function to print graph edges with resistance values."""
    print("Graph edges with resistance values:")
    for u, v, data in G.edges(data=True):
        print(f"{u} -- {v} with resistance {data['weight']}Ω")

# Create a complex graph
G = nx.MultiGraph()
# Add nodes and resistors with varying connections for a more complex setup
G.add_weighted_edges_from([
    ('A', 'B', 5),
    ('B', 'C', 10),
    ('C', 'D', 15),
    ('D', 'E', 20),
    ('A', 'C', 2),
    ('C', 'E', 3),
    ('B', 'E', 4)
])

# Initial graph printout
print("Initial Graph:")
print_graph(G)
draw_graph(G, "Initial Graph")

# Reduce the graph
reduce_graph(G)

# Reduced graph printout
print("\nReduced Graph:")
print_graph(G)
````