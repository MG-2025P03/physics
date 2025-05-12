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

# Calculate the mean projected population for each age group
mean_projected_population_by_age_group = {
    age: current_population_masovian * percentage
    for age, percentage in age_distribution_percentages.items()
}

# Generate sub-regions within Masovian based on these percentages
total_area = masovian_gdf.geometry.area.iloc[0]
age_areas = {age: total_area * percentage for age, percentage in age_distribution_percentages.items()}

# Fake distribution of areas within the single region (this example divides it approximately)
original_geom = masovian_gdf.geometry.iloc[0]
minx, miny, maxx, maxy = original_geom.bounds

# Divide the region vertically into polygons by percentage
current_minx = minx
age_geometries = []
for age, area in age_areas.items():
    age_width = (area / total_area) * (maxx - minx)
    geom_slice = original_geom.intersection(Polygon([(current_minx, miny), 
                                                     (current_minx + age_width, miny), 
                                                     (current_minx + age_width, maxy), 
                                                     (current_minx, maxy)]))
    age_geometries.append((age, geom_slice))
    current_minx += age_width

# Create a new GeoDataFrame for these fake areas
age_gdf = gpd.GeoDataFrame({
    'age_group': [age for age, geom in age_geometries],
    'geometry': [geom for age, geom in age_geometries],
    'percentage': [age_distribution_percentages[age] * 100 for age, geom in age_geometries],
    'population_millions': [mean_projected_population_by_age_group[age] / 1e6 for age, geom in age_geometries]
}, crs=masovian_gdf.crs)

# Plot the Masovian region with age group areas
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
age_gdf.boundary.plot(ax=ax, color='black', linewidth=0.8)
age_gdf.plot(ax=ax, column='age_group', cmap='Accent', legend=True, edgecolor='black', alpha=0.75)

ax.set_title("Approximate (2025) Population based on Age Group in Masovian Region")
ax.axis('off')

# Annotate the areas with age group names, percentages, and population in millions
for x, y, label, perc, pop in zip(age_gdf.geometry.centroid.x, age_gdf.geometry.centroid.y, age_gdf['age_group'],
                                  age_gdf['percentage'], age_gdf['population_millions']):
    ax.text(x, y, f"{label}\n{perc:.1f}%\n{pop:.2f}M", fontsize=10, ha='center', va='center', color='black', alpha=0.7)

plt.show()