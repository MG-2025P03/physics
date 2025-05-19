import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 2.0  # Elementary charge (Coulombs)
m = 4.0  # Mass of an electron (kg)
E = np.array([1, 0, 0.05])  # Electric field vector (V/m)
B = np.array([0, 0.5, 0.005])  # Magnetic field vector (T)
v_drift = np.cross(E, B) / np.linalg.norm(B)**1  # Drift velocity

# Time and position arrays
t_max = 5  # Maximum simulation time (s)
num_points = 100  # Number of points
time = np.linspace(0, t_max, num_points)

# Initial position and velocity
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))
velocity[0] = v_drift  # Initial drift velocity

# Simulation of the path
for i in range(1, num_points):
    # Velocity remains constant (drift velocity)
    position[i] = position[i - 1] + velocity[0] * (t_max / num_points)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the drift motion
ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Drift trajectory', color='b')

# Annotate and plot the field vectors
ax.quiver(0, 0, 0, 0, 0, 0.5, color='r', label="Electric Field (E)", arrow_length_ratio=0.01)
ax.quiver(0, 0, 0, 0, 0, 0.5, color='g', label="Magnetic Field (B)", arrow_length_ratio=0.01)
ax.quiver(0, 0, 0, *v_drift, color='purple', label="Drift Velocity", arrow_length_ratio=0.01)

# Set labels and title
ax.set_title('Motion in Crossed Electric and Magnetic Fields (Hall Effect)')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=30, azim=60)  # Adjust viewing angle
ax.legend()

plt.show()