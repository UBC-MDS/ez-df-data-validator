import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from dsci_524_group23.handle_missing import handle_missing


def test_handle_missing():
    # Setup Data
    data = {
        'A': [1, 2, np.nan, 4, 4],
        'B': ['x', 'y', np.nan, 'x', 'x'],
        'C': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)

    # --- Test 1: Strategy 'mean' ---
    df_mean = df.copy()
    res_mean = handle_missing(df_mean, strategy='mean', columns=['A'])

    expected_mean = df.copy()
    expected_mean.loc[2, 'A'] = 2.75

    try:
        assert_frame_equal(res_mean[['A']], expected_mean[['A']])
        print("Test 'mean' passed.")
    except AssertionError:
        print("Test 'mean' failed.")

    # --- Test 2: Strategy 'mode' on Object column ---
    df_mode = df.copy()
    res_mode = handle_missing(df_mode, strategy='mode', columns=['B'])

    expected_mode = df.copy()
    expected_mode.loc[2, 'B'] = 'x'

    try:
        assert_frame_equal(res_mode[['B']], expected_mode[['B']])
        print("Test 'mode' passed.")
    except AssertionError:
        print("Test 'mode' failed.")

    # --- Test 3: Strategy 'drop' ---
    # Expected: Row 2 should be removed entirely
    df_drop = df.copy()
    res_drop = handle_missing(df_drop, strategy='drop')
    try:
        assert len(res_drop) == 4
        assert 2 not in res_drop.index
        print("Test 'drop' passed.")
    except AssertionError:
        print("Test 'drop' failed.")

    # --- Test 4: Error Handling ---
    # Test Invalid Strategy
    try:
        handle_missing(df, strategy='magic', columns=['A'])
    except ValueError:
        print("Test 'invalid strategy error' passed.")

    # Test Invalid dtype
    df_datetime = df.copy()
    df_datetime['D'] = [pd.to_datetime('05-05-2025'), pd.to_datetime('05-05-2026'), np.nan, np.nan, np.nan]
    try:
        handle_missing(df_datetime, strategy='mode', columns=['D'])
    except TypeError:
        print("Test 'invalid dtype error' passed.")

    # Test invalid input type in arg
    df_type = df.copy()
    try:
        handle_missing(df_type, strategy='mean', columns=5)
    except TypeError:
        print("Test 'invalid input type error' passed.")
    try:
        handle_missing(df_type, strategy=4)
    except TypeError:
        print("Test 'invalid input type error' passed.")