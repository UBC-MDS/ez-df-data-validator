import pandas as pd


def find_duplicates(data, subset=None, keep="first"):
    """
    Identify duplicate rows in a pandas DataFrame.

    This function returns the rows that are considered duplicates
    according to the specified subset of columns. Rows are considered
    duplicates if they have identical values across the specified
    columns, following pandas equality and NaN-handling semantics.

    Parameters
    ----------
    data : pandas.DataFrame
        Input DataFrame to check for duplicate rows.

    subset : list of str, optional
        List of column names to consider when identifying duplicates.
        If None, all columns are used. All column names must exist in
        `data`, and the list must not be empty.

    keep : {'first', 'last', False}, default 'first'
        Determines which duplicates are returned:
        - 'first' : Return duplicates except for the first occurrence.
        - 'last' : Return duplicates except for the last occurrence.
        - False : Return all duplicate rows.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame containing only the rows identified as
        duplicates. If no duplicate rows are found, an empty DataFrame
        with the same columns as `data` is returned.

    Raises
    ------
    TypeError
        If `data` is not an instance of pandas.DataFrame.
        If `subset` is not None and is not a list of strings.

    ValueError
        If `subset` contains columns not present in `data`
        or if `keep` is not one of {'first', 'last', False}.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     "A": [1, 1, 2],
    ...     "B": [3, 3, 4]
    ... })
    >>> find_duplicates(df)
       A  B
    1  1  3

    >>> find_duplicates(df, keep=False)
       A  B
    0  1  3
    1  1  3
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    if subset is not None:
        if not isinstance(subset, (list, tuple)):
            raise TypeError("subset must be a list of column names")

        if not all(isinstance(col, str) for col in subset):
            raise TypeError("All elements in subset must be strings")

        if len(subset) == 0:
            raise ValueError("subset cannot be empty")

        missing_cols = [col for col in subset if col not in data.columns]

        if missing_cols:
            raise ValueError(f"Columns not found in data: {missing_cols}")

    if keep not in ("first", "last", False):
        raise ValueError("keep must be one of {'first', 'last', False}")

    duplicated_mask = data.duplicated(subset=subset, keep=keep)
    duplicates_df = (
        data[duplicated_mask].copy().reset_index(drop=True)
    )  # fixed with ChatGPT (test was failing)

    return duplicates_df
