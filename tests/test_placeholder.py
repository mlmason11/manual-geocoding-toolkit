import geopandas as gpd
from manual_geocoding.placeholder import generate_placeholders

def test_generate_placeholders_partial(partial_missing_df):
    origin = (40.75, -73.95)
    gdf = generate_placeholders(partial_missing_df, origin)

    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 4
    assert gdf.geometry.notnull().all()
    assert gdf.loc[1, 'geometry'] != gdf.loc[0, 'geometry']

def test_generate_placeholders_all_valid(all_valid_df):
    origin = (40.75, -73.95)
    gdf = generate_placeholders(all_valid_df, origin)

    assert gdf.loc[0, 'geometry'].x == -74.0
    assert gdf.loc[1, 'geometry'].y == 40.8
