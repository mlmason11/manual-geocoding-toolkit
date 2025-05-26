from setuptools import setup, find_packages

setup(
    name="manual-geocoding-toolkit",
    version="0.1.0",
    description="A Python toolkit for manually geocoding incomplete spatial data",
    author="Max Mason",
    author_email="mlmason11@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "geopandas",
        "shapely",
        "openpyxl",
        "pyproj",
        "typer[all]"
    ],
    entry_points={
        "console_scripts": [
            "manual-geocoding=manual_geocoding.cli:app"
        ]
    },
    python_requires=">=3.10",
)
