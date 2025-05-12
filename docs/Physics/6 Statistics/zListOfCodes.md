#3. List of Codes

### Sampling - 5/10/20/30/50

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

### Estimating Pi

````
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
````

### [2021 Enrollees vs 2026 Graduates (Approx)

````
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
````

### 2050 Poland Population by Region (Forecast)

````
ximport geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

# Setting file path
file_path = "https://mg-2025p03.github.io/physics/_pics/pl_shp.zip"

# Reading specific layer
poland_gdf = gpd.read_file(file_path, layer='pl')

# Correct encoding of region names and verification
poland_gdf['name'] = poland_gdf['name'].apply(lambda x: x.encode('latin1').decode('utf-8'))

# Print to verify names from GeoDataFrame
print("Regions from GeoDataFrame:")
print(poland_gdf['name'].unique())

# Reproject to a suitable CRS for Poland (EPSG:2180)
poland_gdf = poland_gdf.to_crs(epsg=2180)

# Define current population data dictionary 
current_population_2022 = {
    'Lower Silesian': 2904457,
    'Kuyavian-Pomeranian': 2083563,
    'Lublin': 2119854,
    'Lubusz': 1005630,
    'Łódź': 2436348, 
    'Lesser Poland': 3360428,
    'Masovian': 5421823,
    'Opole': 982249,
    'Subcarpathian': 2128203,
    'Podlachian': 1188866,
    'Pomeranian': 2329218,
    'Silesian': 4455701,
    'Świętokrzyskie': 1216949, 
    'Warmian-Masurian': 1423965,
    'Greater Poland': 3475329,
    'West Pomeranian': 1687128
}

# Define mapping for names
name_map = {
    'Dolnośląskie': 'Lower Silesian',
    'Kujawsko-Pomorskie': 'Kuyavian-Pomeranian',
    'Lubelskie': 'Lublin',
    'Lubuskie': 'Lubusz',
    'Łódzkie': 'Łódź',
    'Małopolskie': 'Lesser Poland',
    'Mazowieckie': 'Masovian',
    'Opolskie': 'Opole',
    'Podkarpackie': 'Subcarpathian',
    'Podlaskie': 'Podlachian',
    'Pomorskie': 'Pomeranian',
    'Śląskie': 'Silesian',
    'Świętokrzyskie': 'Świętokrzyskie',
    'Warmińsko-Mazurskie': 'Warmian-Masurian',
    'Wielkopolskie': 'Greater Poland',
    'Zachodniopomorskie': 'West Pomeranian'
}

# Simulation setup
years = 2050 - 2022
iterations = 1000

growth_rate_mean = 0.005
growth_rate_std = 0.004

# Monte Carlo simulation
projection_results = {region: [] for region in current_population_2022.keys()}

for region, initial_population in current_population_2022.items():
    for _ in range(iterations):
        population = initial_population
        for year in range(years):
            growth_rate = np.random.normal(growth_rate_mean, growth_rate_std)
            growth_rate = 1 if growth_rate == 0 else growth_rate
            population += population * growth_rate
        projection_results[region].append(population)

# Function to map population using updated methodology
def map_population(region_name):
    simulation_name = region_name
    if simulation_name is not None:
        return np.mean(projection_results[simulation_name])
    else:
        return np.nan

# Population projection
poland_gdf['projected_population_2050'] = poland_gdf['name'].apply(map_population)

# Print regions with NaN values
print("Regions with NaN values after mapping:")
print(poland_gdf[poland_gdf['projected_population_2050'].isna()]['name'])

# Plotting the results
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
poland_gdf.boundary.plot(ax=ax, linewidth=1)
poland_gdf.plot(ax=ax, column='projected_population_2050', cmap='YlOrRd', legend=True)
ax.set_title("Projected Population in 2050 in Poland by Region (Monte Carlo)")
ax.axis('off')

