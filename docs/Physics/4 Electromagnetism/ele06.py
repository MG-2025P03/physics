import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
E = 1e5  # Electric field strength (V/m)
B = 1.0  # Magnetic field strength (T)
d = 0.1  # Distance over which the electric field accelerates the ions (m)
v0 = np.sqrt(2 * E * 1.6e-19 / 1.67e-27)  # Initial velocity for reference ion with m/q = 1

# Mass-to-charge ratios for three different ions
m_q_ratios = [1, 2, 0.5]  # m/q relative values
colors = ['r', 'g', 'b']
labels = ['m/q = 1', 'm/q = 2', 'm/q = 0.5']

# Time array
time = np.linspace(0, 1e-5, 1000)

# Create the figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for m_q, color, label in zip(m_q_ratios, colors, labels):
    # Calculate the velocity and radius for each m/q ratio
    v = v0 / np.sqrt(m_q)
    radius = v / (B * 1.6e-19 / (m_q * 1.67e-27))
    
    # Calculate trajectory
    x = time * v  # Simulating linear progression along an axis
    y = radius * np.cos(v * B * time / (m_q * 1.67e-27)) - radius
    z = radius * np.sin(v * B * time / (m_q * 1.67e-27))

    ax.plot(x, y, z, color=color, label=label)

# Set labels and title
ax.set_title('3D Mass Spectrometer: Ion Trajectories by Mass-to-Charge Ratio')
ax.set_xlabel('Axial progression (m)')
ax.set_ylabel('Deflection in y (m)')
ax.set_zlabel('Deflection in z (m)')
ax.legend()

plt.show()