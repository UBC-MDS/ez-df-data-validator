import numpy as np

from dsci_524_group23.find_duplicates import find_duplicates


def test_find_duplicates_success():
    """
    Test that find_duplicates works as expected.
    """
    df = pd.DataFrame({"A": [1, 1, 2], "B": [3, 3, 4]})

    out = find_duplicates(df)
    expected_out = pd.DataFrame({"A": [1], "B": [3]})
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_find_duplicates_data_type_error():
    """
    Test that find_duplicates throws TypeError when data is not a df.
    """
    df = 5
    assertRaises(TypeError, find_duplicates(df))


def test_find_duplicates_with_empty_df():
    """
    Test that find_duplicates works with an empty df.
    """
    df = pd.DataFrame()

    out = find_duplicates(df)
    expected_out = pd.DataFrame()
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_find_duplicates_keep_value_error():
    """
    Test that find_duplicates throws ValueError when keep is not a valid entry.
    """
    keep = "name"
    assertRaises(TypeError, find_duplicates(df, keep=keep))


def test_find_duplicates_subset_value_error():
    """
    Test that find_duplicates throws ValueError when subset is not a valid entry.
    """

    df = pd.DataFrame({"A": [1, 1, 2], "B": [3, 3, 4]})

    assertRaises(TypeError, find_duplicates(df, subset="C"))
