import csv


def get_csv_row_positions(stream):
    row_positions = [0]
    stream.seek(0)
    bad_quotes = False
    quotation_count = 0
    for line in iter(stream.readline, ''):
        line_quotation_count = line.count('"')
        if bad_quotes:
            quotation_count += line_quotation_count
            if line_quotation_count & 1:
                bad_quotes = False
                quotation_count == 0
                row_positions.append(stream.tell())
        else:
            if line_quotation_count & 1:
                quotation_count += line_quotation_count
                bad_quotes = True
            else:
                row_positions.append(stream.tell())

    stream.seek(0)
    return row_positions[:-1]


def get_csv_headers(stream):
    stream.seek(0)
    reader = csv.reader(stream)
    try:
        row_data = next(reader)
        stream.seek(0)
        headers = ["{}_{}".format(value, index) if row_data.count(value) > 1 else value for index, value in enumerate(row_data)]
        return headers
    except StopIteration:
        return None