import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from dsci_524_group23.handle_missing import handle_missing
import pytest

@pytest.fixture
def test_df():
    """Fixture to provide a fresh DataFrame for every test."""
    data = {
        'A': [1, 2, np.nan, 4, 4],
        'B': ['x', 'y', np.nan, 'x', 'x'],
        'C': [10, 20, 30, 40, 50],
        'D': [5.0, 2.5, 2.5, 4.0, 5.0]
    }
    return pd.DataFrame(data)


def test_handle_missing_mean(test_df):
    res_mean = handle_missing(test_df.copy(), strategy='mean', columns=['A'])
    expected_mean = test_df.copy()
    expected_mean.loc[2, 'A'] = 2.75
    assert_frame_equal(res_mean[['A']], expected_mean[['A']])


def test_handle_missing_mode(test_df):
    res_mode = handle_missing(test_df.copy(), strategy='mode', columns=['B'])
    expected_mode = test_df.copy()
    expected_mode.loc[2, 'B'] = 'x'
    assert_frame_equal(res_mode[['B']], expected_mode[['B']])


def test_handle_missing_drop(test_df):
    res_drop = handle_missing(test_df.copy(), strategy='drop')
    assert len(res_drop) == 4
    assert 2 not in res_drop.index


def test_handle_missing_invalid_strategy(test_df):
    with pytest.raises(ValueError):
        handle_missing(test_df, strategy='magic', columns=['A'])


def test_handle_missing_invalid_dtype(test_df):
    df_datetime = test_df.copy()
    df_datetime['E'] = [pd.to_datetime('2025-05-05'), pd.to_datetime('2026-05-05'), np.nan, np.nan, np.nan]
    with pytest.raises(TypeError):
        handle_missing(df_datetime, strategy='mode', columns=['E'])


def test_handle_missing_invalid_input_types(test_df):
    # Test invalid columns type
    with pytest.raises(TypeError, match='columns must be a list.'):
        handle_missing(test_df, strategy='mean', columns=5)

    # Test invalid strategy type
    with pytest.raises(TypeError, match='Strategy must be a string.'):
        handle_missing(test_df, strategy=4)

def test_handle_missing_no_na(test_df):
    cd_only = test_df[['C', 'D']].copy()
    res = handle_missing(cd_only, strategy='mean', columns=['C', 'D'])
    assert_frame_equal(res, cd_only)

def test_handle_missing_all_columns_default(test_df):
    res = handle_missing(test_df, strategy='mode', columns=None)
    assert res.isna().sum().sum() == 0

def test_handle_missing_non_df(test_df):
    with pytest.raises(TypeError, match='df must be a pandas DataFrame.'):
        handle_missing(test_df['C'], strategy='mean')

def test_handle_missing_independent_column(test_df):
    df = pd.DataFrame({
        'A': [10, 20, np.nan],  # mean = 15
        'B': [1, 2, np.nan]  # mean = 1.5
    })
    res = handle_missing(df, strategy='mean', columns=['A', 'B'])
    assert res.loc[2, 'A'] == 15
    assert res.loc[2, 'B'] == 1.5

def test_handle_missing_all_nan_column_raises_error():
    df = pd.DataFrame({'A': [np.nan, np.nan, np.nan]})
    with pytest.raises(ValueError, match="Column A only contains NaN."):
        handle_missing(df, strategy='mean', columns=['A'])