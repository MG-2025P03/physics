import plotly.graph_objects as go
import numpy as np

# Constants
earth_radius = 6371  # Earth radius in kilometers
scale_factor = 1.5  # Factor to adjust plotting scale for arcs
arc_radius = earth_radius * scale_factor  # Arc radius for trajectory paths

# Function to calculate an escape trajectory starting at Earth's edge at 80 degrees
def escape_trajectory(start_x, start_y, num_points, arc_radius):
    # Create arc trajectory starting at (start_x, start_y)
    arc_angle = np.linspace(0, np.pi, num_points)  # Sweep from the starting point toward upper left

    x = start_x + arc_radius * np.cos(arc_angle + np.pi)
    y = start_y + arc_radius * np.sin(arc_angle + np.pi)
    return x, y

# Calculate the starting point at 80 degrees on Earth's surface
angle_80_rad = np.radians(80)
start_x = earth_radius * np.cos(angle_80_rad)
start_y = earth_radius * np.sin(angle_80_rad)

# Define satellite trajectories
num_satellites = 6
num_points = 100
trajectories = [escape_trajectory(start_x, start_y, num_points, arc_radius) for _ in range(num_satellites)]

# Create figure
fig = go.Figure()

# Plot Earth as a circle
theta = np.linspace(0, 2 * np.pi, num_points)
earth_x = earth_radius * np.cos(theta)
earth_y = earth_radius * np.sin(theta)

fig.add_trace(go.Scatter(x=earth_x, y=earth_y, mode='lines', fill='toself',
                         name='Earth', line=dict(color='blue', width=2), showlegend=False))

# Plot satellite trajectories
colors = ['red', 'green', 'purple', 'orange', 'pink', 'cyan']  # Different colors for differentiation
for i, (x, y) in enumerate(trajectories):
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', 
                             name=f'Satellite {i+1}', line=dict(color=colors[i])))

# Chart layout
fig.update_layout(
    title='Satellite Escape Trajectories',
    xaxis=dict(
        title='X (km)',
        range=[-3 * earth_radius, 3 * earth_radius],  # Extend the range to ensure visibility
        scaleanchor='y',  # Ensures the x and y axes are on the same scale
    ),
    yaxis=dict(
        title='Y (km)',
        range=[-3 * earth_radius, 3 * earth_radius],  # Extend the range to ensure visibility
    ),
    showlegend=True,
)

# Position Earth in the lower-right quadrant by adjusting the axes' display and centering plot
fig.update_yaxes(scaleanchor = "x", scaleratio = 1)
fig.update_xaxes(constrain='domain')
fig.update_yaxes(constrain='domain', automargin=True)

# Show the plot
fig.show()