# Analysis of Wave Interference Patterns Formed by Point Sources at the Vertices of a Square

## Wave Equations

Assuming a simple harmonic wave emitted from each source with the same frequency and amplitude, the wave equation from a point source located at position $x_0, y_0$ can be described by:

$$
\psi(x, y, t) = A \cos(kr - \omega t + \phi)
$$

where:

$\psi$ is the wave displacement

$A$ is the amplitude

$k$ is the wave number, given by $k = \frac{2\pi}{\lambda}$

$\omega$ is the angular frequency, given by $\omega = 2\pi f$

$r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$ is the distance from the source to the point $x, y$

$\phi$ is the phase constant

$\lambda$ is the wavelength

$f$ is the frequency

### Superposition of Waves

The principle of superposition states that the resultant wave displacement at any point on the water surface is the sum of the displacements due to each individual wave. Therefore, the total wave displacement $\Psi(x, y, t)$ is given by (initial 4 vertices):

$$
\Psi(x, y, t) = \psi_A(x, y, t) + \psi_B(x, y, t) + \psi_C(x, y, t) + \psi_D(x, y, t)
$$

This equation represents the interference pattern on the water surface.

### Interference Patterns

Constructive Interference: Occurs at points where the path difference between waves from two or more sources is an integer multiple of the wavelength $m\lambda$, where $m$ is an integer. At these points, the waves reinforce each other, resulting in larger amplitudes.

Destructive Interference: Occurs at points where the path difference is an odd multiple of half wavelengths $(m + \frac{1}{2})\lambda$. Here, the waves cancel each other, resulting in nodes or points of no displacement.

### Combined Displacement Function

The resultant wave displacement at a point ((x, y)) at time (t) is given by:

$$
\Psi(x, y, t) = \psi_A(x, y, t) + \psi_B(x, y, t) + \psi_C(x, y, t) + \psi_D(x, y, t)
$$

where each $\psi$ is the wave equation from an individual source.

### Simulation on Waves

```
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
    angles = np.linspace(0, 3 * np.pi, num_sources, endpoint=False)
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
        angles = np.linspace(0, xL * np.pi, num_sources, endpoint=False)
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
```

#### Waves Simulation

[![One Source](../../_pics/Waves01.png] 'sample text')] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

![Four Sources](https://mg-2025p03.github.io/physics/_pics/Waves04.png])

[![ Six Sources](../physics/_pics/Waves06.png])]( (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Eight Sources](../physics/_pics/Waves08.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Ten Sources](../physics/_pics/Waves10.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Thirteen Sources](../physics/_pics/Waves13.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Twenty Seven Sources](../physics/_pics/Waves27.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Forty Sources](../physics/_pics/Waves40.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)

[![ Fifty Sources](../physics/_pics/Waves50.png])] (https://mg-2025p03.github.io/physics/3 Waves/waves.html)