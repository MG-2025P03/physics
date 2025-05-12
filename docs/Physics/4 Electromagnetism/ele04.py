import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v0 = 1e6  # Initial velocity of the particle (m/s)
t_max = 1e-7  # Simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Calculate the radius and angular frequency
r = m * v0 / (q * B)
omega = q * B / m

# Parametric equations for circular motion in 3D
x = r * np.cos(omega * time)
y = r * np.sin(omega * time)
z = time  # Representing time along the z-axis

# Create the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label='Particle trajectory')
ax.set_title('Circular Motion of a Charged Particle in a Magnetic Field (3D)')
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('Time (s)')
ax.scatter([0], [0], [0], color='r', label='Center of motion', zorder=5)  # Center point

plt.legend()
plt.show()