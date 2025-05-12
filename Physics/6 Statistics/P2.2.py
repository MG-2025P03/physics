import numpy as np
import matplotlib.pyplot as plt

def simulate_ai_technologies_vs_graduates(num_simulations: int, factor: int) -> np.ndarray:
    # Simulate IT graduates data
    it_graduates = np.random.normal(loc=1000, scale=50, size=num_simulations)  # Mean of 1000, SD of 50
    
    # Simulate AI technologies as a function of graduates with noise
    ai_technologies = factor * (0.02 * it_graduates + np.random.normal(0, 5, num_simulations))
    
    return it_graduates, ai_technologies

# Number of simulations
num_simulations = 1000
scaling_factor = 100  # Factor to adjust influence

# Run the simulation
graduates, ai_technologies = simulate_ai_technologies_vs_graduates(num_simulations, scaling_factor)

# Plot the simulation results
plt.figure(figsize=(12, 6))
plt.scatter(graduates, ai_technologies, alpha=0.6, color='gold', edgecolors='red')
plt.title("Monte Carlo Simulation: AI Technologies vs IT Graduates")
plt.xlabel("Number of IT Graduates")
plt.ylabel("Number of AI Technologies")
plt.grid(True)
plt.show()