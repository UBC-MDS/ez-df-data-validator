import pandas as pd
import pytest

from ez_df_data_validator.missing_summary import missing_summary


def test_missing_summary_basic_counts_and_pct():
    df = pd.DataFrame(
        {
            "a": [1, None, 3],
            "b": [None, None, "x"],
        }
    )
    out = missing_summary(df)

    # output should be a DataFrame with expected columns
    assert isinstance(out, pd.DataFrame)
    assert set(["missing_count", "missing_pct"]).issubset(out.columns)

    # counts
    assert out.loc["a", "missing_count"] == 1
    assert out.loc["b", "missing_count"] == 2

    # pct (3 rows)
    assert out.loc["a", "missing_pct"] == pytest.approx(1 / 3)
    assert out.loc["b", "missing_pct"] == pytest.approx(2 / 3)


def test_missing_summary_no_missing_returns_zeros():
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    out = missing_summary(df)

    assert out.loc["a", "missing_count"] == 0
    assert out.loc["b", "missing_count"] == 0
    assert out.loc["a", "missing_pct"] == 0
    assert out.loc["b", "missing_pct"] == 0


def test_missing_summary_all_missing_column():
    df = pd.DataFrame({"a": [None, None], "b": [1, None]})
    out = missing_summary(df)

    assert out.loc["a", "missing_count"] == 2
    assert out.loc["a", "missing_pct"] == pytest.approx(1.0)
    assert out.loc["b", "missing_count"] == 1
    assert out.loc["b", "missing_pct"] == pytest.approx(0.5)


def test_missing_summary_empty_dataframe_raises():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        missing_summary(df)


def test_missing_summary_none_raises():
    with pytest.raises(ValueError):
        missing_summary(None)


def test_missing_summary_non_dataframe_raises_typeerror():
    with pytest.raises(TypeError):
        missing_summary([1, 2, 3])


def test_missing_summary_single_row_dataframe():
    df = pd.DataFrame({"a": [None], "b": [1]})
    out = missing_summary(df)

    assert out.loc["a", "missing_count"] == 1
    assert out.loc["a", "missing_pct"] == 1.0
    assert out.loc["b", "missing_count"] == 0
    assert out.loc["b", "missing_pct"] == 0.0


def test_missing_summary_mixed_dtypes():
    df = pd.DataFrame(
        {
            "num": [1, None, 3],
            "char": ["x", None, "y"],
            "bool": [True, False, None],
        }
    )
    out = missing_summary(df)

    assert out.loc["num", "missing_count"] == 1
    assert out.loc["char", "missing_count"] == 1
    assert out.loc["bool", "missing_count"] == 1


def test_missing_summary_index_name_is_column():
    df = pd.DataFrame({"a": [1, None]})
    out = missing_summary(df)

    assert out.index.name == "column"
