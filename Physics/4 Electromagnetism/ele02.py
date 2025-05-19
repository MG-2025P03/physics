import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 16  # Charge of the particle (Coulombs)
m = 9  # Mass of the particle (kg)
B = 10.0  # Magnetic field strength (Tesla)
E = 1000  # Electric field strength (V/m)
v0 = 20  # Initial velocity of the particle (m/s)
t_max = 10  # Maximum time for the simulation (s)
num_points = 1000  # Number of points in the simulation

# Time discretization
time = np.linspace(0, t_max, num_points)

# Initialize position and velocity arrays
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))

# Initial conditions
velocity[0] = [v0, 0, 0]  # Initial velocity in x-direction

# Time increment
dt = t_max / num_points

# Main loop to calculate position and velocity
for i in range(1, num_points):
    v = velocity[i-1]
    F_electric = q * np.array([E, 0, 0])          # Electric force
    F_magnetic = q * np.cross(v, [0, 0, B])       # Magnetic force
    F_total = F_electric + F_magnetic
    a = F_total / m                               # Acceleration

    # Update velocity and position
    velocity[i] = velocity[i-1] + a * dt
    position[i] = position[i-1] + velocity[i] * dt

# Plotting the results
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Particle trajectory')
ax.set_title('Helical Motion of a Charged Particle in Crossed E and B Fields')
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('z-position (m)')

plt.legend()
plt.show()