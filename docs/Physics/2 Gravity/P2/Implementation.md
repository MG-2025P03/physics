# Simulations

## Orbital velocity

### First Cosmic Velocity - Trajectory of a small satellite body in parabolic orbit

<details>
<summary> <- Click to view the codes</summary>

```
import plotly.graph_objects as go
import numpy as np

# Constants
G = 6.674 * 10**-2  # gravitational constant in m^3 kg^-1 s^-2
mass_earth = 5.972 * 10**2.0  # mass of Earth in kg
mass_moon = 7.342 * 10**1.8  # mass of Moon in kg
radius_earth = 6.371 * 10**6  # radius of Earth in meters
average_moon_distance = 3.844 * 10**7  # average distance from Earth to Moon in meters

# Orbital parameters
eccentricity = 0.0549  # eccentricity of the Moon's orbit
semi_major_axis = average_moon_distance - radius_earth  # semi-major axis of the orbit

# Function to generate the Moon's orbit
def generate_moon_orbit(num_points=50):
    theta = np.linspace(0, 2 * np.pi, num_points)  # Angle array for drawing the ellipse
    r = semi_major_axis * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))  # Radius from center (polar form)
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Offset by Earth’s radius to position the Moon's orbit around Earth
    x += radius_earth
    return x, y

# Set up the plot
fig = go.Figure()

# Add the Earth's position
fig.add_trace(go.Scatter(
    x=[0],  # Earth's position at origin
    y=[0],
    mode='markers',
    name="Earth",
    marker=dict(size=12, color='blue'),
    text="Earth"
))

# Generate and add the Moon's orbit
x_orbit, y_orbit = generate_moon_orbit()
fig.add_trace(go.Scatter(
    x=x_orbit / 1e4,  # Convert to kilometers for display
    y=y_orbit / 1e4,
    mode='lines',
    name="Moon's Orbit",
    line=dict(color='gray', width=2)
))

# Layout settings
fig.update_layout(
    title="Moon's Orbit Around Earth",
    xaxis=dict(
        title="Distance (km)",
        showgrid=False,
        zeroline=False,
        scaleanchor="y",  # Ensures y is proportional to x
    ),
    yaxis=dict(
        title="Distance (km)",
        showgrid=False,
        zeroline=False
    ),
    showlegend=True
)

# Show the plot
fig.show()
```

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

[![Escape Trajectory](https://mg-2025p03.github.io/physics/_pics/G2P2.2.png)](https://mg-2025p03.github.io/physics/_pics/G2P2.2.png)

