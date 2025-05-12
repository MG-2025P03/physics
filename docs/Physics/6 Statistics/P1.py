import numpy as np
import matplotlib.pyplot as plt

# Define population size
population_size = 100000

# Generate populations
uniform_population = np.random.uniform(low=0.0, high=1.0, size=population_size)
exponential_population = np.random.exponential(scale=1.0, size=population_size)
binomial_population = np.random.binomial(n=10, p=0.5, size=population_size)

# Plotting the distributions
plt.figure(figsize=(18, 6))

# Uniform Distribution
plt.subplot(1, 3, 1)
plt.hist(uniform_population, bins=50, color='blue', alpha=0.7, edgecolor='black')
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Exponential Distribution
plt.subplot(1, 3, 2)
plt.hist(exponential_population, bins=50, color='green', alpha=0.7, edgecolor='black')
plt.title('Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Binomial Distribution
plt.subplot(1, 3, 3)
plt.hist(binomial_population, bins=max(binomial_population) - min(binomial_population) + 1, color='red', alpha=0.7, edgecolor='black')
plt.title('Binomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Adjust layout and show plot
plt.tight_layout()
plt.show()