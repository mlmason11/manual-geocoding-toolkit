# Contributing to Manual Geocoding Toolkit

Thanks for your interest in contributing!

This project is designed to help GIS analysts manually geocode incomplete datasets using a clean, Python-based workflow. Whether you're fixing bugs, adding features, or improving documentation, we welcome your input.

---

## 🧱 How to Contribute

1. **Fork** this repository
2. **Clone** your fork to your local machine:

   ```bash
   git clone https://github.com/your-username/manual-geocoding-toolkit.git
   ```

3. **Create a new branch** for your feature or fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**, test locally, and commit:

   ```bash
   git commit -m "Add feature: your-feature-name"
   ```

5. **Push to your fork**:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** (PR) from your branch into `main` on this repo.

---

## 🧪 Running Tests

Before submitting a PR, please make sure the test suite passes.

```bash
pytest
```

This ensures your change doesn’t break existing functionality.

---

## 📁 Folder Structure Overview

- `manual_geocoding/`: Main CLI and processing logic
- `tests/`: Unit tests for major functions
- `data/`: Sample files for demoing the workflow
- `tutorial/`: Full walkthrough for end users

---

## ✨ Contributions We Love

- Fixes for bugs or edge cases
- CLI enhancements or usability improvements
- Data validation tools or format converters
- Expanded documentation, walkthroughs, or tutorials

---

## 📜 Code Style

Follow existing formatting and function naming styles. This project uses standard Python 3.10+ conventions.

Optionally, you can use:

```bash
black .
```

to autoformat before committing.

---

## 🤝 Thank You :D

Whether it's a bug report, feature request, or pull request — your contribution means a lot. Together, we’re making geospatial work cleaner and more accessible.
