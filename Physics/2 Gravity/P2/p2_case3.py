import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
mass_earth = 5.972 * 10**24  # Mass of Earth (kg)
radius_earth = 6.371 * 10**6  # Radius of Earth (m)

# Number of points for the trajectory
num_points = 500
theta = np.linspace(0, 2 * np.pi, num_points)  # Angles for the circular trajectory

# Define starting positions for the three bodies (in km above Earth's surface)
starting_positions = [
    (radius_earth + 500e3, 0),  # 500 km above Earth's surface
    (radius_earth + 1000e3, 0),  # 1000 km above Earth's surface
    (radius_earth + 1500e3, 0)   # 1500 km above Earth's surface
]

# Initialize the plot
plt.figure(figsize=(10, 10))

# Plot Earth at the origin
plt.plot(0, 0, 'bo', markersize=12, label="Earth")

# Calculate and plot the trajectories of the three bodies
for i, (r, ang) in enumerate(starting_positions):
    # Calculate the circular trajectory for the body
    x = r * np.cos(theta)  # Circular path around Earth
    y = r * np.sin(theta)

    # Plot the trajectory with a label for each body
    plt.plot(x, y, label=f"Body {i+1} Starting Position: {r / 1e3:.1f} km", linewidth=2)

# Annotations and Labels
plt.title("Circular Trajectories of Bodies Escaping Earth's Gravity")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.xlim([-2e7, 2e7])  # Set limits for x-axis
plt.ylim([-2e7, 2e7])  # Set limits for y-axis
plt.gca().set_aspect('equal', adjustable='box')  # Keep equal aspect ratio for accurate circular representation
plt.legend()
plt.grid()
plt.show()