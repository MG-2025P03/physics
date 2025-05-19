import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 2.0  # Charge of the particle (Coulombs)
m = 3.0  # Mass of the particle (kg)
E = 10  # Electric field magnitude (V/m)
B = 1.0  # Magnetic field strength (T)
v0 = 0  # Initial velocity (m/s), assume starting from rest for simplicity
t_max = 10  # Maximum simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Initial velocity and acceleration
v_initial = np.array([v0, 0, 0])  # Start with some initial velocity
a_electric = np.array([q * E / m, 0, 0])  # Acceleration due to electric field

# Magnetic field direction
B_field = np.array([0, 0, B])

# Initialize arrays for position and velocity
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))
velocity[0] = v_initial

# Numerical integration
dt = t_max / num_points
for i in range(1, num_points):
    v = velocity[i-1]
    F_magnetic = q * np.cross(v, B_field)  # Lorentz force component due to magnetic field
    a_magnetic = F_magnetic / m
    a_total = a_electric + a_magnetic  # Total acceleration
    
    # Update velocity and position
    velocity[i] = velocity[i-1] + a_total * dt
    position[i] = position[i-1] + velocity[i] * dt

# Plotting the trajectory
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Particle trajectory', color='b')

# Set labels and title
ax.set_title('Motion in Combined Uniform Electric and Magnetic Fields')
ax.set_xlabel('X Axis (Electric Field Direction)')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis (Magnetic Field Direction)')
ax.view_init(elev=25, azim=60)  # Adjust viewing angle
ax.legend()

plt.show()