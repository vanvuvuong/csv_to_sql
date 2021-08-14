"""
	Getting the table name
	Process the csv data to JSON type data for creating Mapping Instance
"""

import csv
import re

def process_data(csv_file:str, delimiter:str, quotechar:str):
	"""
		Process the csv file, and convert to JSON type

		The default delimiter is `,` you could change them to whatever the delimiter you want

		The default quote character is `"` you could change them to whatever the character you want
	"""
	_table_name = csv_file.replace('files/', '').split('.csv')[0]
	_table_name = re.sub('[^a-zA-Z0-9-_]', '', _table_name)
	with open(csv_file, 'r+', encoding='utf-8', errors='ignore') as file:
		data = csv.DictReader(file, delimiter=delimiter, skipinitialspace=True, quotechar=quotechar)
		_csv_data = list()
		for row in data:
			_row = dict()
			for column, column_data in row.items():
				_row[column] = column_data
			_csv_data.append(_row)
		# equal with
		# csv_data = [{column, column_data for column, column_data in row.items()} for row in csv.DictReader()]
	return _table_name, _csv_data
