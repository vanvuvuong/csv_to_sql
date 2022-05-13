from alive_progress.core.progress import alive_bar
from libs.db_utils import init_engine
from libs.process_data import process_data, pd
from libs.logger import logging
from time import sleep
from typer import Option
import sys, typer

app = typer.Typer()


def chunker(data_frame: pd.DataFrame, size: int):
	return (data_frame[pos:pos + size] for pos in range(0, len(data_frame), size))

@app.command("import")
def import_data(csv_file: str, encoding: str = Option('utf-8', "--encode", prompt="Encoding:"),
	delimiter: str = Option(',', "--deli", prompt="Delimiter:"),
	quotechar: str = Option('"', "--quote", prompt="Quote character:"),
	config_file: str = "config/config.yaml"):

	"""
		Process the data with pandas.read_csv and import to database through engine
	"""

	engine = init_engine(config_file)
	try:
		table_name, data_frame = process_data(csv_file, encoding, delimiter, quotechar)
	except Exception as err:
		logging.info(f"Table Name: {table_name}")
		logging.info(f"Data Frame: {data_frame}")
		logging.debug(f"Exception: {err}")
		sys.exit(0)
	if not table_name or not data_frame:
		sys.exit(0)
	chunksize = int(len(data_frame)/100)
	with alive_bar(int(len(data_frame)/chunksize)) as bar:
		for index, cdf in enumerate(chunker(data_frame, chunksize)):
			replace = "replace" if index == 0 else "append"
			cdf.to_sql(table_name, con=engine, if_exists=replace, index_label='index')
			bar()

	sleep(0.25)
	print('#########################')
	sleep(0.5)
	print("Finish import the data")
	sleep(0.25)
	print('#########################')


app()
