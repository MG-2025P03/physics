import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v_perpendicular = 1e6  # Initial velocity perpendicular to B (m/s)
v_parallel = 0.5e6  # Initial velocity parallel to B (m/s)
t_max = 1e-7  # Maximum time for the simulation (s)
num_points = 1000  # Number of simulation points

# Time discretization
time = np.linspace(0, t_max, num_points)

# Initialize position and velocity arrays
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))

# Initial conditions
velocity[0] = [v_perpendicular, 0, v_parallel]  # Initial velocity

# Cyclotron frequency and radius
omega = q * B / m
r = m * v_perpendicular / (q * B)

# Compute positions and velocities
for i in range(1, num_points):
    v = velocity[i - 1]
    F_magnetic = q * np.cross(v, [0, 0, B])  # Magnetic force
    a = F_magnetic / m                       # Acceleration

    # Update velocity and position
    velocity[i] = velocity[i - 1] + a * (t_max / num_points)
    position[i] = position[i - 1] + velocity[i] * (t_max / num_points)

# Plotting the results
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Particle trajectory')
ax.set_title('Helical Motion of a Charged Particle in a Magnetic Field')
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('z-position (m)')

plt.legend()
plt.show()