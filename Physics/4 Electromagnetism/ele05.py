import numpy as np
import matplotlib.pyplot as plt

# Constants
E = 0.3  # Electric field strength (V/m)
B = 0.4  # Magnetic field strength (T)
d = 0.8  # Distance over which the electric field accelerates the ions (m)
v0 = np.sqrt(2 * E * 16.7 / 10)  # Initial velocity for reference ion with m/q = 1

# Mass-to-charge ratios for three different ions
m_q_ratios = [0.5, 1, 0.25]  # m/q relative to the reference ion
colors = ['r', 'g', 'b']
labels = ['m/q = 0.5', 'm/q = 1', 'm/q = 0.25']

# Time array
time = np.linspace(0, 3, 6)

# Create the plot
plt.figure(figsize=(12, 6))

for m_q, color, label in zip(m_q_ratios, colors, labels):
    # Calculate the velocity based on m/q ratio
    v = v0 / np.sqrt(m_q)
    
    # Radius of the trajectory
    radius = v / (B * 1.67 / (m_q * 16.7))
    
    # Calculate trajectory
    x = radius * np.sin(v * B * time / (m_q * 1.67))
    y = radius * np.cos(v * B * time / (m_q * 1.67)) - radius

    plt.plot(x, y, color=color, label=label)

plt.title('Mass Spectrometer: Ion Trajectories Based on Mass-to-Charge RatioXX')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.show()