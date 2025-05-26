# 📘 Manual Geocoding Toolkit – Full Walkthrough

This tutorial provides an end-to-end guide for using the Manual Geocoding Toolkit to clean, complete, and update spatial datasets that lack reliable coordinate data.

Whether you're dealing with field-collected information, historic records, or incomplete spreadsheets, this toolkit helps you:

✅ Identify missing geometry
✅ Generate placeholder points for editing
✅ Refine them in a GIS editor like QGIS
✅ Sync new coordinates back into the original spreadsheet

This project was inspired by real data challenges faced during my work with the NYC Department of Transportation, where spatial records were frequently incomplete or inconsistent.

---

## ✨ What Makes This Toolkit Different?

- 100% Python-based and cross-platform
- CLI-driven and scriptable
- ArcMap-agnostic: works without any ESRI tools
- Designed with public-sector workflows in mind
- Built to be extensible and understandable

---

## 🧭 What This Tutorial Covers

- Project setup & dependencies
- Understanding the input data structure
- Generating placeholder geometry
- Editing features manually in QGIS
- Syncing the updated geometry back into a spreadsheet
- Running tests and modifying the toolkit

---

## ⚙️ 2. Project Setup

Follow these steps to get started on any Mac, Linux, or Windows machine.

### 📁 Step 1: Clone the Project

```bash
git clone https://github.com/yourusername/manual-geocoding-toolkit.git
cd manual-geocoding-toolkit
```

### 🧪 Step 2: Create a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all necessary packages like `pandas`, `geopandas`, `shapely`, `pyproj`, and `typer`.

### ⚙️ Step 4: Install the CLI Tool Locally

```bash
pip install -e .
```

This installs the `manual-geocoding` CLI so you can run commands like:

```bash
manual-geocoding --help
```

You should now see a list of available subcommands:

- `create-placeholders`
- `sync-coordinates-cli`

### 🧪 Optional: Run Tests

Make sure everything is working by running:

```bash
pytest
```

You should see all tests pass. This confirms your environment is correctly set up.

---

## 📊 3. Understanding the Input Data

To use the toolkit, your input spreadsheet (Excel or CSV) should include:

- A column named `id` (unique identifier for each record)
- Optional `lat` and `lon` columns

Example:

| id | name     | lat     | lon      |
|----|----------|---------|----------|
| 1  | Site A   |         |          |
| 2  | Site B   | 40.7128 | -74.0060 |
| 3  | Site C   |         |          |

This allows the tool to:

- Detect rows missing coordinates
- Leave existing coordinates untouched
- Link edited geometry back to the source row using `id`

If you don't have a `lat`/`lon` column at all, the tool will still work — it will just treat all rows as missing geometry.

---

## 🧱 4. Creating Placeholder Geometry

Placeholder points are generated when coordinates are missing.
You define an `origin` (starting point) and the CLI places the points in a grid layout by default.

### Example Command

```bash
manual-geocoding create-placeholders data/sample_input.xlsx --origin "40.7128,-74.0060" --output data/sample_output.geojson
```

This will:

- Use `40.7128,-74.0060` as the center for generating a grid of points
- Add placeholder geometry only for rows missing lat/lon
- Output a `.geojson` file ready for editing in QGIS

🧠 Tip: The `spacing` parameter (in degrees) controls the distance between points.

---

## 🖱️ 5. Editing Placeholder Points in QGIS

Once you've generated `sample_output.geojson`, open it in QGIS to manually edit the placeholder points.

### Steps in QGIS

1. Open QGIS
2. Drag in `sample_output.geojson`
3. Toggle **Editing Mode** (pencil icon)
4. Select and drag the placeholder points to their correct positions
5. Click **Save Edits**
6. Export the layer to a new file, e.g. `adjusted.geojson`

🎯 Make sure to preserve the `id` column — it's how your edits are matched back to the table.

You can optionally load a basemap or satellite imagery for more precise placement.

---

## 🔁 6. Syncing Geometry Back to Spreadsheet

After manually editing and saving your GeoJSON, use the following command:

```bash
manual-geocoding sync-coordinates-cli data/adjusted.geojson data/sample_input.xlsx --output data/synced_output.xlsx
```

This will:

- Extract updated coordinates from the geometry field
- Match each feature by its `id`
- Insert the new `lat` and `lon` values into the original table

### Example Output

| id | name     | lat     | lon      |
|----|----------|---------|----------|
| 1  | Site A   | 40.7000 | -74.0100 |
| 2  | Site B   | 40.7128 | -74.0060 |
| 3  | Site C   | 40.7050 | -74.0020 |

You've now gone from a partially missing dataset → to clean, editable geometry → to fully updated spreadsheet.
