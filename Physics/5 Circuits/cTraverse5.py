import networkx as nx
import matplotlib.pyplot as plt

def equivalent_resistance_series(resistances):
    """Calculate equivalent resistance for resistors in series."""
    return sum(resistances)

def equivalent_resistance_parallel(resistances):
    """Calculate equivalent resistance for resistors in parallel."""
    return 1 / sum(1 / r for r in resistances if r != 0)

def draw_graph(G, title):
    """Helper function to draw the graph with resistances."""
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)  # Fixed seed for consistent layout
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})
    plt.title(title)
    plt.axis('off')
    plt.show()

def reduce_graph(G):
    """Recursive reduction of the graph and store intermediate graphs."""
    graphs = [G.copy()]  # Store the initial graph

    def recursive_reduce(G, graphs):
        changed = False  # Flag to indicate if any reduction was made

        nodes_to_remove = []
        edges_to_modify = []

        # Check for series connections:
        for node in list(G.nodes):
            if G.degree[node] == 2:  # A series node has exactly two connections
                neighbors = list(G.neighbors(node))
                if len(neighbors) == 2:
                    n1, n2 = neighbors
                    # Calculate equivalent resistance for this series connection
                    resistances = [data['weight'] for _, _, data in G.edges(node, data=True)]
                    series_resistance = equivalent_resistance_series(resistances)

                    edges_to_modify.append((n1, n2, series_resistance))
                    nodes_to_remove.append(node)
                    changed = True

        # Apply series reduction
        for n1, n2, series_resistance in edges_to_modify:
            # Add a direct edge between n1 and n2
            if G.has_edge(n1, n2):
                # Accumulate the resistance in an existing edge
                edge_data = list(G.get_edge_data(n1, n2).values())[0]
                edge_data['weight'] += series_resistance
            else:
                # Add a new edge
                G.add_edge(n1, n2, weight=series_resistance)

        G.remove_nodes_from(nodes_to_remove)

        # Check for and reduce parallel connections:
        edges_to_check = list(G.edges(data=True, keys=True))
        for u, v, key, _ in edges_to_check:
            if G.number_of_edges(u, v) > 1:
                parallel_resistances = [
                    edge_data['weight'] for edge_data in G.get_edge_data(u, v).values()
                ]
                # Calculate equivalent resistance
                parallel_resistance = equivalent_resistance_parallel(parallel_resistances)
                # Remove all parallel edges and add a single equivalent one
                G.remove_edges_from([(u, v, k) for k in list(G[u][v])])
                G.add_edge(u, v, weight=parallel_resistance)
                changed = True

        # Only recurse if changes were made
        if changed:
            graphs.append(G.copy())  # Add current state to list
            recursive_reduce(G, graphs)

    recursive_reduce(G, graphs)
    return graphs

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

# Print initial graph details and visualize it
print("Initial Graph:")
print_graph(G)

# Reduce the graph and get all intermediate graphs
graphs = reduce_graph(G)

# Calculate indices for the graphs to display: first, some middle ones, and the last
n = len(graphs)
if n > 5:
    indices_to_display = [0, n // 4, n // 2, 3 * n // 4, n - 1]
else:
    indices_to_display = range(n)

# Display selected graphs
for i in indices_to_display:
    draw_graph(graphs[i], f"Graph at Step {i}")

# Final Reduced graph printout
print("\nReduced Graph:")
print_graph(G)