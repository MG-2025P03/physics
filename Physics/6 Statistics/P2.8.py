import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point

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

# Define the population distribution for each specific age between 13 and 18
# Assuming equal distribution for simplification; these should be adjusted with real data if available
age_distribution_percentages = {
    13: 0.0167 * 4,  # ~1.67%
    14: 0.0167 / 4,
    15: 0.0167 * 3,
    16: 0.0167 / 3,
    17: 0.0167 * 2,
    18: 0.0167 / 2
}

# Total population for ages 13-18
current_population_masovian = 5421823
population_ages_13_to_18 = current_population_masovian * sum(age_distribution_percentages.values())  # Adjust to total percentage if needed

# Simulate data points for each individual age in the Masovian region
ages = list(age_distribution_percentages.keys())
points_by_age = {age: [] for age in ages}
num_simulations = 1000  # Total number of points to simulate across these ages
minx, miny, maxx, maxy = masovian_gdf.total_bounds

# Generate random points within the region for each age
for age in ages:
    num_points = int(num_simulations * age_distribution_percentages[age])  # Proportional split
    # Print regions with NaN values
    print("Age Population Probability", age, ":", f'{(((age_distribution_percentages[age] * current_population_masovian) / population_ages_13_to_18) * 100):.2f}')
    for _ in range(num_points):
        while True:
            x = np.random.uniform(minx, maxx)
            y = np.random.uniform(miny, maxy)
            point = Point(x, y)
            if point.within(masovian_gdf.geometry.iloc[0]):
                points_by_age[age].append(point)
                break

# Plot points within the Masovian region, differentiating by age
fig, ax = plt.subplots(1, 1, figsize=(12, 10))
masovian_gdf.boundary.plot(ax=ax, color='black', linewidth=0.8)



# Colors and labels for plotting different ages
colors = ['red', 'green', 'blue', 'purple', 'cyan', 'orange']
for age, color in zip(ages, colors):
    # Create a GeoDataFrame for these points
    points_gdf = gpd.GeoDataFrame(geometry=points_by_age[age], crs=masovian_gdf.crs)
    points_gdf.plot(ax=ax, color=color, marker='o', markersize=5, alpha=0.7, label=f'Age {age}')

ax.set_title(" Simulated Distribution of Ages 13-18 in Masovian Region")
ax.axis('off')
ax.legend(loc='upper right')

plt.show()