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


def create_gif(filename="interference.gif", duration=2, fps=10): #Defaults to 2 seconds
    num_sources_list = np.linspace(0, 75, int(duration * fps), endpoint=True, dtype=int) #Number of frames for smoother animation
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

# Text fragment analysis
text_fragment = """1.00
36
36
18
5.4
4.5
0.75 -
0.50
0.25 -
9
6.4
6
5.44.8
3.6
13.63.4
3.2
3
1.81.6
2
0.00.0 0
3.6
12
3.6
9.0
3.0
2.7
A
- 6
1.8
4.5
8
- 9
1.5
0.0 - O
1.8
0
- 0
0
0
0.0
0.0
0.00
-0.25
-0.50
-0.75 -
-1.6
-1-3 -3.2
2252:2-4.6 3.2
-4.5 |12 F -12
4.8.6 1-6
-4.8
-5.4
- - 6.4
1.2
-16
-8
-9
-6
- - 12
- - 18
-1.8
-1.5
-3.0
-3.6
-4.5
-5.4
0.9
0.0
-0.9
-1.8
-1.00
-6.0
-D1
urces
17"""

def extract_numbers(text):
    numbers = []
    for line in text.splitlines():
        for word in line.split():
            try:
                number = float(word)
                numbers.append(number)
            except ValueError:
                pass
    return numbers

numbers = extract_numbers(text_fragment)

# Question: How many distinct values are greater than 5 but less than 15 in the text fragment?
distinct_values = set()
for number in numbers:
    if 5 < number < 15:
        distinct_values.add(number)

num_distinct_values = len(distinct_values)
answer = f"There are {num_distinct_values} distinct values greater than 5 and less than 15."
print(answer)

# Main execution
create_gif(duration=30)  # Create a GIF that cycles through source numbers