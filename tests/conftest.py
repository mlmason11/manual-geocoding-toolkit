import pandas as pd
import pytest

@pytest.fixture
def partial_missing_df():
    return pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['A', 'B', 'C', 'D'],
        'lat': [40.7, None, None, 40.8],
        'lon': [-74.0, None, None, -73.9]
    })

@pytest.fixture
def all_valid_df():
    return pd.DataFrame({
        'id': [1, 2],
        'lat': [40.7, 40.8],
        'lon': [-74.0, -73.9]
    })
