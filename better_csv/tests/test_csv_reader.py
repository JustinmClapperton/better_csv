from io import StringIO
import pytest
from csv_reader import CsvReader
from exceptions import RowDoesNotExistException
from tests.csv_data_factory import create_test_csv, initial_data

initial_csv = create_test_csv()


@pytest.fixture
def valid_csv_reader():
    """Returns csv reader with initial csv data"""
    return CsvReader(StringIO(initial_csv))


def test_header_count(valid_csv_reader):
    assert len(valid_csv_reader.headers) == 3


def test_input_row_positions_count(valid_csv_reader):
    assert len(valid_csv_reader.input_row_positions) == 3


def test_row_position_equals_sum_of_previous_rows_characters(valid_csv_reader):
    count = 0
    for row in range(len(initial_data)):
        assert valid_csv_reader.input_row_positions[row] == count
        count += sum([len(values) for values in initial_data[row]]) + 3


def test_read_next_row(valid_csv_reader):
    row = 0
    while valid_csv_reader.good():
        assert valid_csv_reader.read_next_row().data == initial_data[row]
        row = valid_csv_reader.current_row


def test_read_row_raises_exception_for_invalid_row(valid_csv_reader):
    with pytest.raises(RowDoesNotExistException):
        valid_csv_reader.read_row(9999)


def test_read_row(valid_csv_reader):
    assert valid_csv_reader.read_row(row_number=2).data == initial_data[2]


def test_valid_data_with_valid_csv(valid_csv_reader):
    assert valid_csv_reader.valid_data()


def test_total_rows(valid_csv_reader):
    valid_csv_reader.total_rows == len(initial_data)



