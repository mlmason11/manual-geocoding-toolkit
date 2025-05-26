import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from manual_geocoding.utils import is_valid_coord, generate_grid_points
from manual_geocoding.config import DEFAULT_SPACING, DEFAULT_CRS

def generate_placeholders(df: pd.DataFrame, origin: tuple, method='grid', spacing=DEFAULT_SPACING) -> gpd.GeoDataFrame:
    df = df.copy()
    missing_mask = ~(df.apply(lambda row: is_valid_coord(row.get('lat'), row.get('lon')), axis=1))

    if missing_mask.sum() == 0:
        print("All rows contain valid coordinates. No placeholders needed.")
        return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['lon'], df['lat']), crs=DEFAULT_CRS)

    print(f"{missing_mask.sum()} rows missing coordinates. Generating placeholders...")

    placeholder_coords = generate_grid_points(origin, missing_mask.sum(), spacing)
    geometry = []

    idx = 0
    for i, row in df.iterrows():
        if is_valid_coord(row.get('lat'), row.get('lon')):
            point = Point(float(row['lon']), float(row['lat']))
        else:
            point = Point(placeholder_coords[idx])
            idx += 1
        geometry.append(point)

    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs=DEFAULT_CRS)
    return gdf
