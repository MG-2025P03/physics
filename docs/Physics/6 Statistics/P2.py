import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points: int) -> float:
    # Generate random points
    x_points = np.random.uniform(0, 1, num_points)
    y_points = np.random.uniform(0, 1, num_points)
    
    # Determine which points are inside the unit quarter circle
    inside_circle = x_points**2 + y_points**2 <= 1
    
    # Calculate the ratio
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    
    # Plot the points
    plt.figure(figsize=(8, 8))
    plt.scatter(x_points, y_points, c=inside_circle, cmap='coolwarm', s=1)
    plt.title(f"Monte Carlo Simulation for Estimating π\nEstimated π ≈ {pi_estimate:.4f}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
    return pi_estimate

# Run the simulation with a specified number of points
pi_estimate = monte_carlo_pi(10000)  # Adjust the number of points for different accuracy levels