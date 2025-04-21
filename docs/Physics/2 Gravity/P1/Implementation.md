```{python}
import plotly.express as px
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

# Plot using Plotly
fig = px.scatter(df, 
                 x="Orbital Radius Cubed (AU³)", 
                 y="Orbital Period Squared (years²)",
                 text="Planet",
                 title="Kepler's Third Law: T² vs r³",
                 labels={"Orbital Radius Cubed (AU³)": "Orbital Radius Cubed (AU³)", "Orbital Period Squared (years²)": "Orbital Period Squared (years²)"},
                 trendline="ols")

# Update the layout for better readability
fig.update_traces(textposition='top center')
fig.update_layout(xaxis_title='Orbital Radius Cubed (AU³)',
                  yaxis_title='Orbital Period Squared (years²)',
                  showlegend=False)

# Show the plot
fig.show()
```{/python}