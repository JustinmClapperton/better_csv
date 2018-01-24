
initial_data = [['header1', 'header2', 'header3'],
                ['row1_column1', 'row1_column2', 'row1_column3'],
                ['row2_column1' 'row2_column2', 'row2_column3']
                ]


def create_test_csv(csv_data=initial_data):
    list_of_csv = []
    for data in csv_data:
        list_of_csv.append(','.join(data))
    return '\n'.join(list_of_csv)

