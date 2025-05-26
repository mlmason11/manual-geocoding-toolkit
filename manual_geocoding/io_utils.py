import pandas as pd
import geopandas as gpd

def read_table(filepath: str) -> pd.DataFrame:
    if filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    elif filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format")

def write_table(df: pd.DataFrame, filepath: str):
    if filepath.endswith('.xlsx'):
        df.to_excel(filepath, index=False)
    elif filepath.endswith('.csv'):
        df.to_csv(filepath, index=False)
    else:
        raise ValueError("Unsupported file format")

def write_spatial(gdf: gpd.GeoDataFrame, filepath: str):
    if filepath.endswith('.geojson'):
        gdf.to_file(filepath, driver='GeoJSON')
    elif filepath.endswith('.shp'):
        gdf.to_file(filepath)
    else:
        raise ValueError("Unsupported spatial file format")

def read_spatial(filepath: str) -> gpd.GeoDataFrame:
    return gpd.read_file(filepath)
