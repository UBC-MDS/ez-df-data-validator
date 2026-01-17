import pandas as pd


def missing_summary(data):
    """
    Generate a summary of missing values in a dataset.

    This function specifies an interface for computing the number and
    proportion of missing values for each column in the input dataset.
    It is intended to help users assess data completeness prior to
    further cleaning steps.

    Parameters
    ----------
    data : pandas.DataFrame
        Input dataset to be analyzed.

    Returns
    -------
    pandas.DataFrame
        A summary table containing the count and percentage of missing
        values for each column.

    Raises
    ------
    ValueError
        If the input data is None or empty.
    TypeError
        If the input data is not a pandas DataFrame.
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
