import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Set file path
file_path = "https://mg-2025p03.github.io/physics/_pics/pl_shp.zip"

# Read specific layer
poland_gdf = gpd.read_file(file_path, layer='pl')

# Correct encoding of region names
poland_gdf['name'] = poland_gdf['name'].apply(lambda x: x.encode('latin1').decode('utf-8'))

# Print names for verification to ensure correct extraction process
print("Regions from GeoDataFrame:", poland_gdf['name'].unique())

# Verify the exact match for filtering
target_region_name = 'Masovian'

# Filter GeoDataFrame to retain only the Masovian region
masovian_gdf = poland_gdf[poland_gdf['name'] == target_region_name]

# Ensure the filtering has succeeded
print("Filtered GeoDataFrame:", masovian_gdf)

# Handle empty DataFrame scenario
if masovian_gdf.empty:
    raise ValueError(f"No data found for the region: {target_region_name}")

# Reproject to a suitable CRS for Poland (EPSG:2180)
masovian_gdf = masovian_gdf.to_crs(epsg=2180)

# Current population for Masovian region
current_population_masovian = 5421823

# Simulation setup for Masovian region
years = 2050 - 2022
iterations = 1000
growth_rate_mean = 0.005
growth_rate_std = 0.004

# Monte Carlo simulation for Masovian
projection_results_masovian = []

for _ in range(iterations):
    population = current_population_masovian
    for year in range(years):
        growth_rate = np.random.normal(growth_rate_mean, growth_rate_std)
        population += population * growth_rate
    projection_results_masovian.append(population)

# Calculate the mean of the simulated values for the 2026 population
mean_projected_population_2026 = np.mean(projection_results_masovian)

# Update the Masovian GeoDataFrame with the projected population
masovian_gdf['projected_population_2026'] = mean_projected_population_2026

# Plotting the results
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
masovian_gdf.boundary.plot(ax=ax, linewidth=1, color="black")
cax = masovian_gdf.plot(ax=ax, column='projected_population_2026', cmap='YlOrRd', legend=False, alpha=0.75)
ax.set_title("Projected Population in 2050 for the Masovian Region (Monte Carlo)")
ax.axis('off')

# Add colorbar correctly
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=masovian_gdf['projected_population_2026'].min(), vmax=masovian_gdf['projected_population_2026'].max()))
sm._A = []  # Dummy for colorbar creation
cbar = fig.colorbar(sm, ax=ax, format=FuncFormatter(lambda x, pos: f'{x/1e6:.1f}M'))
cbar.set_label('Population (Millions)')

# Add region name
for x, y, label in zip(masovian_gdf.geometry.centroid.x, masovian_gdf.geometry.centroid.y, masovian_gdf['name']):
    ax.text(x, y, label, fontsize=10, ha='center', va='center', color='black', alpha=0.6)

plt.show()