import numpy as np
import matplotlib.pyplot as plt

# Set parameters
L = 1.0  # Length of the needle
D = 1.0  # Distance between the parallel lines
n = 10  # Number of needle drops

# Initialize count of crossings
crossings = 0

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 4)  # X-axis limits
ax.set_ylim(0, 4)  # Y-axis limits
ax.set_xticks(np.arange(0, 5, 1))
ax.set_yticks(np.arange(0, 5, 1))
ax.set_aspect('equal', adjustable='box')

# Draw parallel lines
for i in np.arange(0, 4, D):
    ax.axhline(y=i, color='black', linewidth=1)

# Simulate needle drops
for _ in range(n):
    # Randomly choose midpoint and angle
    midpoint_x = np.random.uniform(0, 4)
    midpoint_y = np.random.uniform(0, 4)
    angle = np.random.uniform(0, np.pi)

    # Calculate the endpoints of the needle
    dx = (L / 2) * np.cos(angle)
    dy = (L / 2) * np.sin(angle)
    x_start = midpoint_x - dx
    x_end = midpoint_x + dx
    y_start = midpoint_y - dy
    y_end = midpoint_y + dy
    
    # Check if the needle crosses a line
    if (y_start // D) != (y_end // D):
        crossings += 1
        color = 'red'  # Crossing needle in red
    else:
        color = 'blue'  # Non-crossing needle in blue

    # Draw the needle
    ax.plot([x_start, x_end], [y_start, y_end], color=color, linewidth=2)

# Estimate pi
pi_estimate = (2 * L * n) / (crossings * D)
print(f"Estimated value of pi: {pi_estimate:.4f}")

# Add title and labels
ax.set_title(f"Buffon's Needle Simulation\nEstimated value of π: {pi_estimate:.4f}")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Show the plot
plt.show()