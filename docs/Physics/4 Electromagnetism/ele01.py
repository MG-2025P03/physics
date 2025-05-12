import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v0 = 1e6  # Initial velocity of the particle (m/s)
time = np.linspace(0, 1e-7, 1000)  # Time array

# Calculate the radius and angular frequency
r = m * v0 / (q * B)
omega = q * B / m

# Parametric equations for circular motion
x = r * np.cos(omega * time)
y = r * np.sin(omega * time)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Particle trajectory')
plt.scatter([0], [0], color='r', label='Center of motion', zorder=5)
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
plt.axvline(0, color='k', linestyle='--', linewidth=0.8)
plt.title('Circular Motion of a Charged Particle in a Magnetic Field')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()