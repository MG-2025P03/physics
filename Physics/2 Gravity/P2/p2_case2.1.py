import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
mass_earth = 5.972 * 10**24  # Mass of Earth (kg)
radius_earth = 6.371 * 10**6  # Radius of Earth (m)

# Calculate escape velocity
escape_velocity = np.sqrt(2 * G * mass_earth / radius_earth)

# Generate data for the trajectory path (ellipse)
num_points = 1000
theta = np.linspace(0, 2 * np.pi, num_points)
r_trajectory = radius_earth * 1.5  # Trajectory radius (1.5 times Earth's radius)
x = r_trajectory * np.cos(theta)
y = r_trajectory * np.sin(theta)

# Set up the plot
plt.figure(figsize=(10, 8))
plt.plot(x, y, label="Escape Trajectory", color="orange")
plt.plot(0, 0, 'bo', markersize=12, label="Earth")  # Earth at the origin
plt.axhline(y=escape_velocity, color='r', linestyle='--', label=f'Escape Velocity: {escape_velocity:.2f} m/s')

# Annotations and Labels
plt.title("Second Cosmic Velocity Illustration")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.xlim(-2.5 * radius_earth, 2.5 * radius_earth)
plt.ylim(-2.5 * radius_earth, 2.5 * radius_earth)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid()
plt.show()