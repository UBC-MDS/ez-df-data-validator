import pytest
import numpy as np
import pandas as pd
from dsci_524_group23.schema_standardizer import standardize_schema

def test_standardize_schema_invalid_input_type():
    """Test that a TypeError is raised when input is not a DataFrame."""

    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        standardize_schema([1, 2, 3])

def test_standardize_schema_empty_df():
    """Test that an empty DataFrame input results in an empty DataFrame output."""

    df_empty = pd.DataFrame()
    out = standardize_schema(df_empty)
    expected_out = pd.DataFrame()
    pd.testing.assert_frame_equal(out, expected_out)

def test_standardize_schema_non_string_headers():
    """Test that integer or non-string headers are correctly converted to strings."""

    df_int_headers = pd.DataFrame({0: [1, 2], 1: [3, 4]})
    out = standardize_schema(df_int_headers)

    expected_out = pd.DataFrame({'0': [1, 2], '1': [3, 4]})  
    pd.testing.assert_frame_equal(out, expected_out)
    
def test_standardize_schema_success():
    """Test the main cleaning logic: snake_case headers, duplicate removal, and constant dropping."""

    df_input = pd.DataFrame({
        'First Name': ['Alice', 'Bob', 'Charlie'],
        'first_name': [1, 2, 3], # Duplicate collision
        'Age (Years)': [25, 30, 35],
        'Country': ['US', 'US', 'US'],
        'Salary/in/USD': [50000, 60000, 70000],
        '__Weird__Header__': [1, 2, 3]})
    out = standardize_schema(df_input)
    
    expected_out = pd.DataFrame({
        'first_name': ['Alice', 'Bob', 'Charlie'],
        'age_years': [25, 30, 35],
        'salary_in_usd': [50000, 60000, 70000],
        'weird_header': [1, 2, 3] })
    
    pd.testing.assert_frame_equal(out, expected_out)

def test_standardize_schema_all_constant_columns():
    """Test that a DataFrame consisting entirely of constant columns returns an empty DataFrame."""

    df_all_const = pd.DataFrame({'A': [1, 1], 'B': ['x', 'x']})
    out = standardize_schema(df_all_const)
    
    expected_out = pd.DataFrame(index=[0, 1], columns=pd.Index([], dtype='object'))
    pd.testing.assert_frame_equal(out, expected_out)

def test_standardize_schema_constant_with_nan():
    """Test that columns containing only NaN values are treated as constant and removed."""

    df = pd.DataFrame({'A': [1, 2],  'B': [np.nan, np.nan]})
    out = standardize_schema(df)
    expected_out = pd.DataFrame({'a': [1, 2]})
    pd.testing.assert_frame_equal(out, expected_out)

def test_standardize_schema_empty_result_header():
    """Test that headers becoming empty strings (e.g., '$$$') get renamed safely."""
    df = pd.DataFrame({'$$$': [1, 2], '...': [3, 4], 'Valid': [5, 6]})
    out = standardize_schema(df)
    
    expected_out = pd.DataFrame({'untitled_0': [1, 2], 'untitled_1': [3, 4], 'valid': [5, 6]})
    pd.testing.assert_frame_equal(out, expected_out)
    