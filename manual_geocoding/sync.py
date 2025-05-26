import pandas as pd
import geopandas as gpd

def sync_coordinates(edited_gdf: gpd.GeoDataFrame, original_df: pd.DataFrame, id_column='id') -> pd.DataFrame:
    edited_df = edited_gdf.copy()
    edited_df['lat'] = edited_df.geometry.y
    edited_df['lon'] = edited_df.geometry.x

    merged = original_df.set_index(id_column).copy()
    merged.update(edited_df.set_index(id_column)[['lat', 'lon']])
    return merged.reset_index()
