import pandas as pd

def handel_missing(df, strategy='drop', columns=None):
    """
    Handles missing data in a pandas DataFrame.

    Function returns a pandas DataFrame where missing
    values are handled in a user-defined way.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame

    strategy : str, default 'drop'
        The strategy to use for handling missing values.

    columns : list, default None
        Columns where the missing values are to be handled.

    Returns
    -------
    pandas.DataFrame
        Dataframe where missing values have been handled.

    Raises
    ------
    TypeError
        If `df` is not a pandas DataFrame.

    ValueError
        If `strategy` is not a permitted strategy.
    """
    pass