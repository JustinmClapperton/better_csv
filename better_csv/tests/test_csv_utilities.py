from io import StringIO

from better_csv.csv_utilities import get_csv_headers, get_csv_row_positions
from tests.csv_data_factory import create_test_csv, initial_data

test_csv = create_test_csv()


def test_get_headers_returns_correct_headers():
    assert get_csv_headers(StringIO(test_csv)) == initial_data[0]


def test_get_csv_row_positions_has_correct_values():
    row_posiitons = get_csv_row_positions(StringIO(test_csv))
    count = 0
    for row in range(len(initial_data)):
        assert row_posiitons[row] == count
        count += sum([len(values) for values in initial_data[row]]) + 3