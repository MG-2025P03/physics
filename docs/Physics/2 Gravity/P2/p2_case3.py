import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

# Constants
G = 6.67430e-11  # Universal gravitational constant, m^3 kg^-1 s^-2
M = 5.972e24     # Mass of Earth, kg
R = 6371e3       # Radius of Earth, m

# Keplerian and hyperbolic trajectories
def trajectory(v0, r0, theta, time_span):
    # Compute initial parameters
    r0_norm = np.linalg.norm(r0)
    v0_mag = np.linalg.norm(v0)
    energy = 0.5 * v0_mag**2 - G * M / r0_norm
    
    def acceleration(r):
        r_norm = np.linalg.norm(r)
        return -G * M * r / r_norm**3

    # Time variables
    dt = 10  # time step, s
    num_steps = int(time_span / dt)
    
    # Initializing arrays to store trajectory points
    trajectory_points = np.zeros((num_steps, 3))
    velocity = v0
    
    for i in range(num_steps):
        r_norm = np.linalg.norm(r0)
        if r_norm < R:  # Stop if hitting the Earth
            break
        trajectory_points[i] = r0
        a = acceleration(r0)
        # Update velocity and position using simple Euler's method
        velocity += a * dt
        r0 += velocity * dt

    return trajectory_points[:i]

# Initial conditions
r0 = np.array([R + 500e3, 0, 0])  # 500 km altitude
time_span = 10000

# Different initial velocities and trajectory types
velocities = [
    [7500, 0, 200], [7800, 0, 0], [8000, 0, -100],  # Elliptical
    [11200, 0, 50],  # Parabolic
    [13000, 0, -200], [15000, 0, 50]  # Hyperbolic
]
colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']

# Calculate and plot
data = []
for i, v in enumerate(velocities):
    traj_points = trajectory(np.array(v), r0.copy(), 0, time_span)
    x, y, z = traj_points.T
    trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color=colors[i]), name=f'Trajectory {i+1}')
    data.append(trace)

# Adding the Earth for reference
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)
x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)
earth_surface = go.Surface(x=x, y=y, z=z, colorscale='Blues', opacity=0.5, showscale=False)

layout = go.Layout(scene=dict(
    xaxis=dict(title='X (m)', range=[-80e6, 80e6]),
    yaxis=dict(title='Y (m)', range=[-80e6, 80e6]),
    zaxis=dict(title='Z (m)', range=[-80e6, 80e6])),
    title="Payload Trajectories from Earth"
)

fig = go.Figure(data=data + [earth_surface], layout=layout)
pyo.plot(fig)