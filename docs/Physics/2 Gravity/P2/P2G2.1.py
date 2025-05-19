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