# Add region names
for x, y, label in zip(poland_gdf.geometry.centroid.x, poland_gdf.geometry.centroid.y, poland_gdf['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='black', alpha=0.6)

plt.show()
````

### 2026 Masovian Region Population by Age group (Forecast)

````
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Set file path for the shapefile
file_path = "https://mg-2025p03.github.io/physics/_pics/pl_shp.zip"

# Read specific layer
poland_gdf = gpd.read_file(file_path, layer='pl')

# Correct encoding of region names
poland_gdf['name'] = poland_gdf['name'].apply(lambda x: x.encode('latin1').decode('utf-8'))

# Filter GeoDataFrame to retain only the Masovian region
masovian_gdf = poland_gdf[poland_gdf['name'] == 'Masovian']

# Reproject to a suitable CRS for Poland (EPSG:2180)
masovian_gdf = masovian_gdf.to_crs(epsg=2180)

# Current population for Masovian region
current_population_masovian = 5421823

# Hypothetical age distribution percentages for the Masovian population
age_distribution_percentages = {
    '1-12': 0.15,   # 15%
    '13-18': 0.10,  # 10%
    '19-35': 0.30,  # 30%
    '36-50': 0.25,  # 25%
    '>50': 0.20     # 20%
}

# Calculate initial population by age group
initial_age_group_populations = {
    group: current_population_masovian * percentage
    for group, percentage in age_distribution_percentages.items()
}

# Simulation setup for Masovian region
years = 2026 - 2022
iterations = 100
growth_rate_mean = 0.005
growth_rate_std = 0.004

# Monte Carlo simulation for each age group
projection_results_by_age_group = {group: [] for group in initial_age_group_populations}

for group, initial_population in initial_age_group_populations.items():
    for _ in range(iterations):
        population = initial_population
        for year in range(years):
            growth_rate = np.random.normal(growth_rate_mean, growth_rate_std)
            population += population * growth_rate
        projection_results_by_age_group[group].append(population)

# Calculate the mean of the simulated values for 2026 population for each age group
mean_projected_population_by_age_group = {
    group: np.mean(populations)
    for group, populations in projection_results_by_age_group.items()
}

# Calculate the distribution of areas based on the simulated projected populations
total_simulated_population = sum(mean_projected_population_by_age_group.values())
age_areas = {group: total_simulated_population * age_distribution_percentages[group]
             for group in mean_projected_population_by_age_group}

# Generate sub-regions within Masovian based on these simulated projections
total_area = masovian_gdf.geometry.area.iloc[0]
original_geom = masovian_gdf.geometry.iloc[0]
minx, miny, maxx, maxy = original_geom.bounds

# Divide the region into vertical strips representing areas for different age groups
current_minx = minx
age_geometries = []
for age, volume in age_areas.items():
    age_width = (volume / total_simulated_population) * (maxx - minx)
    geom_slice = original_geom.intersection(Polygon([(current_minx, miny),
                                                     (current_minx + age_width, miny),
                                                     (current_minx + age_width, maxy),
                                                     (current_minx, maxy)]))
    age_geometries.append((age, geom_slice))
    current_minx += age_width

# Create a new GeoDataFrame for these simulated areas with projected populations
age_gdf = gpd.GeoDataFrame({
    'age_group': [age for age, geom in age_geometries],
    'geometry': [geom for age, geom in age_geometries],
    'population_millions': [mean_projected_population_by_age_group[age] / 1e6 for age, geom in age_geometries],
    'percentage': [age_distribution_percentages[age] * 100 for age, geom in age_geometries]
}, crs=masovian_gdf.crs)

# Plot the Masovian region with age group areas based on Monte Carlo projections
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
age_gdf.boundary.plot(ax=ax, color='black', linewidth=0.8)
age_gdf.plot(ax=ax, column='age_group', cmap='Accent', legend=True, edgecolor='black', alpha=0.75)

ax.set_title("Projected Age Group Areas in Masovian Region (Monte Carlo Simulation)")
ax.axis('off')

# Annotate the areas with age group names, percentages, and population in millions
for x, y, label, perc, pop in zip(age_gdf.geometry.centroid.x, age_gdf.geometry.centroid.y, age_gdf['age_group'],
                                  age_gdf['percentage'], age_gdf['population_millions']):
    ax.text(x, y, f"{label}\n{perc:.1f}%\n{pop:.2f}M", fontsize=10, ha='center', va='center', color='black', alpha=0.7)

plt.show()
````