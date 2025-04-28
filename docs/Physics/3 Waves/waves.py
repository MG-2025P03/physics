import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact

# Constants
A = 1.0  # Amplitude
wavelength = 1.0  # Wavelength
k = 2 * np.pi / wavelength  # Wave number
omega = 2 * np.pi  # Angular frequency

# Grid for the simulation
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)

def generate_sources(num_sources, radius=3):
    """Generate sources positioned in a circle around the origin."""
    if num_sources == 100:
        return []
    angles = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
    return [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

def wave_interference(X, Y, sources):
    """Calculate the wave interference pattern."""
    result = np.zeros_like(X)
    for (x0, y0) in sources:
        R = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-9  # Avoid division by zero
        result += A * np.cos(k * R - omega * 0)  # Static view with t = 0
    return result

def plot_wave_pattern(num_sources):
    """Plot the interference pattern based on the number of sources."""
    sources = generate_sources(num_sources)
    Z = wave_interference(X, Y, sources)
    plt.figure(figsize=(8, 8))
    plt.contourf(X, Y, Z, levels=100, cmap='jet')
    plt.title(f"Interference Pattern with {num_sources} Sources")
    plt.xlabel("x (units)")
    plt.ylabel("y (units)")
    plt.colorbar(label='Wave Intensity')
    if sources:  # Only plot sources if there are any.
        plt.scatter(*zip(*sources), color='white', label='Wave Sources')
        plt.legend(loc='upper right')
    plt.show()

# Interactive slider for the number of sources
interact(
    plot_wave_pattern,
    num_sources=widgets.IntSlider(min=0, max=300, step=1, value=4)
)