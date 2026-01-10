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
    """
    pass
