import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_points: int) -> float:
    x_points = np.random.uniform(0, 1, num_points)
    y_points = np.random.uniform(0, 1, num_points)
    inside_circle = x_points**2 + y_points**2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_points
    return pi_estimate

# Define the range of point numbers to test
points_list = [10, 100, 1000, 10000, 100000, 1000000]

# Store the estimates and deviations
pi_estimates = []
deviations = []

# Run the simulation for each number of points
for num_points in points_list:
    pi_estimate = monte_carlo_pi(num_points)
    pi_estimates.append(pi_estimate)
    deviations.append(abs(pi_estimate - np.pi))

# Plotting the results
plt.figure(figsize=(12, 6))

# Subplot 1: Estimated π vs. Number of Points
plt.subplot(1, 2, 1)
plt.plot(points_list, pi_estimates, marker='o', linestyle='-')
plt.axhline(y=np.pi, color='r', linestyle='--', label='True π')
plt.xscale('log')
plt.title('Estimated π vs. Number of Points')
plt.xlabel('Number of Points (log scale)')
plt.ylabel('Estimated π')
plt.legend()
plt.grid(True)

# Subplot 2: Error in Estimate vs. Number of Points
plt.subplot(1, 2, 2)
plt.plot(points_list, deviations, marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('log')
plt.title('Error in Estimate vs. Number of Points')
plt.xlabel('Number of Points (log scale)')
plt.ylabel('Error in Estimate')
plt.grid(True)

plt.tight_layout()
plt.show()