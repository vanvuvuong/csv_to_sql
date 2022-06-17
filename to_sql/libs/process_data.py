import libs.logger as Logger
import re, traceback
from time import time_ns
from typing import Optional, Tuple
from pandas.core.frame import DataFrame
import pandas as pd

logger = Logger.get_instance()

def create_table_name(file: str) -> Tuple[str, str]:
    _table_name = f"{re.sub('[^a-zA-Z0-9-_]', '', file.split('/')[-1].split('.')[0])}_{str(time_ns())[-5:]}"
    _file_extension = file.split('.')[-1]
    assert _file_extension in {'csv', 'xml'}
    return _table_name, _file_extension

def csv_to_frame(csv_file: str, encoding: str, delimiter: str, quotechar: str) -> Optional[DataFrame]:
    """Process the data from csv file

    Args:
        csv_file (str): csv path files
        encoding (str): csv encoding
        delimiter (str): csv delimiter
        quotechar (str): csv quotechar

    Returns:
        Optional[DataFrame]: data frame
    """
    _data_frame = None
    try:
        _data_frame = pd.read_csv(csv_file, sep=delimiter, quotechar=quotechar, engine='c',
            skipinitialspace=True, na_values='', keep_default_na=False, parse_dates=True, escapechar = '\\',
            encoding=encoding, error_bad_lines=False)
        _data_frame.index = _data_frame.index + 1

    except UnicodeDecodeError as errors:
        traceback.print_exc()
        logger.info("---------------------------------")
        logger.warning(f"The ENCODING ({encoding}) to read the file NOT MATCH with the CSV FILE's ENCODING. Please choose the RIGHT ENCODING ONE.")
        logger.info("---------------------------------")
        logger.debug(f"Please Google the errors: {errors}")
    except Exception as errors:
        logger.info("---------------------------------")
        traceback.print_exc()
        logger.debug(f"Errors: {errors}")
        logger.info("---------------------------------")
    finally:
        return _data_frame

def xml_to_frame(xml_file: str, encoding: str, parser: str) -> Optional[DataFrame]:
    _data_frame = None
    try:
        _data_frame = pd.read_xml(xml_file, encoding=encoding, parser=parser)
    except Exception as errors:
        logger.info("---------------------------------")
        traceback.print_exc()
        logger.debug(f"Errors: {errors}")
        logger.info("---------------------------------")
    finally:
        return _data_frame