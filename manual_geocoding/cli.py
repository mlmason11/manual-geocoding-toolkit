import typer
from manual_geocoding.io_utils import read_table, write_table, write_spatial, read_spatial
from manual_geocoding.placeholder import generate_placeholders
from manual_geocoding.sync import sync_coordinates

app = typer.Typer()

@app.command()
def create_placeholders(input_file: str, origin: str, output_file: str, spacing: float = 0.001):
    lat, lon = map(float, origin.split(","))
    df = read_table(input_file)
    gdf = generate_placeholders(df, (lon, lat), spacing=spacing)
    write_spatial(gdf, output_file)
    print(f"Generated {len(gdf)} features and saved to {output_file}")

@app.command()
def sync_coordinates_cli(edited_file: str, original_file: str, output_file: str, id_column: str = 'id'):
    edited_gdf = read_spatial(edited_file)
    original_df = read_table(original_file)
    updated_df = sync_coordinates(edited_gdf, original_df, id_column=id_column)
    write_table(updated_df, output_file)
    print(f"Updated coordinates written to {output_file}")

if __name__ == "__main__":
    app()
