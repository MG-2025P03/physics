import plotly.graph_objects as go
import numpy as np

# Constants
G = 6.67430e-20  # km^3/kg/s^2, gravitational constant
earth_mass = 5.972e24  # kg
moon_mass = 7.34767309e22  # kg
earth_radius = 6371  # km
moon_radius = 1737  # km
moon_distance = 384400  # km, average distance from Earth
moon_orbit_velocity = 1.023  # km/s, average orbital velocity

def compute_gravitational_acceleration(position, mass, body_position):
    """Compute gravitational acceleration due to a celestial body."""
    displacement = body_position - position
    distance = np.linalg.norm(displacement)
    acceleration = G * mass * displacement / distance**3
    return acceleration

def simulate_earth_moon_parabolic_satellite_orbit(num_steps, time_step):
    # Initial positions and velocities
    moon_position = np.array([moon_distance, 0.0], dtype=np.float64)
    moon_velocity = np.array([0.0, moon_orbit_velocity], dtype=np.float64)
    
    # Starting the satellite with a velocity that would result in a parabolic trajectory
    satellite_position = np.array([-moon_distance * 2, 0.0], dtype=np.float64)
    satellite_velocity = np.array([0.0, np.sqrt(2 * G * earth_mass / np.linalg.norm(satellite_position))])  # parabolic speed at this distance

    earth_position = np.array([0.0, 0.0], dtype=np.float64)
    
    moon_positions = [moon_position.copy()]
    satellite_positions = [satellite_position.copy()]

    for _ in range(num_steps):
        # Gravitational accelerations
        accel_moon_earth = compute_gravitational_acceleration(moon_position, earth_mass, earth_position)
        accel_satellite_earth = compute_gravitational_acceleration(satellite_position, earth_mass, earth_position)
        accel_satellite_moon = compute_gravitational_acceleration(satellite_position, moon_mass, moon_position)

        # Total acceleration on the satellite
        accel_satellite = accel_satellite_earth + accel_satellite_moon

        # Update velocities
        moon_velocity += accel_moon_earth * time_step
        satellite_velocity += accel_satellite * time_step

        # Update positions
        moon_position += moon_velocity * time_step
        satellite_position += satellite_velocity * time_step

        moon_positions.append(moon_position.copy())
        satellite_positions.append(satellite_position.copy())

    return np.array(moon_positions), np.array(satellite_positions)

# Simulation parameters
time_span = 30 * 24 * 3600  # 30 days in seconds
time_step = 1800  # 30-minute time steps
num_steps = int(time_span / time_step)

# Compute orbits
moon_positions, satellite_positions = simulate_earth_moon_parabolic_satellite_orbit(num_steps, time_step)

# Extract x and y coordinates
x_moon, y_moon = moon_positions[:, 0], moon_positions[:, 1]
x_satellite, y_satellite = satellite_positions[:, 0], satellite_positions[:, 1]

# Data for Earth
phi = np.linspace(0, 2 * np.pi, 100)
x_earth = earth_radius * np.cos(phi)
y_earth = earth_radius * np.sin(phi)

# Plotting
fig = go.Figure()

# Plot Earth
fig.add_trace(go.Scatter(x=x_earth, y=y_earth, fill='toself', name='Earth', line_color='blue'))

# Plot Moon Orbit
fig.add_trace(go.Scatter(
    x=x_moon, y=y_moon,
    mode='lines',
    name='Moon Orbit',
    line=dict(color='gray', width=2)
))

# Plot Parabolic Satellite Trajectory
fig.add_trace(go.Scatter(
    x=x_satellite, y=y_satellite,
    mode='lines',
    name='Satellite Parabolic Trajectory',
    line=dict(color='red', width=2)
))

# Set plot range to show the whole Earth-Moon system and satellite path
fig.update_xaxes(range=[-moon_distance * 3, moon_distance * 3])
fig.update_yaxes(range=[-moon_distance * 3, moon_distance * 3])

# Add titles and labels
fig.update_layout(
    title='Satellite Parabolic Trajectory Entering the Earth-Moon System',
    xaxis_title='Distance (km)',
    yaxis_title='Distance (km)',
    legend_title='Celestial Bodies'
)

# Show plot
fig.show()