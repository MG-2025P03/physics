import numpy as np
import matplotlib.pyplot as plt

# Constant Parameters
G = 6.674e-11  # Gravitational constant (m^3/kg/s^2)
M = 5.972e24   # The mass of a larger body, e.g. the Earth (kg)
m = 200       # The mass of a smaller body, e.g. a satellite (kg)

# Initial conditions
r0 = 7e6  # Initial distance from the center of mass of the larger body(m)
v0 = 4300  #  Initial orbital velocity (m/s)
theta0 = 0  # Initial angle in radians

# Time parameters
T = 6000  # Simulation time (s)
N = 100_000  # Number of time steps
dt = T / N

# Tables for position and speed
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

# Warunki początkowe
x[0] = r0 * np.cos(theta0)
y[0] = r0 * np.sin(theta0)
vx[0] = -v0 * np.sin(theta0)
vy[0] = v0 * np.cos(theta0)

# Numerical integration (Euler's method)
for i in range(1, N):
    r = np.sqrt(x[i - 1]**2 + y[i - 1]**2)  # Distance from center of mass
    ax = -G * M * x[i - 1] / r**3          # Acceleration in x axis
    ay = -G * M * y[i - 1] / r**3          # Acceleration in y axis
    
    # Using the previous velocity to update the current velocity
    vx[i] = vx[i - 1] + ax * dt
    vy[i] = vy[i - 1] + ay * dt
    
    # Using the previous position to update the current position
    x[i] = x[i - 1] + vx[i - 1] * dt
    y[i] = y[i - 1] + vy[i - 1] * dt

# Wizualizacja trajektorii
plt.figure(figsize=(8, 8))
plt.plot(x, y, label="Trajectory")
plt.plot(0, 0, 'ro', label="Central body (e.g. Earth)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Trajectory of a satellite/small body in a parabolic orbit")
plt.legend(loc='lower right')
plt.grid()
plt.axis('equal')
plt.show()