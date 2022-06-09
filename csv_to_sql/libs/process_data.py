from .logger import logging
import pandas as pd
import re, traceback


def process_data(csv_file: str, encoding: str, delimiter: str, quotechar: str):
	_table_name = csv_file.replace('files/', '').split('.csv')[0]
	_table_name = re.sub('[^a-zA-Z0-9-_]', '', _table_name)
	try:
		_data_frame = pd.read_csv(csv_file, sep=delimiter, quotechar=quotechar, squeeze=True, engine='c',
			skipinitialspace=True, na_values='', keep_default_na=False, parse_dates=True, escapechar = '\\',
			encoding=encoding, warn_bad_lines=True, error_bad_lines=False)
		_data_frame.index = _data_frame.index + 1
		return _table_name, _data_frame

	except UnicodeDecodeError as errors:
		traceback.print_exc()
		logging.info("---------------------------------")
		logging.warning(f"The ENCODING ({encoding}) to read the file NOT MATCH with the CSV FILE's ENCODING. Please choose the RIGHT ENCODING ONE.")
		logging.info("---------------------------------")
		logging.debug(f"Please Google the errors: {errors}")
		return None, None
	except Exception as errors:
		logging.info("---------------------------------")
		traceback.print_exc()
		logging.info(f"Errors: {errors}")
		return None, None
