import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Runge-Kutta method to integrate the Lorentz force equation
def runge_kutta(t, dt, state, charge, mass, E_field, B_field):
    def lorentz_force(state, q, m, E, B):
        position, velocity = state[:3], state[3:]
        v_cross_B = np.cross(velocity, B)
        acceleration = (q * (E + v_cross_B)) / m
        return np.concatenate((velocity, acceleration))

    k1 = lorentz_force(state, charge, mass, E_field, B_field)
    k2 = lorentz_force(state + k1 * dt / 2, charge, mass, E_field, B_field)
    k3 = lorentz_force(state + k2 * dt / 2, charge, mass, E_field, B_field)
    k4 = lorentz_force(state + k3 * dt, charge, mass, E_field, B_field)
    
    return state + (k1 + 2*k2 + 2*k3 + k4) * dt / 6

# Initial parameters
Electric_Field_strength = np.array([1e5, 0, 0])  # Electric field (V/m)
Magnetic_Field_strength = np.array([0, 0, 1.0])  # Magnetic field (T)
Initial_velocity = np.array([0, 1e6, 0])         # Initial velocity (m/s)
charge = 1.6e-19                                 # Charge (Coulombs)
mass = 9.11e-31                                  # Mass (kg)

# Time settings
t_max = 1e-6
dt = 1e-9
num_steps = int(t_max / dt)

# Initial state [x, y, z, vx, vy, vz]
initial_state = np.concatenate((np.zeros(3), Initial_velocity))

# Arrays to store positions
positions = np.zeros((num_steps, 3))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the initial trajectory
state = initial_state
for i in range(num_steps):
    state = runge_kutta(i * dt, dt, state, charge, mass, Electric_Field_strength, Magnetic_Field_strength)
    positions[i] = state[:3]
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], label='Trajectory')

# Set labels and title
ax.set_title('Particle Trajectory under Lorentz Force')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=25, azim=45)
ax.legend()

# Add sliders for user input
ax_electric = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_magnetic = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_velocity = plt.axes([0.25, 0.2, 0.65, 0.03])
ax_charge = plt.axes([0.25, 0.25, 0.65, 0.03])
ax_mass = plt.axes([0.25, 0.3, 0.65, 0.03])

slider_electric = Slider(ax_electric, 'Electric Field (V/m)', 1e3, 1e6, valinit=Electric_Field_strength[0], valstep=1e3)
slider_magnetic = Slider(ax_magnetic, 'Magnetic Field (T)', 0.1, 5.0, valinit=Magnetic_Field_strength[2], valstep=0.1)
slider_velocity = Slider(ax_velocity, 'Initial Velocity (m/s)', 1e3, 1e7, valinit=Initial_velocity[1], valstep=1e3)
slider_charge = Slider(ax_charge, 'Charge (C)', 1e-20, 1e-18, valinit=charge, valstep=1e-20)
slider_mass = Slider(ax_mass, 'Mass (kg)', 1e-32, 1e-30, valinit=mass, valstep=1e-32)

def update(val):
    global Electric_Field_strength, Magnetic_Field_strength, Initial_velocity, charge, mass
    Electric_Field_strength[0] = slider_electric.val
    Magnetic_Field_strength[2] = slider_magnetic.val
    Initial_velocity[1] = slider_velocity.val
    charge = slider_charge.val
    mass = slider_mass.val

    # Clear the previous trajectory
    ax.clear()

    # Recalculate and plot the new trajectory
    state = initial_state
    for i in range(num_steps):
        state = runge_kutta(i * dt, dt, state, charge, mass, Electric_Field_strength, Magnetic_Field_strength)
        positions[i] = state[:3]
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], label='Trajectory')

    # Update the plot
    ax.set_title('Particle Trajectory under Lorentz Force')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.view_init(elev=25, azim=45)
    ax.legend()
    fig.canvas.draw_idle()

slider_electric.on_changed(update)
slider_magnetic.on_changed(update)
slider_velocity.on_changed(update)
slider_charge.on_changed(update)
slider_mass.on_changed(update)

plt.show()