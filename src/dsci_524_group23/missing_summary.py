import pandas as pd


def missing_summary(data):
    """
    Generate a summary of missing values in a dataset.

    This function computes, for each column in a pandas DataFrame,
    the total number of missing values and the proportion of missing
    values relative to the number of rows.

    Parameters
    ----------
    data : pandas.DataFrame
        Input dataset to be analyzed.

    Returns
    -------
    pandas.DataFrame
        A summary table indexed by column name with:
        - ``missing_count`` (int): number of missing values per column
        - ``missing_pct`` (float): proportion of missing values per column

    Raises
    ------
    ValueError
        If ``data`` is None or an empty DataFrame.
    TypeError
        If ``data`` is not a pandas DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> from dsci_524_group23.missing_summary import missing_summary
    >>> df = pd.DataFrame({"a": [1, None, 3], "b": [None, None, "x"]})
    >>> missing_summary(df)
            missing_count  missing_pct
    column
    a                   1     0.333333
    b                   2     0.666667
    """

    if data is None:
        raise ValueError("`data` cannot be None.")
    if not isinstance(data, pd.DataFrame):
        raise TypeError("`data` must be a pandas DataFrame.")
    if data.empty:
        raise ValueError("`data` cannot be empty.")

    missing_count = data.isna().sum()
    missing_pct = missing_count / len(data)

    out = pd.DataFrame(
        {
            "missing_count": missing_count,
            "missing_pct": missing_pct,
        }
    )
    out.index.name = "column"
    return out
