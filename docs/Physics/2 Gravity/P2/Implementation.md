# Simulations

## Orbital velocity

### First Cosmic Velocity - Trajectory of a small satellite body in parabolic orbit

<details>
<summary> <- Click to view the codes</summary>

```
import io
import numpy as np
import matplotlib.pyplot as plt
import base64

# Constant Parameters
G = 6.674e-11  # Gravitational constant (m^3/kg/s^2)
M = 5.972e24   # The mass of a larger body, e.g. the Earth (kg)
m = 200       # The mass of a smaller body, e.g. a satellite (kg)

# Initial conditions
r0 = 7e6  # Initial distance from the center of mass of the larger body(m)
v0 = 4300  #  Initial orbital velocity (m/s)
theta0 = 0  # Initial angle in radians

# Time parameters
T = 6000  # Simulation time (s)
N = 100_000  # Number of time steps
dt = T / N

# Tables for position and speed
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

# Warunki początkowe
x[0] = r0 * np.cos(theta0)
y[0] = r0 * np.sin(theta0)
vx[0] = -v0 * np.sin(theta0)
vy[0] = v0 * np.cos(theta0)

# Numerical integration (Euler's method)
for i in range(1, N):
    r = np.sqrt(x[i - 1]**2 + y[i - 1]**2)  # Distance from center of mass
    ax = -G * M * x[i - 1] / r**3          # Acceleration in x axis
    ay = -G * M * y[i - 1] / r**3          # Acceleration in y axis
    
    # Using the previous velocity to update the current velocity
    vx[i] = vx[i - 1] + ax * dt
    vy[i] = vy[i - 1] + ay * dt
    
    # Using the previous position to update the current position
    x[i] = x[i - 1] + vx[i - 1] * dt
    y[i] = y[i - 1] + vy[i - 1] * dt

# Wizualizacja trajektorii
plt.figure(figsize=(8, 8))
plt.plot(x, y, label="Trajectory")
plt.plot(0, 0, 'ro', label="Central body (e.g. Earth)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("First cosmic velocity - Trajectory of a satellite/small body in a parabolic orbit")
plt.legend(loc='lower right')
plt.grid()
plt.axis('equal')
plt.show()

# Save the plot to a BytesIO object
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
plt.close() # Close the plot to free memory

# Embed the image in HTML
image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<title>Satellite Trajectory</title>
</head>
<body>
<h1>Satellite Trajectory Simulation</h1>
<img src="data:image/png;base64,{image_base64}" alt="Satellite Trajectory">
</body>
</html>
"""

# Save the HTML to a file
with open("satellite_trajectory.html", "w") as f:
    f.write(html_content)

print("HTML file 'satellite_trajectory.html' created successfully.")
```
</details>

