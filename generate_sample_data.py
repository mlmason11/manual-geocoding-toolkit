import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Step 1: Create sample_input.xlsx
df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Site A", "Site B", "Site C"],
    "lat": [None, 40.7128, None],
    "lon": [None, -74.0060, None]
})
df.to_excel("data/sample_input.xlsx", index=False)
print("✅ sample_input.xlsx created")

# Step 2: Generate sample_output.geojson (placeholders for missing rows)
geometry = [
    Point(-74.0050, 40.7100),  # placeholder for Site A
    Point(-74.0060, 40.7128),  # real coord for Site B
    Point(-74.0070, 40.7150)   # placeholder for Site C
]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
gdf.to_file("data/sample_output.geojson", driver="GeoJSON")
print("✅ sample_output.geojson created")

# Step 3: Simulate manual edits → adjusted.geojson
gdf.loc[gdf['id'] == 1, 'geometry'] = gdf.loc[gdf['id'] == 1, 'geometry'].translate(xoff=0.001, yoff=-0.001)
gdf.loc[gdf['id'] == 3, 'geometry'] = gdf.loc[gdf['id'] == 3, 'geometry'].translate(xoff=-0.001, yoff=0.001)
gdf.to_file("data/adjusted.geojson", driver="GeoJSON")
print("✅ adjusted.geojson created")

# Step 4: Sync new lat/lon back to Excel → synced_output.xlsx
gdf['lat'] = gdf.geometry.y
gdf['lon'] = gdf.geometry.x
synced_df = df.copy()
synced_df.set_index('id', inplace=True)
gdf.set_index('id', inplace=True)
synced_df.update(gdf[['lat', 'lon']])
synced_df.reset_index(inplace=True)
synced_df.to_excel("data/synced_output.xlsx", index=False)
print("✅ synced_output.xlsx created")
