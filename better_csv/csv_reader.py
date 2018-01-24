import csv
from enum import Enum
import csv_utilities
from csv_row import CsvRow
from exceptions import RowDoesNotExistException


class ReaderStatus(Enum):
    READING = 0
    FINISHED = 1


class CsvReader:
    """
    Improved CSV reader with the ability to index each row

    Attributes:
        headers (list): List of headers for CSV file
        current_row_number (int): number of the current row of the reader
    """

    def __init__(self, input_io_stream):
        self.input_io_stream = input_io_stream
        self.csv_reader = csv.reader(self.input_io_stream)
        self.current_reader_status = ReaderStatus.READING
        self.current_stream_position = 0
        self.current_row_data = None
        self.current_row_number = 0
        self.input_row_positions = csv_utilities.get_csv_row_positions(self.input_io_stream)
        self.headers = csv_utilities.get_csv_headers(self.input_io_stream)
    
    def read_next_row(self):
        """Reads the next available row based on the current file pointer position"""
        if not self.current_row_data:
            try:
                self.current_row_data = next(self.csv_reader)
            except StopIteration:
                self.current_reader_status = ReaderStatus.FINISHED
                return None

        row = CsvRow(self.current_row_data, self.headers)
        self.current_row_number += 1
        try:
            self.current_row_data = next(self.csv_reader)
            return row
        except StopIteration:
            self.current_reader_status = ReaderStatus.FINISHED
            return row

    def read_row(self, row_number):
        """Reads the row at the given row number"""
        self.move_to_row(row_number)
        row = self.read_next_row()
        if row:
            return row

    def move_to_row(self, row_number):
        """Moves the file pointer to the position of the specified row number"""
        try:
            position = self.input_row_positions[row_number]
        except IndexError:
            raise RowDoesNotExistException
        self.current_row_data = None
        self.current_reader_status = ReaderStatus.READING
        self.current_stream_position = position
        self.current_row_number = self.input_row_positions.index(self.current_stream_position)
        self.input_io_stream.seek(position)

    def good(self):
        """Returns true when the file is good to continue reading from"""
        return self.current_reader_status == ReaderStatus.READING

    def total_rows(self):
        """Returns the count of total rows"""
        return len(self.input_row_positions)

    def valid_data(self):
        """Returns true as long as there is at least one row data"""
        return len(self.input_row_positions) > 1

    def close(self):
        """Closes the input stream"""
        self.input_io_stream.close()
