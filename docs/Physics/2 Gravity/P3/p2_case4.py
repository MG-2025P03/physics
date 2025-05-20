import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 100                    # mass of the payload in kg
g = 9.81                   # gravitational acceleration in m/s^2
R_earth = 6371           # radius of the Earth in meters
altitude = 2000            # starting altitude above the Earth's center
initial_x_position = 0     # initial horizontal position (centered)
initial_velocity = 150     # initial horizontal velocity in m/s

# Initial conditions
y = R_earth + altitude     # initial position (altitude above Earth's center)
x = initial_x_position      # initial horizontal position

# Define the desired impact angle
impact_angle = 15          # Impact angle in degrees
impact_angle_rad = np.radians(impact_angle)

# Calculate the vertical component of the initial velocity based on the impact angle
v_x = initial_velocity      # Horizontal component remains as defined
v_y = -initial_velocity * np.tan(impact_angle_rad)  # Negative because it moves downwards

# Prepare to store trajectory
trajectory = []

# Time parameters
dt = 0.1   # time step in seconds
t = 0      # initial time

# Simulation loop
while y >= (R_earth*0.81):  # Continue until payload hits the Earth
    # Calculate gravitational force (F = GMm/r^2)
    F_gravity = (m * g * R_earth**2) / (y**2)  # Gravitational force on payload
    
    # Calculate the acceleration due to gravity
    a_y = -F_gravity / m  # Negative because it acts downwards
    
    # Update velocities
    v_y += a_y * dt

    # Update positions
    x_new = x + v_x * dt
    y_new = y + v_y * dt

    # Store the current trajectory data
    trajectory.append((x_new, y_new))  # Append as a tuple (x, y)
    
    # Update for the next iteration
    x, y, t = x_new, y_new, t + dt

# Convert trajectory to a NumPy array for easier plotting
trajectory = np.array(trajectory)

# Prepare Earth representation as a flat circle
earth_x = np.linspace(-R_earth, R_earth, 100)
earth_y = np.sqrt(R_earth**2 - earth_x**2)  # half-circle for the Earth
earth_y = np.concatenate((earth_y, -earth_y[::-1]))  # complete the circle
earth_x = np.concatenate((earth_x, earth_x[::-1]))  # repeat x values for the full circle

# Plotting
plt.figure(figsize=(12, 12))
plt.plot(trajectory[:, 0], trajectory[:, 1], label='Trajectory', color='red')
plt.fill(earth_x, earth_y, color='blue', alpha=0.5, label='Earth')

# Setting plot limits, title, and labels
plt.title("Trajectory of Payload Hitting Earth at 2000m Altitude with a velocity of 150 m/s")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Altitude (m)")
plt.xlim(-10000, 10000)  # Adjust x limits
plt.ylim(0, 10000)       # Adjust y limits to view trajectory and impact angle
# plt.axhline(R_earth, color='black', lw=1)  # Earth surface line
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')  # Equal scaling for x and y

# Show the plot
plt.show()