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