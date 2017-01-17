#!/usr/bin/python3

# Tables using the tabulate library

from tabulate import tabulate

table_data = [
['Heading1', 'Heading2'],
['row1 col1', 'row1 col2'],
['row2 col1', 'row2 col2'],
]

print(tabulate(table_data, headers='firstrow', tablefmt='fancy_grid'))
