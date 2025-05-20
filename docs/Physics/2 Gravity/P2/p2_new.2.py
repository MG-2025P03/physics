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