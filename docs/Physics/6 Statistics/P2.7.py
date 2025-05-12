import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_enrollees_vs_graduates(num_simulations: int, graduate_rate: float) -> np.ndarray:
    # Simulate uniformly distributed 2021 enrollees in a unit square
    enrollees_x = np.random.uniform(0, 1, num_simulations)
    enrollees_y = np.random.uniform(0, 1, num_simulations)

    # Calculate a new distribution for 2025 graduates
    graduates_x = enrollees_x  # Assume x-coordinates remain the same for simplicity
    graduates_y = graduate_rate * enrollees_y + np.random.normal(0, 0.1, num_simulations)

    # Plot the simulation results
    plt.figure(figsize=(8, 8))
    plt.scatter(enrollees_x, enrollees_y, color='lightgreen', s=10, alpha=0.5, label='2021 Enrollees')
    plt.scatter(graduates_x, graduates_y, color='orange', s=10, alpha=0.5, edgecolors='red', linewidth=0.5, label='2025 Graduates')
    plt.title("Monte Carlo Simulation: Enrollees vs Graduates")
    plt.xlabel("Normalized Enrollee ID")
    plt.ylabel("Normalized Enrollment Level / Graduation Level")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.show()

    return (enrollees_x, enrollees_y), (graduates_x, graduates_y)

# Run the simulation with a specified number of simulations and graduate rate
enrollees, graduates = monte_carlo_enrollees_vs_graduates(num_simulations=10000, graduate_rate=0.8)