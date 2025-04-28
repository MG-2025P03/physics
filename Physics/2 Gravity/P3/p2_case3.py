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
    if num_sources == 0:
        return []
    angles = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
    return [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

def wave_interference(X, Y, sources):
    """Calculate the wave interference pattern."""
    result = np.zeros_like(X)
    for (x0, y0) in sources:
        R = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-9  # Avoid division by zero
        result += A * np.cos(k * R)  # Static view with t = 0
    return result

def plot_wave_pattern(num_sources):
    """Plot the interference pattern based on the number of sources."""
    plt.close('all')  # Close any existing figures

    sources = generate_sources(num_sources)
    Z = wave_interference(X, Y, sources)
    fig, ax = plt.subplots(figsize=(8, 8))
    contour = ax.contourf(X, Y, Z, levels=100, cmap='jet')
    ax.set_title(f"Interference Pattern with {num_sources} Sources")
    ax.set_xlabel("x (units)")
    ax.set_ylabel("y (units)")
    fig.colorbar(contour, ax=ax, label='Wave Intensity')

    if sources:
        ax.scatter(*zip(*sources), color='white', label='Wave Sources')
        ax.legend(loc='upper right')

    plt.tight_layout()  # Adjust subplot parameters for a tight layout
    plt.show()


# Slider for the number of sources
num_sources_slider = widgets.IntSlider(
    min=0,
    max=300,
    step=1,
    value=1,
    description='Sources: ',
    continuous_update=True
)

# Interactive plot
interact(plot_wave_pattern, num_sources=num_sources_slider)