import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for toroidal field
radius_major = 1.0  # Major radius of the torus (distance from center of tube to center of torus)
radius_minor = 0.2  # Minor radius of the torus (radius of the tube)

# Create data for a torus
theta = np.linspace(0, 2 * np.pi, 100)  # Angle around the torus
phi = np.linspace(0, 2 * np.pi, 100)  # Angle along the torus' tube
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for the torus
x = (radius_major + radius_minor * np.cos(phi)) * np.cos(theta)
y = (radius_major + radius_minor * np.cos(phi)) * np.sin(theta)
z = radius_minor * np.sin(phi)

# Create the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the torus surface
ax.plot_surface(x, y, z, color='c', alpha=0.5, rstride=5, cstride=5, edgecolor='none')

# Plot magnetic field lines
num_lines = 8
for i in range(num_lines):
    angle_offset = (i / num_lines) * 2 * np.pi
    x_line = (radius_major + radius_minor * np.cos(phi)) * np.cos(theta + angle_offset)
    y_line = (radius_major + radius_minor * np.cos(phi)) * np.sin(theta + angle_offset)
    z_line = radius_minor * np.sin(phi)
    ax.plot(x_line[0, :], y_line[0, :], z_line[0, :], color='r')

# Set labels and title
ax.set_title('3D Representation of Plasma Confinement in a Toroidal Field')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=30, azim=60)  # Better viewing angle

plt.show()