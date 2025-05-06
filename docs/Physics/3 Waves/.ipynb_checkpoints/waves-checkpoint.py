import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider
from IPython.display import display

def wave_interference(n_sources, grid_size=500):
    # Constants for wave calculation
    A = 1  # amplitude
    k = 2 * np.pi / 20  # wave number
    omega = 2 * np.pi / 50  # angular frequency
    t = 0  # static time for visualization

    # Grid for calculation
    x = np.linspace(-grid_size / 2, grid_size / 2, grid_size)
    y = np.linspace(-grid_size / 2, grid_size / 2, grid_size)
    X, Y = np.meshgrid(x, y)

    # Polygon vertices (source positions)
    angles = np.linspace(0, 2 * np.pi, n_sources, endpoint=False)
    sources = np.array([np.cos(angles), np.sin(angles)]).T * (grid_size / 3)  # Position the sources

    # Calculate wave interference
    Z = np.zeros(X.shape)
    for sx, sy in sources:
        R = np.sqrt((X - sx) ** 2 + (Y - sy) ** 2)
        Z += A * np.sin(k * R - omega * t)

    # Normalize the wave pattern for color mapping
    Z_min, Z_max = Z.min(), Z.max()
    Z = (Z - Z_min) / (Z_max - Z_min)

    # Plotting
    plt.figure(figsize=(8, 8))
    plt.imshow(Z, extent=(-grid_size/2, grid_size/2, -grid_size/2, grid_size/2), cmap='viridis')
    plt.title(f'Wave Interference Pattern with {n_sources} Sources')
    plt.axis('off')
    plt.show()

# Create a slider for selecting the number of sources
slider = IntSlider(value=3, min=1, max=100, step=1, description='Sources:')
display(slider)

# Interactive plotting
interact(wave_interference, n_sources=slider)