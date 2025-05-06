import plotly.express as px
import pandas as pd
import numpy as np

# Constants
G = 6.674 * 10**-11  # gravitational constant in m^3 kg^-1 s^-2

# Data for all planets in the solar system
bodies = {
    "Celestial Body": [
        "Mercury", "Venus", "Earth", "Mars", 
        "Jupiter", "Saturn", "Uranus", "Neptune"
    ],
    "Mass (kg)": [
        3.3011 * 10**23, 4.8675 * 10**24, 5.972 * 10**24, 6.4171 * 10**23, 
        1.898 * 10**27, 5.683 * 10**26, 8.681 * 10**25, 1.024 * 10**26
    ],
    "Radius (m)": [
        2.4397 * 10**6, 6.0518 * 10**6, 6.371 * 10**6, 3.3895 * 10**6, 
        6.9911 * 10**7, 5.8232 * 10**7, 2.5362 * 10**7, 2.4622 * 10**7
    ]
}

# Convert data to a DataFrame
df = pd.DataFrame(bodies)

# Calculate first cosmic velocity
df["First Cosmic Velocity (m/s)"] = np.sqrt(G * df["Mass (kg)"] / df["Radius (m)"])

# Round velocities to the nearest thousand
df["First Cosmic Velocity (m/s)"] = df["First Cosmic Velocity (m/s)"].apply(lambda x: round(x, -3))

# Plot using Plotly
fig = px.bar(df,
             x="Celestial Body",
             y="First Cosmic Velocity (m/s)",
             title="First Cosmic Velocity for Solar System Planets (Rounded to Nearest 1000 m/s)",
             labels={"First Cosmic Velocity (m/s)": "First Cosmic Velocity (m/s)"},
             text="First Cosmic Velocity (m/s)")

# Update layout to show text clearly
fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')

# Show the plot
fig.show()