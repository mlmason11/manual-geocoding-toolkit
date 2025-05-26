import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from manual_geocoding.sync import sync_coordinates

def test_sync_coordinates_updates_missing_values():
    original_df = pd.DataFrame({
        'id': [1, 2],
        'lat': [None, 40.8],
        'lon': [None, -73.9]
    })

    edited_gdf = gpd.GeoDataFrame({
        'id': [1, 2],
        'geometry': [Point(-74.0, 40.7), Point(-73.9, 40.8)]
    }, crs="EPSG:4326")

    synced_df = sync_coordinates(edited_gdf, original_df, id_column='id')

    assert round(synced_df.loc[0, 'lat'], 4) == 40.7
    assert round(synced_df.loc[0, 'lon'], 4) == -74.0
