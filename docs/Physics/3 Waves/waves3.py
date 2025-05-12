import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import imageio  # For GIF creation
import io  # To work with imageio
from PIL import Image  # For converting matplotlib canvas to image

# Parameters
L = 1.0     # Side length of the square
c = 1.0     # Wave speed
f = 1.0     # Frequency of the wave
A = 1.0     # Amplitude of the wave
lambda_ = 1.0 # Wavelength
k = 2 * np.pi / lambda_  # Wave number
t = 0.0     # Time

# Function to calculate the wave displacement from a source
def wave_displacement(x, y, x0, y0, k, t):
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    return A * np.sin(2 * np.pi * f * t - k * r)

# Function to calculate the interference pattern
def calculate_interference_data(num_sources):
    # Preparing the grid
    x = np.linspace(-L, L, 200)
    y = np.linspace(-L, L, 200)
    X, Y = np.meshgrid(x, y)

    # Create a regular polygon (circle-like distribution) for more sources
    angles = np.linspace(0, 2 * np.pi, num_sources, endpoint=False)
    positions = [(L * np.cos(angle), L * np.sin(angle)) for angle in angles]

    # Calculate superposition
    Z = np.zeros(X.shape)
    for (x0, y0) in positions:
        Z += wave_displacement(X, Y, x0, y0, k, t)

    return X, Y, Z, positions

# Function to plot the interference pattern (without slider)
def plot_interference(num_sources, ax):
    ax.clear()  # Clear the previous plot

    X, Y, Z, positions = calculate_interference_data(num_sources)

    # Find min and max values for consistent color scale
    vmin = np.min(Z)
    vmax = np.max(Z)

    # Plot
    contour = ax.contourf(X, Y, Z, 20, cmap='RdBu_r', vmin=vmin, vmax=vmax)  # Set vmin and vmax here

    # Add the sources to the plot
    for x0, y0 in positions:
        ax.plot(x0, y0, 'o', markersize=3, color='black')

    ax.set_title(f"Interference Pattern with {num_sources} Sources")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")


def create_gif(filename="interference.gif", duration=3, fps=15): #Defaults to 2 seconds
    num_sources_list = np.linspace(0, 50, int(duration * fps), endpoint=True, dtype=int) #Number of frames for smoother animation
    images = []

    fig, ax = plt.subplots()
    try:
        for num_sources in num_sources_list:
            plot_interference(num_sources, ax)
            fig.canvas.draw()

            # Convert the matplotlib figure to a PIL Image
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            image = Image.open(buf)
            images.append(np.array(image))
            buf.close()

        imageio.mimsave(filename, images, fps=fps)
        print(f"GIF saved as {filename}")
    except Exception as e:
        print(f"Error creating GIF: {e}")
    finally:
        plt.close(fig)  # Close the figure to release memory

# Main execution
create_gif(duration=30)  # Create a GIF that cycles through source numbers