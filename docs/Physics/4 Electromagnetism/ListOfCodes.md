#List of Codes

## Figure 1 - Circular Motion of a Charged Particle in a Magnetic Field

- This code simulates the circular motion of a charged particle in a uniform magnetic field.

- The particle's trajectory is plotted in the x-y plane, showing the circular path it takes due to the Lorentz force.

```
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
```

## Figure 2 - Circular Motion of a Charged Particle in a Magnetic Field (3D)

- This code simulates the circular motion of a charged particle in a uniform magnetic field in 3D space.
- The trajectory is plotted in 3D, with time represented along the z-axis.
- The particle moves in a circular path in the x-y plane, while the z-coordinate increases linearly with time.
- This represents the particle's motion through time, showing how it moves in a helical path in 3D space.

```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v0 = 1e6  # Initial velocity of the particle (m/s)
t_max = 1e-7  # Simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Calculate the radius and angular frequency
r = m * v0 / (q * B)
omega = q * B / m

# Parametric equations for circular motion in 3D
x = r * np.cos(omega * time)
y = r * np.sin(omega * time)
z = time  # Representing time along the z-axis

# Create the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, label='Particle trajectory')
ax.set_title('Circular Motion of a Charged Particle in a Magnetic Field (3D)')
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('Time (s)')
ax.scatter([0], [0], [0], color='r', label='Center of motion', zorder=5)  # Center point

plt.legend()
plt.show()
```

## Figure 3 -  Helical Motion of a Charged Particle in Crossed E and B Fields

- This script simulates the helical motion of a charged particle in crossed electric and magnetic fields.
- The particle is subjected to a constant electric field in the x-direction and a constant magnetic field in the z-direction.   
- The motion is calculated using the Lorentz force law, and the trajectory is plotted in 3D.
- The simulation parameters can be adjusted to observe different behaviors of the particle.
- The code uses numpy for numerical calculations and matplotlib for plotting.
- The trajectory is visualized in a 3D plot, showing the helical path of the particle as it moves through the fields.

```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
E = 1e3  # Electric field strength (V/m)
v0 = 2e6  # Initial velocity of the particle (m/s)
t_max = 1e-7  # Maximum time for the simulation (s)
num_points = 1000  # Number of points in the simulation

# Time discretization
time = np.linspace(0, t_max, num_points)

# Initialize position and velocity arrays
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))

# Initial conditions
velocity[0] = [v0, 0, 0]  # Initial velocity in x-direction

# Time increment
dt = t_max / num_points

# Main loop to calculate position and velocity
for i in range(1, num_points):
    v = velocity[i-1]
    F_electric = q * np.array([E, 0, 0])          # Electric force
    F_magnetic = q * np.cross(v, [0, 0, B])       # Magnetic force
    F_total = F_electric + F_magnetic
    a = F_total / m                               # Acceleration

    # Update velocity and position
    velocity[i] = velocity[i-1] + a * dt
    position[i] = position[i-1] + velocity[i] * dt

# Plotting the results
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Particle trajectory')
ax.set_title('Helical Motion of a Charged Particle in Crossed E and B Fields')
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')
ax.set_zlabel('z-position (m)')

plt.legend()
plt.show()
```

## Figure 4 - Mass Spectrometer: Ion Trajectories Based on Mass-to-Charge Ratio

- This code simulates the trajectories of ions in a mass spectrometer based on their mass-to-charge ratios.
- It uses the Lorentz force law to calculate the motion of ions in electric and magnetic fields.
- The code generates a plot showing the trajectories of three different ions with varying mass-to-charge ratios.
- The plot illustrates how the radius of curvature of the ion paths depends on their mass-to-charge ratios.
- The ions are accelerated by an electric field and then deflected by a magnetic field, creating circular paths.
- The code uses NumPy for numerical calculations and Matplotlib for plotting the trajectories.

````
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
````

## Figure 5 - 3D Representation of Plasma Confinement in a Toroidal Field

- This code generates a 3D plot of a toroidal magnetic field, representing plasma confinement in fusion reactors.
- The plot includes a toroidal surface and magnetic field lines to illustrate the concept of plasma confinement.
- The code uses NumPy for numerical calculations and Matplotlib for plotting.
- The toroidal field is a common configuration in fusion reactors, such as tokamaks, where plasma is confined in a donut-shaped magnetic field.

````
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for toroidal field
radius_major = 1.0  # Major radius of the torus (distance from center of tube to center of torus)
radius_minor = 0.2  # Minor radius of the torus (radius of the tube)

# Create data for a torus
theta = np.linspace(0, 2 * np.pi, 100)  # Angle around the torus
phi = np.linspace(0, 2 * np.pi, 100)  # Angle along the torus' tube
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for the torus
x = (radius_major + radius_minor * np.cos(phi)) * np.cos(theta)
y = (radius_major + radius_minor * np.cos(phi)) * np.sin(theta)
z = radius_minor * np.sin(phi)

# Create the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the torus surface
ax.plot_surface(x, y, z, color='c', alpha=0.5, rstride=5, cstride=5, edgecolor='none')

# Plot magnetic field lines
num_lines = 8
for i in range(num_lines):
    angle_offset = (i / num_lines) * 2 * np.pi
    x_line = (radius_major + radius_minor * np.cos(phi)) * np.cos(theta + angle_offset)
    y_line = (radius_major + radius_minor * np.cos(phi)) * np.sin(theta + angle_offset)
    z_line = radius_minor * np.sin(phi)
    ax.plot(x_line[0, :], y_line[0, :], z_line[0, :], color='r')

