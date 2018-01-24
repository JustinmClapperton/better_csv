import pytest

from better_csv.csv_row import CsvRow

test_headers = ['header1', 'header2', 'header3']
test_data = ['column1', 'column2', 'column3']


@pytest.fixture
def valid_csv_row():
    """Creates a valid CsvRow"""
    return CsvRow(test_data, test_headers)

def test_to_dict(valid_csv_row):
    assert valid_csv_row.to_dict()['header2'] == 'column2'
