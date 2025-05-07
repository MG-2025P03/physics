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
    pos = nx.spring_layout(G)  # Layout for better visualization
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{w}Ω' for u, v, w in G.edges(data='weight')})
    plt.title(title)
    plt.axis('off')
    plt.show()

def reduce_graph(G, step=0):
    """Recursive reduction of the graph."""
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

        # Mark the middle node in the series connection for removal
        path_between = list(nx.all_shortest_paths(G, source=n1, target=n2))
        for path in path_between:
            if len(path) == 3:
                nodes_to_remove.extend(path[1:-1])

    G.remove_nodes_from(set(nodes_to_remove))

    # Check for and reduce parallel connections:
    edges_to_check = list(G.edges(keys=True, data=True))
    for u, v, key, data in edges_to_check:
        if G.number_of_edges(u, v) > 1:
            parallel_resistances = [
                edge_data['weight'] for edge_data in G.get_edge_data(u, v).values()
            ]
            # Calculate equivalent resistance
            parallel_resistance = equivalent_resistance_parallel(parallel_resistances)
            # Remove all parallel edges and add a single equivalent one
            G.remove_edges_from([(u, v, k) for k in range(G.number_of_edges(u, v))])
            G.add_edge(u, v, weight=parallel_resistance)

    # Visualize current graph state
    draw_graph(G, f"Graph After Step {step}")

    # If any reductions were made, continue to reduce recursively
    if nodes_to_remove or edges_to_modify:
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