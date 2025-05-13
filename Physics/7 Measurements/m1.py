import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_gravity_simulation(num_points: int) -> None:
    # Given values
    computed_g = 9.33  # Computed gravitational acceleration in m/s²
    true_g = 9.81      # Earth's actual gravitational acceleration in m/s²

    # Ratio of computed_g to true_g
    ratio = computed_g / true_g

    # Determine the size of the rectangle for computed gravity
    rect_size = ratio  # As a proportion of the full plotting area (1x1)

    # Number of points representing computed gravity
    num_points_computed = int(num_points * ratio)
    
    # Number of points representing Earth's gravity (outside the rectangle)
    num_points_earth = num_points - num_points_computed

    # Generate random points within the rectangle for computed gravity
    x_computed = np.random.uniform(0, rect_size, num_points_computed)
    y_computed = np.random.uniform(0, rect_size, num_points_computed)

    # Generate random points outside the rectangle for Earth's gravity
    x_earth = np.concatenate((
        np.random.uniform(0, 1, num_points_earth // 2),  # Left and right space
        np.random.uniform(rect_size, 1, num_points_earth // 2)  # Top and bottom space
    ))
    y_earth = np.concatenate((
        np.random.uniform(rect_size, 1, num_points_earth // 2),  # Top and bottom space
        np.random.uniform(0, 1, num_points_earth // 2)  # Left and right space
    ))

    # Plot the results
    plt.figure(figsize=(8, 8))
    
    # Plot points for computed gravity inside the rectangle
    plt.scatter(x_computed, y_computed, color='blue', s=1, label='Computed Gravity (9.33 m/s²)')
    
    # Plot points for Earth's gravity outside the rectangle
    plt.scatter(x_earth, y_earth, color='red', s=1, label="Earth's Gravity (9.81 m/s²)")

    # Draw rectangle boundary for computed gravity
    rectangle = plt.Rectangle((0, 0), rect_size, rect_size, color='blue', fill=False, linestyle='dashed', linewidth=1)
    plt.gca().add_artist(rectangle)

    # Enhance plot with titles and labels
    plt.title('Monte Carlo Simulation: Gravity Error Representation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the simulation with a specified number of points
monte_carlo_gravity_simulation(10000)