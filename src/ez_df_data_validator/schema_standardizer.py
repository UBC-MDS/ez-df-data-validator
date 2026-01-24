import pandas as pd
import re

def standardize_schema(data):
    """
    Sanitize and standardize a DataFrames structure.

    This function performs a series of cleaning steps:
    1. Standardizes column headers (snake_case, no punctuation/replace with underscore).
    2. Removes columns that result in duplicate names (keeping the first).
    3. Removes columns containing a single unique value (constants).

    Parameters
    ----------
    data : pandas.DataFrame
        The raw input DataFrame to be standardized.

    Returns
    -------
    pandas.DataFrame
        The fully sanitized DataFrame.

    Raises
    ------
    TypeError
        If the input `data` is not a pandas DataFrame.
    """
    # Defensive check: Input type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    # Create a copy to avoid mutating original data
    df = data.copy()

    # If empty, return immediately
    if df.empty:
        return df

    # 1. Standardize Headers
    new_columns = []
    for i, col in enumerate(df.columns):
        col_str = str(col).lower()
        col_str = re.sub(r'[^a-z0-9]', '_', col_str)
        col_str = re.sub(r'_+', '_', col_str)
        col_str = col_str.strip('_')
        if not col_str:
            col_str = f"untitled_{i}"
        new_columns.append(col_str)

    df.columns = new_columns

    # 2. Drop Duplicate Columns
    df = df.loc[:, ~df.columns.duplicated()]

    # 3. Drop Constant Columns
    df = df.loc[:, df.nunique(dropna=False) > 1]

    return df
