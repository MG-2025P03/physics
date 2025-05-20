# Background

In analyzing the possible trajectories of a payload released near Earth, we must consider the shape of the path determined by its initial conditions, primarily velocity and altitude. Trajectories can generally be categorized into three types: elliptical, parabolic, and hyperbolic. Here's how these trajectories relate to orbital insertion, reentry, and escape scenarios, along with a conceptual framework for numerical analysis.
Types of Trajectories

## Elliptical Trajectory

Description: An elliptical trajectory implies an orbit where the gravitational force of the Earth acts as the centripetal force keeping the payload in a closed orbit. An ellipse includes circular orbits as a special case where the eccentricity is zero.
Scenario: If the payload is released with a velocity below escape velocity $<v_2$ but above orbital velocity $v_1$, it will enter an elliptical orbit.
Use in Space Exploration: This is desirable for satellites that need to orbit Earth or other celestial bodies.

## Parabolic Trajectory

Description: A parabolic trajectory indicates that the payload is on the threshold of escape, having just enough energy to break free from Earth's gravity, but not more.
Scenario: Occurs at exactly the escape velocity $v_2$. This is a theoretical construct as maintaining exactly parabolic conditions is practically challenging.
Use in Space Exploration: Useful for trajectory analysis; practically rare due to precise conditions needed.

## Hyperbolic Trajectory

Description: In a hyperbolic trajectory, the payload has excess energy compared to the parabolic trajectory, indicating that it will escape Earth’s gravitational field.
Scenario: When the payload's velocity exceeds escape velocity $>v_2$.
Use in Space Exploration: Required for missions aiming to leave Earth permanently, for interplanetary and interstellar missions.

## Numerical Analysis of Trajectories

To perform a numerical analysis of a payload's trajectory, we’ll use Newton's laws of motion and gravitational forces. The following steps outline the numerical computation process:

Initial Conditions:

Position: Initial altitude above Earth.
Velocity: Initial speed and direction of the payload.

## Mathematical Model

Use a differential equation based on Newton's second law of motion and gravitational attraction:

$$
\mathbf{F} = m \cdot \mathbf{a} = -\frac{GMm}{r^2} \hat{r}
$$

Where:

$m$ is the mass of the payload<br/>
$G$ is the gravitational constant<br/>
$M$ is the mass of Earth<br/>
$r$ is the distance between the Earth's center and the payload<br/>
$\hat{r}$ is the unit vector along the radial direction.

## Numerical Integration

To compute the trajectory of a payload released from a certain altitude with specific initial conditions, we can apply numerical methods to solve the equations of motion under the influence of gravity and atmospheric drag. Below is a step-by-step process including the necessary equations and numerical approach.

Example Scenario

Let’s consider a payload released from a height of 10 km (10,000 meters) with an initial horizontal velocity of 300 m/s. 

Given Parameters

Initial Position: 

$y_0 = 10,000 , \text{m}$ (altitude)

$x_0 = 0 , \text{m}$ (horizontal position)

Initial Velocity:  

$v_{y0} = 0 , \text{m/s}$ (vertical velocity at release)

$v_{x0} = 300 , \text{m/s}$ (horizontal velocity)

Mass of Payload: $m = 10 , \text{kg}$ (assumed for drag calculations)

Drag Coefficient: $C_d = 0.8$ (assumed for a streamlined object)

Cross-sectional Area: $A = 0.1 , \text{m}^2$ (assumed)

Air Density $\rho$: 
$\rho = 0.4135 , \text{kg/m}^3$ (approximate value at 10 km altitude)

Gravitational Acceleration: $g = 9.81 , \text{m/s}^2$

Equations of Motion Forces Acting on the Payload:

Gravitational Force:

$$
F_g = m \cdot g
$$

Drag Force:

$$
F_d = \frac{1}{2} \cdot C_d \cdot A \cdot \rho \cdot v^2
$$

Where $v$ is the speed of the payload, calculated as:

$$
v = \sqrt{v_x^2 + v_y^2}
$$

Equations of Motion:

Horizontal Motion:
$$
\frac{d^2x}{dt^2} = -\frac{F_d \cdot v_x}{m} \quad \text{(drag only)}
$$

Vertical Motion:
$$
\frac{d^2y}{dt^2} = -g - \frac{F_d \cdot v_y}{m} \quad \text{(gravity + drag)}
$$

Numerical Integration
To compute the trajectory, we will use a numerical integration method, such as Euler’s method or the Runge-Kutta method. For simplicity, we'll use Euler’s method here.

Time Step and Initialization
Time Step: $dt = 0.1 , \text{s}$

Total Time: $T = 100 , \text{s}$ (simulation time)

Trajectory Calculation Steps
Initialize Variables:

$$
t = 0, \quad x = 0, \quad y = 10,000, \quad v_x = 300, \quad v_y = 0
$$

Loop Until Payload Hits the Ground:

In each iteration while (y > 0):

Calculate the speed:

$$
v = \sqrt{v_x^2 + v_y^2}
$$

Calculate drag force:
$$
F_d = 0.5 \cdot C_d \cdot A \cdot \rho \cdot v^2
$$  

Update acceleration:
$$
a_x = -\frac{F_d \cdot v_x}{m}, \quad a_y = -g - \frac{F_d \cdot v_y}{m}
$$

Update velocities:
$$
v_x = v_x + a_x \cdot dt, \quad v_y = v_y + a_y \cdot dt
$$

Update positions:
$$
x = x + v_x \cdot dt, \quad y = y + v_y \cdot dt
$$

Update time:
$$
t = t + dt
$$

### Trajectory of Freely Released Payload

[![Escape Trajectory](https://mg-2025p03.github.io/physics/_pics/G3.png)](https://mg-2025p03.github.io/physics/_pics/G3.png)

