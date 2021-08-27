import pandas as pd
import re, traceback


def process_data(csv_file: str, encoding: str, delimiter: str, quotechar: str):
	_table_name = csv_file.replace('files/', '').split('.csv')[0]
	_table_name = re.sub('[^a-zA-Z0-9-_]', '', _table_name)
	try:
		_data_frame = pd.read_csv(csv_file, sep=delimiter, quotechar=quotechar, squeeze=True, engine='c',
			skipinitialspace=True, na_values='', keep_default_na=False, parse_dates=True,
			encoding=encoding, warn_bad_lines="warn")
		_data_frame.index = _data_frame.index + 1
		return _table_name, _data_frame
	except Exception as errors:
		traceback.print_exc()
		print(f"Error: {errors}")
		return None, None
