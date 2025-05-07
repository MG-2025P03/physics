import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, TextBox

# Initial parameters (default values)
init_num_balls = 50
init_spring_constant = 350.0
init_damping = 0.5
init_time_step = 0.03
init_y_position = 3.0

# Simulation time and frames
simulation_time = 10
frames = int(simulation_time / init_time_step)

# Set up the figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.4)  # Make space for sliders

ax.set_xlim(0, (init_num_balls - 1))  # Initial x limit
ax.set_ylim(-2, 2)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_title("Wave Simulation")
ax.grid(True)

# Create the line object for the balls (initially with default values)
x_positions = np.linspace(0, (init_num_balls - 1), init_num_balls)
y_positions = np.zeros(init_num_balls)
line, = ax.plot(x_positions, y_positions, 'bo-', markersize=8)

# Define update function (now needs to reinitialize the whole simulation)
def update(num_balls, spring_constant, damping, time_step, init_y_position):
    global y_positions, y_velocities, x_positions, frames, ani
    #Stop the old animation
    if 'ani' in globals():
        ani.event_source.stop()


    # Recalculate initial parameters and simulation time
    x_positions = np.linspace(0, (num_balls - 1), num_balls)
    y_positions = np.zeros(num_balls)
    middle_index = num_balls // 2
    y_positions[middle_index] = init_y_position
    if num_balls > 1:
        y_positions[middle_index - 1] = init_y_position / 2
    y_velocities = np.zeros(num_balls)
    frames = int(simulation_time / time_step)

    ax.set_xlim(0, (num_balls - 1))  # Reset axis limits
    line.set_data(x_positions, y_positions)

    # Function to calculate forces on each ball
    def calculate_forces(y_positions, y_velocities):
        forces = np.zeros(num_balls)
        for i in range(num_balls):
            # Spring force from the left
            if i > 0:
                extension_left = (y_positions[i] - y_positions[i - 1])
                forces[i] -= spring_constant * extension_left  # Negative sign to pull back
            # Spring force from the right
            if i < num_balls - 1:
                extension_right = (y_positions[i] - y_positions[i + 1])
                forces[i] -= spring_constant * extension_right  # Negative sign to pull back

            # Damping force (proportional to velocity)
            forces[i] -= damping * y_velocities[i]

        return forces

    def animate(frame):
        global y_positions, y_velocities

        forces = calculate_forces(y_positions, y_velocities)

        # Update velocities and positions using Euler integration
        y_velocities += forces * time_step
        y_positions += y_velocities * time_step

        line.set_data(x_positions, y_positions)  # Plot position data
        return line,



    #Recreate the animation
    ani = animation.FuncAnimation(fig, animate, frames=frames, blit=True, repeat=False)
    fig.canvas.draw_idle() #Force the draw
    return ani

# Create sliders
ax_num_balls = plt.axes([0.25, 0.3, 0.65, 0.03])
slider_num_balls = Slider(ax_num_balls, 'Num Balls', 2, 100, valinit=init_num_balls, valstep=1) #Minimum of 2 balls


ax_spring_constant = plt.axes([0.25, 0.25, 0.65, 0.03])
slider_spring_constant = Slider(ax_spring_constant, 'Spring Constant', 50, 400, valinit=init_spring_constant)

ax_damping = plt.axes([0.25, 0.2, 0.65, 0.03])
slider_damping = Slider(ax_damping, 'Damping', 0.02, 3.0, valinit=init_damping)

ax_time_step = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_time_step = Slider(ax_time_step, 'Time Step', 0.005, 0.05, valinit=init_time_step)

ax_y_position = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_y_position = Slider(ax_y_position, 'Y Position', 0.1, 4.0, valinit=init_y_position)



def slider_changed(val):
    num_balls = int(slider_num_balls.val)
    spring_constant = slider_spring_constant.val
    damping = slider_damping.val
    time_step = slider_time_step.val
    init_y_position = slider_y_position.val

    update(num_balls, spring_constant, damping, time_step, init_y_position)
slider_num_balls.on_changed(slider_changed)
slider_spring_constant.on_changed(slider_changed)
slider_damping.on_changed(slider_changed)
slider_time_step.on_changed(slider_changed)
slider_y_position.on_changed(slider_changed)


# Initial animation (with initial values)
ani = update(init_num_balls, init_spring_constant, init_damping, init_time_step, init_y_position)

# Text Fragment Analysis (Answer the question)
text_fragment = """1.00
36
36
18
5.4
4.5
0.75 -
0.50
0.25 -
9
6.4
6
5.44.8
3.6
13.63.4
3.2
3
1.81.6
2
0.00.0 0
3.6
12
3.6
9.0
3.0
2.7
A
- 6
1.8
4.5
8
- 9
1.5
0.0 - O
1.8
0
- 0
0
0
0.0
0.0
0.00
-0.25
-0.50
-0.75 -
-1.6
-1-3 -3.2
2252:2-4.6 3.2
-4.5 |12 F -12
4.8.6 1-6
-4.8
-5.4
- - 6.4
1.2
-16
-8
-9
-6
- - 12
- - 18
-1.8
-1.5
-3.0
-3.6
-4.5
-5.4
0.9
0.0
-0.9
-1.8
-1.00
-6.0
-D1
urces
17"""


def extract_numbers(text):
    numbers = []
    for line in text.splitlines():
        for word in line.split():
            try:
                number = float(word)
                numbers.append(number)
            except ValueError:
                pass
    return numbers


numbers = extract_numbers(text_fragment)


#What is the median of the positive numbers?
positive_numbers = sorted([num for num in numbers if num > 0])
if positive_numbers:
    n = len(positive_numbers)
    if n % 2 == 0:
        # Even number of elements, take the average of the middle two
        median = (positive_numbers[n // 2 - 1] + positive_numbers[n // 2]) / 2
    else:
        # Odd number of elements, take the middle one
        median = positive_numbers[n // 2]
    answer = f"The median of the positive numbers is: {median}"
else:
    answer = "No positive numbers found in the text fragment."

print(answer)



plt.show()