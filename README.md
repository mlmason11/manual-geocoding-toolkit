# 🗺️ Manual Geocoding Toolkit

A Python-based command-line tool to assist GIS analysts with **manually geocoding datasets** that lack clean or complete coordinate data.

Built for portability and inspired by real-world workflows developed at the **NYC Department of Transportation**, this toolkit streamlines the process of adding, adjusting, and syncing spatial data—without relying on proprietary software like ArcMap.

![Build](https://github.com/mlmason11/manual-geocoding-toolkit/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/github/license/mlmason11/manual-geocoding-toolkit)

---

## 📚 Table of Contents

- [Key Features](#key-features)
- [Installation](#installation)
- [CLI Usage](#cli-usage)
- [Folder Structure](#folder-structure)
- [Testing](#testing)
- [Walkthrough](#walkthrough)
- [Why This Exists](#why-this-exists)
- [License](#license)
- [Contributions](#contributions)

---

## Key Features

- Generate placeholder geometry for records with missing coordinates
- Manually adjust geometry in QGIS or any GIS editor
- Sync updated geometry back into Excel or CSV
- Convert between tabular and spatial formats
- Lightweight, cross-platform, and ArcPy-free

---

## Installation

```bash
git clone https://github.com/mlmason11/manual-geocoding-toolkit.git
cd manual-geocoding-toolkit
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
pip install -e .
```

---

## CLI Usage

```bash
manual-geocoding --help
```

### Create Placeholder Geometry

```bash
manual-geocoding create-placeholders data/sample_input.xlsx --origin "40.7128,-74.0060" --output data/sample_output.geojson
```

### Sync Adjusted Geometry Back to Table

```bash
manual-geocoding sync-coordinates-cli data/adjusted.geojson data/sample_input.xlsx --output data/synced_output.xlsx
```

---

## Folder Structure

```text
manual_geocoding/     # Core logic and CLI
tests/                # Unit tests
data/                 # Sample files for demo and testing
tutorial/             # Full walkthrough and screenshots
```

---

## Testing

To run tests locally:

```bash
pytest
```

Test coverage includes:

- Placeholder generation logic
- Coordinate syncing
- Partial and complete datasets

---

## Walkthrough

A full tutorial is available in [`tutorial/walkthrough.md`](tutorial/walkthrough.md), including:

- Sample input and outputs
- Editing with QGIS
- Syncing back to Excel

---

## Why This Exists

This toolkit was designed in response to a real-world problem: spatial datasets without complete coordinate data. It allows GIS professionals to work manually where needed, and push updated geometry back into their source data without losing structure or precision.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contributions

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.

Pull requests are welcome!
