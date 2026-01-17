import pytest
import pandas as pd
from dsci_524_group23.schema_standardizer import standardize_schema

def test_standardize_schema_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        standardize_schema([1, 2, 3])

def test_standardize_schema_empty_df():
    df_empty = pd.DataFrame()
    out = standardize_schema(df_empty)
    expected_out = pd.DataFrame()
    
    pd.testing.assert_frame_equal(out, expected_out)

def test_standardize_schema_non_string_headers():
    df_int_headers = pd.DataFrame({0: [1, 2], 1: [3, 4]})
    out = standardize_schema(df_int_headers)
    
    expected_out = pd.DataFrame({'0': [1, 2], '1': [3, 4]})  
    pd.testing.assert_frame_equal(out, expected_out)
    
def test_standardize_schema_success():
    df_input = pd.DataFrame({
        'First Name': ['Alice', 'Bob', 'Charlie'],
        'first_name': [1, 2, 3], # Duplicate collision
        'Age (Years)': [25, 30, 35],
        'Country': ['US', 'US', 'US'],
        'Salary/in/USD': [50000, 60000, 70000]})
    out = standardize_schema(df_input)
    
    assert 'first_name' in out.columns
    assert out['first_name'].iloc[0] == 'Alice'