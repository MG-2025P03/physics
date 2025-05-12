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