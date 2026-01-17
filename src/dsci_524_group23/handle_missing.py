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
        Permissible values (numeric): mean, median, max, min, mode, drop
        Permissible values (else): mode, drop

    columns : list, default None
        Columns where the missing values are to be handled.
        Default handles all columns.

    Returns
    -------
    pandas.DataFrame
        Dataframe where missing values have been handled.

    Raises
    ------
    TypeError
        If `df` is not a pandas DataFrame.
        If `strategy` is not a string.
        If `columns` is not a list or None.
        If `strategy` cannot be used for dtype of column.
        If dtype of column is not designed to be handled.

    ValueError
        If `strategy` is not permitted.
        If column is not in df.columns.
        If column only contains NaN.

    Examples
    --------
    >>> import numpy as np
    >>> import pandas as pd
    >>>df = pd.DataFrame({
    ...     "A": [1, 1, 2],
    ...     "B": [np.nan, 3, 4]
    ... })
    >>> handle_missing(df)
       A  B
    1  1  3
    2  2  4

    >>> handle_missing(df, strategy='mean')
       A  B
    0  1  3.5
    1  1  3.0
    2  2  4.0
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError('df must be a pandas DataFrame.')

    if not isinstance(strategy, str):
        raise TypeError('Strategy must be a string.')

    if strategy not in ['mean', 'median', 'max', 'min', 'mode', 'drop']:
        raise ValueError('Strategy must be permitted.')

    if columns is None:
        columns = df.columns.tolist()

    if not isinstance(columns, list):
        raise TypeError('columns must be a list.')

    df = df.copy()

    for col in columns:
        if col not in df.columns:
            raise ValueError(f'Column {col} not in dataframe.')

        if df[col].isna().all():
            raise ValueError(f'Column {col} only contains NaN.')

        if strategy == 'drop':
            df = df.dropna(subset=[col])
            continue

        if df[col].isna().sum() == 0:
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            if strategy == 'mean':
                df[col] = df[col].fillna(df[col].mean())

            elif strategy == 'median':
                df[col] = df[col].fillna(df[col].median())

            elif strategy == 'max':
                df[col] = df[col].fillna(df[col].max())

            elif strategy == 'min':
                df[col] = df[col].fillna(df[col].min())

            elif strategy == 'mode':
                df[col] = df[col].fillna(df[col].mode())

            else:
                raise TypeError(f'Strategy {strategy} cannot be used for dtype of column {col}.')

        elif pd.api.types.is_object_dtype(df[col]):
            if strategy == 'mode':
                if df[col].mode().shape[0] == 1:
                    df[col] = df[col].fillna(df[col].mode())
                else:
                    df[col] = df[col].fillna(df[col].mode().iloc[0])
            else:
                raise TypeError(f'Strategy {strategy} cannot be used for dtype of column {col}.')

        else:
            raise TypeError(f'The dtype of column {col} cannot be used. \nColumn {col} has dtype {df[col].dtype}.')

    return df