# Set labels and title
ax.set_title('3D Representation of Plasma Confinement in a Toroidal Field')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=30, azim=60)  # Better viewing angle

plt.show()
````

## Figure 6 - Circular Motion in a Uniform Magnetic Field

- This script simulates the motion of a charged particle in a uniform magnetic field.
- The particle moves in a circular path due to the Lorentz force acting on it.
- The simulation visualizes the trajectory of the particle and the magnetic field lines.
- The code uses NumPy for numerical calculations and Matplotlib for plotting.
- The 3D plot shows the circular motion of the particle and the magnetic field lines.
- The particle is assumed to have a charge of 1.6e-19 C and a mass of 9.11e-31 kg.
- The magnetic field strength is set to 1.0 Tesla, and the initial velocity of the particle is 1e6 m/s.
- The simulation runs for a maximum time of 1e-7 seconds with 1000 points in the time array.
- The radius of the circular motion and the angular frequency are calculated based on the charge, mass, and magnetic field strength.
- The parametric equations for circular motion are used to calculate the x and y coordinates of the particle's trajectory.
- The z coordinate is set to zero, indicating no motion in the z-direction.
- The 3D plot is created using Matplotlib's Axes3D module, and the trajectory of the particle is plotted in blue.
- The center of motion is marked with a red dot, and several magnetic field lines are plotted in green.
- The plot is labeled with appropriate titles and axis labels, and the viewing angle is adjusted for better visualization.



````
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
B = 1.0  # Magnetic field strength (Tesla)
v0 = 1e6  # Initial velocity magnitude of the particle (m/s)
t_max = 1e-7  # Maximum simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Calculate the radius and angular frequency
r = m * v0 / (q * B)
omega = q * B / m

# Parametric equations for circular motion
x = r * np.cos(omega * time)
y = r * np.sin(omega * time)
z = np.zeros_like(time)  # No motion in the z-direction

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the circular motion
ax.plot(x, y, z, label='Particle trajectory', color='b')
ax.scatter([0], [0], [0], color='r', label='Center of motion', zorder=5)

# Plot some magnetic field lines
bz = np.linspace(-1, 1, num_points)
bx = np.zeros_like(bz) + r  # Offset field lines
by = np.zeros_like(bz)
for bx_offset in np.linspace(-r, r, 5):
    ax.plot(bx + bx_offset, by, bz, color='g', alpha=0.3)

# Set labels and title
ax.set_title('Circular Motion in a Uniform Magnetic Field')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis (Field Direction)')
ax.view_init(elev=25, azim=45)  # Adjust viewing angle
ax.legend()

plt.show()
````

## Figure 7 - Particle in Electric and Magnetic Fields

- This code simulates the motion of a charged particle in a uniform electric field and a uniform magnetic field.
- The particle experiences a Lorentz force due to the electric and magnetic fields, and its trajectory is plotted in 3D.
- The simulation uses numerical integration to update the particle's position and velocity over time.
- The electric field is assumed to be in the x-direction, while the magnetic field is in the z-direction.
- The initial velocity of the particle is set to zero for simplicity, but can be modified as needed.
- The simulation parameters can be adjusted to explore different scenarios, such as varying the strength of the fields or the mass of the particle.
- The resulting plot shows the trajectory of the particle in 3D space, illustrating the combined effects of the electric and magnetic fields on its motion.
- The code uses NumPy for numerical calculations and Matplotlib for plotting the trajectory.
- The trajectory is visualized in a 3D plot, with the x-axis representing the electric field direction, the y-axis as a free axis, and the z-axis representing the magnetic field direction.
- The plot includes labels for the axes and a legend indicating the particle's trajectory.
- The viewing angle of the plot is adjusted for better visualization.

````
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
q = 1.6e-19  # Charge of the particle (Coulombs)
m = 9.11e-31  # Mass of the particle (kg)
E = 1e5  # Electric field magnitude (V/m)
B = 1.0  # Magnetic field strength (T)
v0 = 0  # Initial velocity (m/s), assume starting from rest for simplicity
t_max = 1e-6  # Maximum simulation time (s)
num_points = 1000  # Number of points in the simulation

# Time array
time = np.linspace(0, t_max, num_points)

# Initial velocity and acceleration
v_initial = np.array([v0, 0, 0])  # Start with some initial velocity
a_electric = np.array([q * E / m, 0, 0])  # Acceleration due to electric field

# Magnetic field direction
B_field = np.array([0, 0, B])

# Initialize arrays for position and velocity
position = np.zeros((num_points, 3))
velocity = np.zeros((num_points, 3))
velocity[0] = v_initial

# Numerical integration
dt = t_max / num_points
for i in range(1, num_points):
    v = velocity[i-1]
    F_magnetic = q * np.cross(v, B_field)  # Lorentz force component due to magnetic field
    a_magnetic = F_magnetic / m
    a_total = a_electric + a_magnetic  # Total acceleration
    
    # Update velocity and position
    velocity[i] = velocity[i-1] + a_total * dt
    position[i] = position[i-1] + velocity[i] * dt

# Plotting the trajectory
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(position[:, 0], position[:, 1], position[:, 2], label='Particle trajectory', color='b')

# Set labels and title
ax.set_title('Motion in Combined Uniform Electric and Magnetic Fields')
ax.set_xlabel('X Axis (Electric Field Direction)')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis (Magnetic Field Direction)')
ax.view_init(elev=25, azim=60)  # Adjust viewing angle
ax.legend()

plt.show()
````