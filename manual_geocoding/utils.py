import pandas as pd
import math

def is_valid_coord(lat, lon) -> bool:
    try:
        return (
            lat is not None and lon is not None and
            not pd.isna(lat) and not pd.isna(lon) and
            -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180
        )
    except Exception:
        return False

def generate_grid_points(origin, n_points, spacing):
    ox, oy = origin
    rows = cols = math.ceil(n_points ** 0.5)
    coords = []
    for i in range(rows):
        for j in range(cols):
            if len(coords) >= n_points:
                break
            x = ox + (j - cols // 2) * spacing
            y = oy + (i - rows // 2) * spacing
            coords.append((x, y))
    return coords
