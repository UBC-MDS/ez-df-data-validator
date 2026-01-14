import pandas as pd

def handle_missing(df, strategy='drop', columns=None):
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
        Permissible values: mean, median, max, min, mode, drop

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

    if not isinstance(strategy, str):
        raise TypeError('Strategy must be a string.')

    if strategy not in ['mean', 'median', 'max', 'min', 'mode', 'drop']:
        raise ValueError('Strategy must be permitted')

    if not isinstance(df, pd.DataFrame):
        raise TypeError('df must be a pandas DataFrame.')

    if not isinstance(columns, list) and columns is not None:
        raise TypeError('columns must be a list.')

    for col in columns:
        if col not in df.columns:
            raise ValueError(f'Column {col} not in dataframe')

        if strategy == 'drop':
            df[col] = df[col].dropna()

        if strategy == 'mean':
            df[col] = df[col].fillna(df[col].mean())

        if strategy == 'median':
            df[col] = df[col].fillna(df[col].median())

        if strategy == 'max':
            df[col] = df[col].fillna(df[col].max())

        if strategy == 'min':
            df[col] = df[col].fillna(df[col].min())

        if strategy == 'mode':
            df[col] = df[col].fillna(df[col].mode())