# Codes used

### Simulating Sampling Distributions

<details>
<summary> <- Click to view the codes</summary>

```
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Function to create sampling distributions and plot histograms
def plot_sampling_distribution(sample_size):
    # Sampling function
    def sampling_distribution(population, sample_size, num_samples=1000):
        sample_means = []
        for _ in range(num_samples):
            sample = np.random.choice(population, size=sample_size)
            sample_means.append(np.mean(sample))
        return sample_means

    plt.figure(figsize=(18, 6))

    distributions = {
        'Uniform': uniform_population,
        'Exponential': exponential_population,
        'Binomial': binomial_population
    }

    for i, (name, population) in enumerate(distributions.items()):
        # Calculate sample means
        sample_means = sampling_distribution(population, sample_size)

        # Plot histogram
        plt.subplot(1, 3, i + 1)
        plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='b', edgecolor='black')
        plt.title(f'{name} Distribution\nSample Size = {sample_size}')
        plt.xlabel('Sample Mean')
        plt.ylabel('Frequency')

        # Calculate and display variance
        variance = np.var(sample_means)
        plt.annotate(f'Variance: {variance:.4f}', xy=(0.7, 0.7), xycoords='axes fraction')

    plt.tight_layout()
    plt.show()

# Generate populations
population_size = 100000
uniform_population = np.random.uniform(low=0.0, high=1.0, size=population_size)
exponential_population = np.random.exponential(scale=1.0, size=population_size)
binomial_population = np.random.binomial(n=10, p=0.5, size=population_size)

# Create an interactive widget
sample_size_slider = widgets.IntSlider(
    value=5,
    min=5,
    max=50,
    step=5,
    description='Sample Size:',
    continuous_update=False,
)

# Display interactive plot
interactive_plot = widgets.interactive(plot_sampling_distribution, sample_size=sample_size_slider)
display(interactive_plot)
```
</details>

### Monte Carlo Simulation - Estimating Pi

<details>
<summary> <- Click to view the codes</summary>

```
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
```

</details>

### Buffon's Needle Example

<details>
<summary> <- Click to view the codes</summary>

```
import numpy as np
import matplotlib.pyplot as plt

# Set parameters
L = 1.0  # Length of the needle
D = 1.0  # Distance between the parallel lines
n = 10  # Number of needle drops

# Initialize count of crossings
crossings = 0

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 4)  # X-axis limits
ax.set_ylim(0, 4)  # Y-axis limits
ax.set_xticks(np.arange(0, 5, 1))
ax.set_yticks(np.arange(0, 5, 1))
ax.set_aspect('equal', adjustable='box')

# Draw parallel lines
for i in np.arange(0, 4, D):
    ax.axhline(y=i, color='black', linewidth=1)

# Simulate needle drops
for _ in range(n):
    # Randomly choose midpoint and angle
    midpoint_x = np.random.uniform(0, 4)
    midpoint_y = np.random.uniform(0, 4)
    angle = np.random.uniform(0, np.pi)

    # Calculate the endpoints of the needle
    dx = (L / 2) * np.cos(angle)
    dy = (L / 2) * np.sin(angle)
    x_start = midpoint_x - dx
    x_end = midpoint_x + dx
    y_start = midpoint_y - dy
    y_end = midpoint_y + dy
    
    # Check if the needle crosses a line
    if (y_start // D) != (y_end // D):
        crossings += 1
        color = 'red'  # Crossing needle in red
    else:
        color = 'blue'  # Non-crossing needle in blue

    # Draw the needle
    ax.plot([x_start, x_end], [y_start, y_end], color=color, linewidth=2)

# Estimate pi
pi_estimate = (2 * L * n) / (crossings * D)
print(f"Estimated value of pi: {pi_estimate:.4f}")

# Add title and labels
ax.set_title(f"Buffon's Needle Simulation\nEstimated value of π: {pi_estimate:.4f}")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Show the plot
plt.show()
```

</details>