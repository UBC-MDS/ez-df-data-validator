import pandas as pd
import numpy as np
import pytest

from dsci_524_group23.find_duplicates import find_duplicates


def test_find_duplicates_success():
    df = pd.DataFrame({"A": [1, 1, 2], "B": [3, 3, 4]})

    out = find_duplicates(df)
    expected_out = pd.DataFrame({"A": [1], "B": [3]})

    pd.testing.assert_frame_equal(out, expected_out)


def test_find_duplicates_data_type_error():
    with pytest.raises(TypeError):
        find_duplicates(5)


def test_find_duplicates_with_empty_df():
    df = pd.DataFrame()

    out = find_duplicates(df)
    expected_out = pd.DataFrame()

    pd.testing.assert_frame_equal(out, expected_out)


def test_find_duplicates_keep_value_error():
    df = pd.DataFrame({"A": [1, 1], "B": [2, 2]})

    with pytest.raises(ValueError):
        find_duplicates(df, keep="name")


def test_find_duplicates_subset_missing_column():
    df = pd.DataFrame({"A": [1, 1], "B": [2, 2]})

    with pytest.raises(ValueError):
        find_duplicates(df, subset=["C"])


def test_subset_not_list_type_error():
    df = pd.DataFrame({"A": [1, 1]})

    with pytest.raises(TypeError):
        find_duplicates(df, subset="A")


def test_empty_subset_value_error():
    df = pd.DataFrame({"A": [1, 1]})

    with pytest.raises(ValueError):
        find_duplicates(df, subset=[])


def test_keep_false_returns_all_duplicates():
    df = pd.DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})

    out = find_duplicates(df, keep=False)
    expected = pd.DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})

    pd.testing.assert_frame_equal(out, expected)


def test_keep_last():
    df = pd.DataFrame({"A": [1, 1, 1], "B": [2, 2, 2]})

    out = find_duplicates(df, keep="last")
    expected = pd.DataFrame({"A": [1, 1], "B": [2, 2]})

    pd.testing.assert_frame_equal(out, expected)


def test_no_duplicates_returns_empty_df():
    df = pd.DataFrame({"A": [1, 2, 3]})

    out = find_duplicates(df)
    expected = df.iloc[0:0]

    pd.testing.assert_frame_equal(out, expected)


def test_nan_duplicates():
    df = pd.DataFrame({"A": [1, 1, np.nan, np.nan]})

    out = find_duplicates(df, keep=False)
    expected = df

    pd.testing.assert_frame_equal(out, expected)


def test_subset_valid():
    df = pd.DataFrame({"A": [1, 1, 2], "B": [1, 2, 2]})

    out = find_duplicates(df, subset=["A"])
    expected = pd.DataFrame({"A": [1], "B": [2]})

    pd.testing.assert_frame_equal(out, expected)
