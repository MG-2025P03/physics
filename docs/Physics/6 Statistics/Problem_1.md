## Simulating Sampling Distributions

Step 1: Population Data Generation

Uniform Distribution: Generate a dataset using numpy.random.uniform().
Exponential Distribution: Generate a dataset using numpy.random.exponential().
Binomial Distribution: Generate a dataset using numpy.random.binomial().

For each type of distribution, you should generate a large dataset, say with 100,000 observations, to represent the population.

Python Code Example:

```
python  Copy codeimport numpy as np

# Population sizes
population_size = 100000

# Generate population data

uniform_population = np.random.uniform(low=0.0, high=1.0, size=population_size)
exponential_population = np.random.exponential(scale=1.0, size=population_size)
binomial_population = np.random.binomial(n=10, p=0.5, size=population_size)

2. Sampling and Visualization
Step 2: Sampling and Sample Mean Calculation

For each distribution, perform random sampling for different sample sizes: 5, 10, 30, 50.
Calculate the sample mean for each sample size.
Repeat the sampling process, e.g., 1000 times, to construct the sampling distribution of the sample mean.

Step 3: Plotting Histograms

Create histograms of the sample means for each sample size.
Observe and discuss the convergence to a normal distribution.

Python Code Example:
python  Copy codeimport matplotlib.pyplot as plt

def sampling_distribution(population, sample_size, num_samples=1000):
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size)
        sample_means.append(np.mean(sample))
    return sample_means

# Visualize sampling distributions
sample_sizes = [5, 10, 30, 50]
distributions = {'Uniform': uniform_population, 'Exponential': exponential_population, 'Binomial': binomial_population}

plt.figure(figsize=(14, 10))
for i, (name, population) in enumerate(distributions.items()):
    for j, size in enumerate(sample_sizes):
        plt.subplot(len(distributions), len(sample_sizes), i * len(sample_sizes) + j + 1)
        sample_means = sampling_distribution(population, size)
        plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='b')
        plt.title(f'{name} Dist.\nSample Size={size}')
        plt.xlabel('Sample Mean')
        plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
```

3. Parameter Exploration
Step 4: Analyzing Convergence and Variance

Explore how different sample sizes affect the rate of convergence to normality.
Discuss how the variance of the original population impacts the spread of the sampling distribution.

4. Practical Applications
Step 5: Real-World Relevance

Highlight the importance of the Central Limit Theorem in various fields:
Estimating Population Parameters: Providing more accurate estimates as sample sizes increase.
Quality Control in Manufacturing: Helps in setting standards and controlling product quality by understanding the underlying population variability.
Predicting Outcomes in Financial Models: Facilitates the application of normal distribution assumptions in finance through aggregation.
