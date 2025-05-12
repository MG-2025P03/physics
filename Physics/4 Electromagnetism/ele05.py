import numpy as np
import matplotlib.pyplot as plt

# Constants
E = 1e5  # Electric field strength (V/m)
B = 1.0  # Magnetic field strength (T)
d = 0.1  # Distance over which the electric field accelerates the ions (m)
v0 = np.sqrt(2 * E * 1.6e-19 / 1.67e-27)  # Initial velocity for reference ion with m/q = 1

# Mass-to-charge ratios for three different ions
m_q_ratios = [1, 2, 0.5]  # m/q relative to the reference ion
colors = ['r', 'g', 'b']
labels = ['m/q = 1', 'm/q = 2', 'm/q = 0.5']

# Time array
time = np.linspace(0, 1e-5, 1000)

# Create the plot
plt.figure(figsize=(12, 6))

for m_q, color, label in zip(m_q_ratios, colors, labels):
    # Calculate the velocity based on m/q ratio
    v = v0 / np.sqrt(m_q)
    
    # Radius of the trajectory
    radius = v / (B * 1.6e-19 / (m_q * 1.67e-27))
    
    # Calculate trajectory
    x = radius * np.sin(v * B * time / (m_q * 1.67e-27))
    y = radius * np.cos(v * B * time / (m_q * 1.67e-27)) - radius

    plt.plot(x, y, color=color, label=label)

plt.title('Mass Spectrometer: Ion Trajectories Based on Mass-to-Charge Ratio')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.show()