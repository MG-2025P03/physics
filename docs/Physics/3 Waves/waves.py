import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Parameters
L = 4.0     # Side length of the square
c = 0.5     # Wave speed
f = 0.5     # Frequency of the wave
A = 0.5     # Amplitude of the wave
lambda_ = 0.5 # Wavelength
k = 2 * np.pi / lambda_  # Wave number
t = 0.3     # Time

# Function to calculate the wave displacement from a source
def wave_displacement(x, y, x0, y0, k, t):
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    return (A * np.sin(2 * np.pi * f * t - k * r)) 

# Function to calculate and plot the interference pattern
def plot_interference(num_sources):
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.85, top=0.85, wspace=0.2, hspace=0.2)
    ax.set_title('Interference Pattern of Waves')

    # Preparing the grid
    x = np.linspace(-L, L, 1200)
    y = np.linspace(-L, L, 1200)
    X, Y = np.meshgrid(x, y)

    # Create a regular polygon (circle-like distribution) for more sources
    angles = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
    positions = [(L * np.cos(angle), L * np.sin(angle)) for angle in angles]

    # Calculate superposition
    Z = np.zeros(X.shape)
    for (x0, y0) in positions:
        Z += wave_displacement(X, Y, x0, y0, k, t)

    # Find min and max values for consistent color scale
    vmin = np.min(Z)
    vmax = np.max(Z)

    # Plot
    contour = ax.contourf(X, Y, Z, 20, cmap='RdBu_r', vmin=vmin, vmax=vmax)  # Set vmin and vmax here
    cbar = plt.colorbar(contour)

    # Add the sources to the plot
    for x0, y0 in positions:
        ax.plot(x0, y0, 'X', markersize=6, color='yellow')

    axcolor = 'lightgoldenrodyellow'
    axSources1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    #axSources2 = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)

    sliderSources1 = Slider(axSources1, 'Num Sources', 1, 75, valinit=num_sources, valstep=1)
    #sliderSources2 = Slider(axSources2, 'Graph size', 1, 4, valinit=L, valstep=0.25)

    def update(val):
        num_sources = int(sliderSources1.val)
        # xL = float(sliderSources2.val)
        xL = L
        angles = np.linspace(0,2 * np.pi, num_sources, endpoint=False)
        positions = [(xL * np.cos(angle), xL * np.sin(angle)) for angle in angles]

        Z = np.zeros(X.shape)
        for (x0, y0) in positions:
            Z += wave_displacement(X, Y, x0 , y0, k, t)

        # Plot with fixed color limits
        ax.clear()

        contour = ax.contourf(X, Y, Z, 20, cmap='RdBu_r', vmin=vmin, vmax=vmax)  # Set vmin and vmax here
        cbar = plt.colorbar(contour, ax=ax)

         # Add the sources to the plot
        for x0, y0 in positions:
            ax.plot(x0, y0, 'x', markersize=6, color='yellow')

        cbar.remove()
        plt.draw()

    sliderSources1.on_changed(update)
    # sliderSources2.on_changed(update)
    plt.show()

# Initial call to plot the interference pattern
plot_interference(4)