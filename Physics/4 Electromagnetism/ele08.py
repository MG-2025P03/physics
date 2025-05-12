import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v0 = 1e6  # Initial velocity magnitude of the particle (m/s)
t_max = 1e-7  # Maximum simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Calculate the radius and angular frequency
r = m * v0 / (q * B)
omega = q * B / m

# Parametric equations for circular motion
x = r * np.cos(omega * time)
y = r * np.sin(omega * time)
z = np.zeros_like(time)  # No motion in the z-direction

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the circular motion
ax.plot(x, y, z, label='Particle trajectory', color='b')
ax.scatter([0], [0], [0], color='r', label='Center of motion', zorder=5)

# Plot some magnetic field lines
bz = np.linspace(-1, 1, num_points)
bx = np.zeros_like(bz) + r  # Offset field lines
by = np.zeros_like(bz)
for bx_offset in np.linspace(-r, r, 5):
    ax.plot(bx + bx_offset, by, bz, color='g', alpha=0.3)

# Set labels and title
ax.set_title('Circular Motion in a Uniform Magnetic Field')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis (Field Direction)')
ax.view_init(elev=25, azim=45)  # Adjust viewing angle
ax.legend()

plt.show()