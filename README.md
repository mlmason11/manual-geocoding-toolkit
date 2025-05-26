# 🗺️ Manual Geocoding Toolkit

A Python-based command-line tool to assist GIS analysts with **manually geocoding datasets** that lack clean or complete coordinate data.

Built for portability and inspired by real-world workflows developed at the **NYC Department of Transportation**, this toolkit streamlines the process of adding, adjusting, and syncing spatial data—without relying on proprietary software like ArcMap.

---

## 🚀 Key Features

- 🔹 Generate placeholder geometry for records with missing coordinates
- 🔹 Use any GIS tool (e.g., QGIS) to manually adjust point locations
- 🔹 Sync updated geometry back into the original spreadsheet
- 🔹 Convert between tabular and spatial formats (Excel, CSV, GeoJSON, Shapefile)
- 🔹 100% Python-based, cross-platform, and ArcPy-free

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/manual-geocoding-toolkit.git
cd manual-geocoding-toolkit
python3 -m venv .venv
source .venv/bin/activate        # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
pip install -e .
