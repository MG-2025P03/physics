import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parameters
a = 1.0          # Half side length of the polygon
A = 1.0          # Amplitude of the waves
wavelength = 1.0 # Wavelength
omega = 2 * np.pi # Angular frequency
k = 2 * np.pi / wavelength # Wave number
t = 0            # Time instance for snapshot
grid_size = 200  # Resolution of the grid
domain_size = 3  # Size of the domain for visualization

# Create a grid of points
x = np.linspace(-domain_size, domain_size, grid_size)
y = np.linspace(-domain_size, domain_size, grid_size)
X, Y = np.meshgrid(x, y)

# Function to calculate positions of sources placed at vertices of a regular polygon
def get_polygon_sources(num_sources, radius):
    theta = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
    return [(radius * np.cos(angle), radius * np.sin(angle)) for angle in theta]

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.25)  # Adjust layout to make space for slider

# Plot initial data
num_sources_initial = 4  # Start with a square (4 sources)
sources = get_polygon_sources(num_sources_initial, np.sqrt(2) * a)
Psi = np.zeros_like(X)

for (x0, y0) in sources:
    R = np.sqrt((X - x0)**2 + (Y - y0)**2)
    Psi += A * np.sin(k * R - omega * t)

contour = plt.contourf(X, Y, Psi, levels=100, cmap='RdYlBu')
plt.colorbar(contour, label='Wave Intensity')
ax.set_title('Interference Pattern of Waves from Polygon Vertex Sources')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_aspect('equal', adjustable='box')

# Slider for number of sources
ax_sources = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_sources = Slider(ax_sources, 'Number of Sources', 3, 12, valinit=num_sources_initial, valstep=1)

# Update function for slider interaction
def update(val):
    num_sources = int(slider_sources.val)
    Psi = np.zeros_like(X)
    sources = get_polygon_sources(num_sources, np.sqrt(2) * a)
    for (x0, y0) in sources:
        R = np.sqrt((X - x0)**2 + (Y - y0)**2)
        Psi += A * np.sin(k * R - omega * t)

    ax.clear()
    contour = ax.contourf(X, Y, Psi, levels=100, cmap='RdYlBu')
    ax.set_title('Interference Pattern of Waves from Polygon Vertex Sources')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_aspect('equal', adjustable='box')
    plt.colorbar(contour, ax=ax, label='Wave Intensity')

slider_sources.on_changed(update)

plt.show()