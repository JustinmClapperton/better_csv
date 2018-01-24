import itertools


class CsvRow(object):

    def __init__(self, data, headers):
        self._data = data
        self._headers = headers

    @property
    def data(self):
        return self._data

    @property
    def headers(self):
        return self._headers

    def to_dict(self):
        return dict(itertools.zip_longest(self.headers, self.data))
