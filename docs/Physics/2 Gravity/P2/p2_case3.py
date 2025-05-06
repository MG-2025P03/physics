import plotly.graph_objects as go
import numpy as np

# Constants
g = 9.81  # m/s², acceleration due to gravity
v0 = 500  # Initial velocity in m/s
altitude = 10000  # Initial altitude in meters
earth_radius = 6371000  # Earth's radius in meters

# Function to calculate trajectory
def get_trajectory(v0, g, time):
    return v0 * time - 0.5 * g * time**2

# Time array
time_of_flight = int(2 * v0 / g)
time = np.linspace(0, time_of_flight, num=1000)  # Up to the time of free fall

# Specified starting points (horizontal displacement)
start_points = [5000, 7000, 9000, 11000, 13000, 15000]

# Create a figure
fig = go.Figure()

# Add trajectories and landing points for each payload
landing_points = []
for start in start_points:
    trajectory = get_trajectory(v0, g, time)
    x_path = start + v0 * time
    y_path = altitude + trajectory
    fig.add_trace(go.Scatter(x=x_path, y=y_path, mode='lines', name=f'Start at {start}m'))

    # Calculate landing point
    landing_x = start + v0 * time_of_flight
    landing_points.append((landing_x, 0))  # landing_y is always 0

# Add Earth as a circle
theta = np.linspace(0, 2 * np.pi, 100)
earth_x = earth_radius * np.cos(theta)
earth_y = earth_radius * np.sin(theta)
fig.add_trace(go.Scatter(x=earth_x, y=earth_y, mode='lines', fill='toself', fillcolor='lightblue', name="Earth"))

# Mark landing points
for point in landing_points:
    fig.add_trace(go.Scatter(x=[point[0]], y=[point[1]], mode='markers+text',
                             marker=dict(size=10, color='red'), text=["Landing"],
                             textposition="top right"))

# Update layout
fig.update_layout(
    title="Trajectories of Freely Released Payloads Near Earth",
    xaxis_title="Horizontal Distance (m)",
    yaxis_title="Altitude (m)",
    legend_title="Starting Point",
    xaxis=dict(range=[0, 15000 + 2 * v0 * time_of_flight]),
    yaxis=dict(scaleanchor="x", scaleratio=1, range=[-3000000, altitude + 5000])  # Adjust the y-axis range
)

# Show the figure
fig.show()