[![First Cosmic Velocity](https://mg-2025p03.github.io/physics/_pics/G2P1.1.png)](https://mg-2025p03.github.io/physics/_pics/G2P1.1.png)

### Second Cosmic Velocity - Escape Trajectory

<details>
<summary> <- Click to view the codes</summary>

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.972e24   # Mass of Earth, kg
R_E = 6.371e6    # Radius of Earth, m

# Function defining the system of Differential Equations
def gravity_equations(state, t):
    x, y, vx, vy = state # Position and velocity
    r = np.sqrt(x**2 + y**2)
    
    # Check if the object hits the earth
    if r <= R_E:
        return [0, 0, 0, 0]  # Stop the simulation if it hits the Earth

    # Gravitational acceleration
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    
    return [vx, vy, ax, ay] # Return derivatives of position and velocity

# Function to plot trajectories with a filled Earth
def plot_trajectories(initial_conditions,t_max,num_points):
    
    # Simulate time / trajectories
    t = np.linspace(0, t_max, num_points)
    
    # initialize the plot
    plt.figure(figsize=(10, 10))
    plt.title('Trajectory of an Object Falling to Earth')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Plot Earth as a filled circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_earth = R_E * np.cos(theta)
    y_earth = R_E * np.sin(theta)
    plt.fill(x_earth, y_earth, color='blue', alpha=0.5, label='Earth')

    # Plot trajectories for each tuple in initial_conditions
    for i, conditions in enumerate(initial_conditions):
        # Unpack initial conditions
        # Initial state vector
        
        # Solve ODE | numerical solution of differential equations
        sol = odeint(gravity_equations, conditions, t, tcrit=1e-5)
        
        # Extract position data
        x = sol[:, 0]
        y = sol[:, 1]

        vy = sol[:, 3]

        # Stop plotting if the object hits the Earth
        mask = np.sqrt(x**2 + y**2) >= R_E
        x = x[mask]
        y = y[mask]
        
        # Plot trajectory with label
        plt.plot(x, y, label=f'Trajectory {i+1}' + f', v = {vy[0]}', linewidth=2)

        #plt.plot(x, y)

        # Central mass point
        # plt.plot(0, 0, 'yo', label='Earth Center')

    
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Trajectories of Objects Falling to Earth')
    plt.legend()
    plt.grid(True)
    plt.axis('equal') # Set equal scaling
    plt.show()

    # Example usage
initial_conditions = [
    [R_E + 1e6, 0, 0, 1000],
    [R_E + 1e6, 0, 0, 3000],
    [R_E + 1e6, 0, 0, 5000],
    [R_E + 1e6, 0, 0, 7000],
    [R_E + 1e6, 0, 0, 9000]
]

plot_trajectories(initial_conditions, 20000, 10000)  # Call the function to plot trajectories
```
</details>

[![Escape Trajectory](https://mg-2025p03.github.io/physics/_pics/GP2.2.png)](https://mg-2025p03.github.io/physics/_pics/GP2.2.png)

### Second Cosmic Velocity - 2nd Scenario | Higher velocities

[![Escape Trajectory](https://mg-2025p03.github.io/physics/_pics/GP2.3.png)](https://mg-2025p03.github.io/physics/_pics/GP2.3.png)

<details>
<summary> <- Click to view the codes</summary>

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.972e24   # Mass of Earth, kg
R_E = 6.371e6    # Radius of Earth, m

# Function defining the system of Differential Equations
def gravity_equations(state, t):
    x, y, vx, vy = state # Position and velocity
    r = np.sqrt(x**2 + y**2)
    
    # Check if the object hits the earth
    if r <= R_E:
        return [0, 0, 0, 0]  # Stop the simulation if it hits the Earth

    # Gravitational acceleration
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    
    return [vx, vy, ax, ay] # Return derivatives of position and velocity

# Function to plot trajectories with a filled Earth
def plot_trajectories(initial_conditions,t_max,num_points):
    
    # Simulate time / trajectories
    t = np.linspace(0, t_max, num_points)
    
    # initialize the plot
    plt.figure(figsize=(10, 10))
    plt.title('Trajectory of an Object Falling to Earth')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')

    # Plot Earth as a filled circle
    theta = np.linspace(0, 2*np.pi, 100)
    x_earth = R_E * np.cos(theta)
    y_earth = R_E * np.sin(theta)
    plt.fill(x_earth, y_earth, color='blue', alpha=0.5, label='Earth')

    # Plot trajectories for each tuple in initial_conditions
    for i, conditions in enumerate(initial_conditions):
        # Unpack initial conditions
        # Initial state vector
        
        # Solve ODE | numerical solution of differential equations
        sol = odeint(gravity_equations, conditions, t, tcrit=1e-5)
        
        # Extract position data
        x = sol[:, 0]
        y = sol[:, 1]

        vy = sol[:, 3]

        # Stop plotting if the object hits the Earth
        mask = np.sqrt(x**2 + y**2) >= R_E
        x = x[mask]
        y = y[mask]
        
        # Plot trajectory with label
        plt.plot(x, y, label=f'Trajectory {i+1}' + f', v = {vy[0]}', linewidth=2)

        #plt.plot(x, y)

        # Central mass point
        # plt.plot(0, 0, 'yo', label='Earth Center')

    
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Trajectories in a Gravitational Field')
    plt.legend()
    plt.grid(True)
    plt.axis('equal') # Set equal scaling
    plt.show()

    # Example usage
initial_conditions = [
    [R_E + 1e6, 0, 0, 10000],
    [R_E + 1e6, 0, 0, 10200],
    [R_E + 1e6, 0, 0, 10400],
    [R_E + 1e6, 0, 0, 10600],
    [R_E + 1e6, 0, 0, 10800],
    [R_E + 1e6, 0, 0, 11000],
    [R_E + 1e6, 0, 0, 12000],
    [R_E + 1e6, 0, 0, 13000],
    [R_E + 1e6, 0, 0, 14000]
]

plot_trajectories(initial_conditions, 20000, 10000)  # Call the function to plot trajectories
```
</details>

### Third Cosmic Velocity - Halley's comet

[![Escape Trajectory](https://mg-2025p03.github.io/physics/_pics/GP2.7.png)](https://mg-2025p03.github.io/physics/_pics/GP2.7.png)

<details>
<summary> <- Click to view the codes</summary>

```
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
```
</details>

