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