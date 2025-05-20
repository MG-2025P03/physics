import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M_sun = 1.989e30  # Mass of the Sun (kg)

# Masses of the remaining planets (in kg)
M_mercury = 3.3011e23  # Mercury
M_venus = 4.8675e24    # Venus
M_earth = 5.972e24     # Earth
M_mars = 6.4171e23     # Mars

# Average distances from the Sun (in meters)
distances = {
    'Mercury': 5.791e10,
    'Venus': 1.082e11,
    'Earth': 1.496e11,
    'Mars': 2.279e11,  # Mars distance
}

# Dictionary to hold remaining planets and their properties
planets = {
    'Mercury': (M_mercury, distances['Mercury']),
    'Venus': (M_venus, distances['Venus']),
    'Earth': (M_earth, distances['Earth']),
    'Mars': (M_mars, distances['Mars']),
}

# Orbital periods (in days)
orbital_periods = {
    'Mercury': 88,
    'Venus': 225,
    'Earth': 365,
    'Mars': 687,
}

# Calculate positions of the planets based on the current date (May 20, 2025)
def calculate_planet_positions():
    # Reference date: Jan 1, 2000
    ref_date = np.datetime64('2000-01-01')
    current_date = np.datetime64('2025-05-20')
    days_since_ref = (current_date - ref_date).astype('timedelta64[D]').astype(int)

    positions = {}
    for planet, distance in distances.items():
        angle = (days_since_ref / orbital_periods[planet]) * 2 * np.pi  # Angle in radians
        x = distance * np.cos(angle)  # x position
        y = distance * np.sin(angle)  # y position
        positions[planet] = (x, y)
    
    return positions

# Function defining the system of Differential Equations
def gravity_equations(state, t):
    x, y, vx, vy = state
    ax_total = 0
    ay_total = 0
    
    # Gravitational influence of the Sun
    r_sun = np.sqrt(x**2 + y**2)
    ax_total += -G * M_sun * x / r_sun**3
    ay_total += -G * M_sun * y / r_sun**3
    
    # Gravitational influences of remaining planets
    for mass, distance in planets.values():
        r_planet = np.sqrt((x - distance)**2 + y**2)
        ax_total += -G * mass * (x - distance) / r_planet**3
        ay_total += -G * mass * y / r_planet**3

    return [vx, vy, ax_total, ay_total]

# Function to plot parabolic orbits for planets
def plot_parabolic_orbit(planet_distance, color, num_points=100):
    # Generate a parabolic path for visibility
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = planet_distance * np.cos(theta)
    y = (planet_distance / 1.5) * np.sin(theta)  # Adjusted to visualize in a parabolic style
    plt.plot(x, y, color=color, linestyle='dashed', linewidth=1)

# Function to plot trajectory of Halley's Comet and location of Solar System bodies
def plot_trajectory(initial_conditions, t_max, num_points):
    # Simulate time / trajectories
    t = np.linspace(0, t_max, num_points)
    
    # Solve ODE for Halley's Comet trajectory
    sol = odeint(gravity_equations, initial_conditions, t)
    
    # Extract position data
    x = sol[:, 0]
    y = sol[:, 1]

    # Initialize the plot to focus on the planets
    plt.figure(figsize=(12, 10))

    # Plot Sun as a filled circle
    plt.scatter(0, 0, color='yellow', s=1000, label='Sun')

    # Calculate and plot planet positions and their paths
    planet_positions = calculate_planet_positions()
    for planet, (x_pos, y_pos) in planet_positions.items():
        plot_parabolic_orbit(distances[planet], 'lightgray')  # Parabolic path for each planet
        plt.scatter(x_pos, y_pos, s=300, label=planet)  # Enlarged representation for each planet

    # Plot Halley's Comet trajectory
    plt.plot(x, y, color='orange', linewidth=2, label='Halley\'s Comet Trajectory')

    # Customizing the plot
    plt.title('Halley\'s Comet Orbit with Parabolic Planets')
    plt.xlabel('Distance (m)')
    plt.ylabel('Distance (m)')

    # Adjust limits to zoom in by 40% centered on the solar system
    plt.xlim(-1.8e11, 1.8e11)  # New limits to zoom by 40%
    plt.ylim(-1.8e11, 1.8e11)

    plt.legend()
    plt.grid()
    plt.axis('equal')  # Set equal scaling to maintain aspect ratio
    plt.show()

# Original computations for Halley's Comet
initial_distance = 0.96 * 1.496e11  # Original distance set to 0.96 AU
velocity_magnitude = -40000  # Example velocity to simulate parabolic path

# Set the direction of the velocity to 106 degrees
angle = 5  # Adjust angle to 106 degrees
angle_rad = np.radians(angle)  # Convert to radians
vx = velocity_magnitude * np.cos(angle_rad)  # x-component of velocity
vy = velocity_magnitude * np.sin(angle_rad)  # y-component of velocity

# Initial conditions for Halley's Comet
initial_conditions = [initial_distance, 0, vx, vy]  # Start with new position and velocity components

# Original t_max was 15 * 365 * 24 * 60 * 60, reduce it by 30%
t_max = 15 * 365 * 24 * 60    # Approximately 10.5 years in seconds
plot_trajectory(initial_conditions, t_max, 10000)  