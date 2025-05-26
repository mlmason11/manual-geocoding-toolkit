# 📁 Data Folder

This folder contains sample files used in the walkthrough and for testing the toolkit end-to-end.

These files demonstrate the full lifecycle of a dataset as it moves through the Manual Geocoding Toolkit — from raw input to synced output.

---

## 📦 Contents

| File                     | Description                                                    |
|--------------------------|----------------------------------------------------------------|
| `sample_input.xlsx`      | Original spreadsheet with some missing lat/lon values          |
| `sample_output.geojson`  | Placeholder points generated for missing coordinates           |
| `adjusted.geojson`       | Simulated manual edits (as if done in QGIS)                    |
| `synced_output.xlsx`     | Final Excel output with updated lat/lon values inserted        |

---

## 🔁 Workflow Summary

1. **`sample_input.xlsx`** — You start here. Some rows have missing coordinates.
2. **`sample_output.geojson`** — Run `create-placeholders` to generate points.
3. **`adjusted.geojson`** — Edit those points in QGIS and save the result.
4. **`synced_output.xlsx`** — Run `sync-coordinates-cli` to update your table with the new coordinates.

---

## 🧪 Use for Testing or Demo

You can use this folder as a test set or portfolio demo without needing any setup. Just follow the steps in `tutorial/walkthrough.md`.
