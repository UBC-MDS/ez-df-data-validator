import pandas as pd


def find_duplicates(data, subset=None, keep="first"):
    """
    Identify duplicate rows in a pandas DataFrame.

    This function returns the rows that are considered duplicates
    according to the specified subset of columns. The behavior of
    which duplicate rows are returned is controlled by the `keep`
    parameter, following pandas duplicate semantics.

    Parameters
    ----------
    data : pandas.DataFrame
        Input DataFrame to check for duplicate rows.

    subset : list of str, optional
        List of column names to consider when identifying duplicates.
        If None, all columns are used.

    keep : {'first', 'last', False}, default 'first'
        Determines which duplicates are returned:
        - 'first' : Return duplicates except for the first occurrence.
        - 'last' : Return duplicates except for the last occurrence.
        - False : Return all duplicate rows.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing only the rows identified as duplicates.

    Raises
    ------
    TypeError
        If `data` is not a pandas DataFrame.

    ValueError
        If `subset` contains columns not present in `data`
        or if `keep` is not one of {'first', 'last', False}.
    """
    pass
