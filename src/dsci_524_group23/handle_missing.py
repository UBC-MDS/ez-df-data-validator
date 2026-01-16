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
        raise ValueError('Strategy must be permitted.')

    if not isinstance(df, pd.DataFrame):
        raise TypeError('df must be a pandas DataFrame.')

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
            df = df.dropna(subset=[col], inplace=True)
            continue

        if df[col].isna().sum() == 0:
            continue

        if df[col].dtype not in ['object', 'category', 'bool', 'int', 'float', 'str']:
            raise TypeError(f'The dtype of column {col} cannot be used. \nColumn {col} has dtype {df[col].dtype}.')

        if df[col].dtype in ['int', 'float']:
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

        elif df[col].dtype in ['object', 'category', 'bool']:
            if strategy == 'mode':
                if df[col].mode().shape[0] == 1:
                    df[col] = df[col].fillna(df[col].mode())
                else:
                    df[col] = df[col].fillna(df[col].mode().iloc[0])

    return df