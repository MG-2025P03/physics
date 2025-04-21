```{python}
import plotly.graph_objects as go
import pandas as pd

# Data for the planets in the solar system
data = {
    "Planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "Orbital Radius (AU)": [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.20, 30.05],
    "Orbital Period (years)": [0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.79]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Calculate the square of the orbital period and the cube of the orbital radius
df["Orbital Period Squared (years²)"] = df["Orbital Period (years)"]**2
df["Orbital Radius Cubed (AU³)"] = df["Orbital Radius (AU)"]**3

# Create the figure
fig = go.Figure()

# Add a scatter trace for the planets
fig.add_trace(go.Scatter(
    x=df["Orbital Radius Cubed (AU³)"],
    y=df["Orbital Period Squared (years²)"],
    mode='markers+text',
    text=df["Planet"],
    textposition='top center',
    name='Planets',
    marker=dict(size=10)
))

# Add a line trace from the origin to each planet's data point
for i, row in df.iterrows():
    fig.add_trace(go.Scatter(
        x=[0, row["Orbital Radius Cubed (AU³)"]],
        y=[0, row["Orbital Period Squared (years²)"]],
        mode='lines',
        line=dict(dash='dot'),
        name=f'Line to {row["Planet"]}'
    ))

# Update layout for logarithmic axes
fig.update_layout(
    title="Kepler's Third Law: Lines from Origin to Planets (Logarithmic Scale)",
    xaxis_title='Orbital Radius Cubed (AU³) [Log Scale]',
    yaxis_title='Orbital Period Squared (years²) [Log Scale]',
    xaxis_type="log",
    yaxis_type="log",
    showlegend=False,
    margin=dict(l=20, r=20, t=30, b=20)
)

# Show the plot
fig.show()

fig.write_html('p1_gravity.html', include_plotlyjs='cdn')
```
 [![Keplers Third Law](https://mg-2025p03.github.io/physics/_pics/Keplers.png "Keplers Third Law")](https://mg-2025p03.github.io/physics/Physics/2%20Gravity/P1/p1_gravity.html)