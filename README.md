# ez-df-data-validator

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/badge/TestPyPI-v0.1.2-blue)](https://test.pypi.org/project/ez-df-data-validator/) |


## Summary

ez-df-data-validator is a project that provides basic, but essential data cleaning functionality for ML workflows.
This package provides a lightweight and user friendly toolkit for common data cleaning tasks in Python. It is designed to streamline data preprocessing by offering clear, reusable functions for detecting duplicates, standardizing column names, and handling missing values. The goal is to reduce repetitive code and make data preparation more efficient and reproducible.

## Installation

Install for regular use:

Create a new folder using `mkdir test_ez` and run the below command:

```bash
pip install -i https://test.pypi.org/simple/ ez-df-data-validator
```

### Requirements
- Python 3.10+

### Example usage

Within the `test_ez` folder, create a test file using `touch test_package.py`. Copy the below contents into this newly created file.

```python
import pandas as pd
import numpy as np
from ez_df_data_validator import (
    standardize_schema, 
    missing_summary, 
    handle_missing,
    find_duplicates
)

# Create a messy dataset
df = pd.DataFrame({
    "Age ": [25, 25, 30, np.nan],
    "Income($)": [50000, 50000, 60000, 60000],
    "City": ["Van", "Van", "Tor", "Tor"]
})

# Clean headers
df = standardize_schema(df)

# Check for duplicates
duplicates = find_duplicates(df)
print(f"Found {len(duplicates)} duplicate rows")

# Summarize missing values
print(missing_summary(df))

# Handle missing values
df_clean = handle_missing(df, strategy="drop")
```

Run the script with `python test_package.py`. It should show an output similar to:

```
$ python test_package.py
Found 1 duplicate rows
        missing_count  missing_pct
column                            
age                 1         0.25
income              0         0.00
city                0         0.00

```

## Functions

The package provides the following core data validation and cleaning utilities:

| Function | Description |
|----------|-------------|
| `standardize_schema()` | Standardize DataFrame column headers, remove duplicate columns and drop constant columns. |
| `find_duplicates()` | Identifies duplicate rows in a dataset based on one or more specified columns, helping users quickly detect and inspect redundant data. |
| `handle_missing()` | Handles missing data in input Pandas dataframe so as to speed up the data science pipeline. |
| `missing_summary()` | Summarizes missing values per column (count and proportion) to help assess data completeness. |


## Developer Guide

Follow these steps to set up the development environment and contribute to the project.

We use **conda** to manage dependencies.

```bash
# Create and activate environment
conda env create -f environment.yml
conda activate ez_df_data_validator

# Install package with development + testing + docs tools
pip install -e ".[tests,dev,docs]"

# Run tests
pytest
pytest --cov=ez_df_data_validator --cov-report=term-missing --cov-branch

# Build documentation locally
quartodoc build
quarto preview
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

- [**Project Homepage**](https://ubc-mds.github.io/ez-df-data-validator/)
- [**API Reference**](https://ubc-mds.github.io/ez-df-data-validator/reference/)
- [**TestPYPI Package**](https://test.pypi.org/project/ez-df-data-validator/)

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
