# Welcome to DSCI_524_group23

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/dsci_524_group23.svg)](https://pypi.org/project/dsci_524_group23/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/dsci_524_group23.svg)](https://pypi.org/project/dsci_524_group23/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

## Summary

DSCI_524_group23 is a project that provides basic, but essential data cleaning functionality for ML workflows. 
This package provides a lightweight and user friendly toolkit for common data cleaning tasks in Python. It is designed to streamline data preprocessing by offering clear, reusable functions for detecting duplicates, standardizing column names, and handling missing values. The goal is to reduce repetitive code and make data preparation more efficient and reproducible.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install dsci_524_group23
```

TODO: Add a brief example of how to use the package to this section

To use dsci_524_group23 in your code:

```python
>>> import dsci_524_group23
>>> dsci_524_group23.hello_world()
```

## Functions

These are the functions in this package:

- rename_feature_headers()

- find_duplicates()
Identifies duplicate rows in a dataset based on one or more specified columns, helping users quickly detect and inspect redundant data.

- handle_missing()

## Position of this package in the Python Ecosystem

This package is intended to complement existing data science libraries rather than replace them. Core functionality overlaps with well established tools such as [pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/), which provide operations for data manipulation and cleaning. However, this package focuses on wrapping common data cleaning patterns into simple functions that are easy to use. Similar preprocessing utilities also exist in [scikit-learn](https://scikit-learn.org/).

## Copyright

- Copyright © 2026 Nishanth Kumarasamy.
- Free software distributed under the [MIT License](./LICENSE).

## Contributors

- Gaurang Ahuja
- Nishanth Kumarasamy
- Johnson Leung
- Siting Wang