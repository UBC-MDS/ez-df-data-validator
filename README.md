# ez-df-data-validator

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/ez-df-data-validator.svg)](https://pypi.org/project/ez-df-data-validator/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/ez-df-data-validator.svg)](https://pypi.org/project/ez-df-data-validator/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |


## Summary

ez-df-data-validator is a project that provides basic, but essential data cleaning functionality for ML workflows.
This package provides a lightweight and user friendly toolkit for common data cleaning tasks in Python. It is designed to streamline data preprocessing by offering clear, reusable functions for detecting duplicates, standardizing column names, and handling missing values. The goal is to reduce repetitive code and make data preparation more efficient and reproducible.

## Installation

You can install this package into your preferred Python environment using pip:

```bash
pip install ez-df-data-validator
```

### Example usage

```python
import pandas as pd
from ez_df_data_validator import standardize_headers, missing_summary

# Example dataset
df = pd.DataFrame({
    "Age ": [25, None, 30],
    "Income($)": [50000, 60000, None]
})

# Clean column names
df = standardize_headers(df)

# Summarize missing values
summary = missing_summary(df)

print(summary)
```


### For development

```bash
git clone https://github.com/UBC-MDS/ez-df-data-validator.git
cd ez-df-data-validator
pip install -e .
pip install -e .[tests,dev]
```

**Requirements**
- Python 3.9+


## Functions

The package provides the following core data validation and cleaning utilities:

| Function | Description |
|----------|-------------|
| `standardize_headers()` | Standardize DataFrame column headers to a clean snake_case format. |
| `drop_duplicate_columns()` | Remove columns with duplicate header names. |
| `drop_constant_columns()` | Remove columns that contain a single unique value across all rows. |
| `find_duplicates()` | Identifies duplicate rows in a dataset based on one or more specified columns, helping users quickly detect and inspect redundant data. |
| `handle_missing()` | Handles missing data in input Pandas dataframe so as to speed up the data science pipeline. |
| `missing_summary()` | Summarizes missing values per column (count and proportion) to help assess data completeness. |


## Development Setup

```bash
conda env create -f environment.yml
conda activate ez_df_data_validator
pip install -e .[tests,dev]
```


## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=ez_df_data_validator --cov-report=term-missing --cov-branch
```


## Continuous Integration

This project uses GitHub Actions for automated testing and code quality checks.  
CI workflow includes:

- Python 3.12 environment  
- Editable package installation with dev/test dependencies  
- Pytest with coverage reporting  
- Ruff linting  

Workflows run on pushes and pull requests to `main`.


## Documentation

Project documentation is automatically generated using **quartodoc** and deployed with **GitHub Pages** as part of the CI/CD workflow.

You can view the latest documentation here:  
https://UBC-MDS.github.io/ez-df-data-validator/


## Position of this package in the Python Ecosystem

This package is intended to complement existing data science libraries rather than replace them. Core functionality overlaps with well established tools such as [pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/), which provide operations for data manipulation and cleaning. However, this package focuses on wrapping common data cleaning patterns into simple functions that are easy to use. Similar preprocessing utilities also exist in [scikit-learn](https://scikit-learn.org/).

## Copyright

- Copyright © 2026 Nishanth Kumarasamy etc.
- Free software distributed under the [MIT License](./LICENSE).

## Contributors

- Gaurang Ahuja
- Nishanth Kumarasamy
- Johnson Leung
- Siting Wang
