# projectile_motion.py

import numpy as np
import matplotlib.pyplot as plt

def calculate_range(v0, angle):
    """Calculate the range of the projectile."""
    g = 9.81  # acceleration due to gravity (m/s^2)
    return (v0**2 * np.sin(2 * np.radians(angle))) / g

def plot_projectile_motion(v0):
    """Plot the range of a projectile vs. angle of projection."""
    angles = np.linspace(0, 90, 100)
    ranges = calculate_range(v0, angles)

    plt.figure(figsize=(10, 6))
    plt.plot(angles, ranges, color='blue')
    plt.title('Range of a Projectile vs. Angle of Projection')
    plt.xlabel('Angle of Projection (degrees)')
    plt.ylabel('Range (m)')
    plt.grid()
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(0, 90)
    plt.ylim(0, max(ranges) + 10)
    plt.show()

if __name__ == "__main__":
    initial_velocity = 50  # You can change this value for different initial velocities
    plot_projectile_motion(initial_velocity)
