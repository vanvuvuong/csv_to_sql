from alive_progress.core.progress import alive_bar
from libs.db_utils import init_engine
from libs.process_data import process_data
from time import sleep
from typer import Option
import sys, typer

app = typer.Typer()


def chunker(data_frame, size):
	return (data_frame[pos:pos + size] for pos in range(0, len(data_frame), size))

@app.command("import")
def import_data(csv_file: str, encoding:str = Option('utf-8', "--encode"),
	delimiter:str = Option(',', "--deli"), quotechar:str = Option('"', "--quote"),
	config_file: str = "config/config.yaml"):
	engine = init_engine(config_file)
	table_name, data_frame = process_data(csv_file, encoding, delimiter, quotechar)
	chunksize = int(len(data_frame)/100)
	if not table_name and data_frame:
		sys.exit(0)
	with alive_bar(int(len(data_frame)/chunksize)) as bar:
		for index, cdf in enumerate(chunker(data_frame, chunksize)):
			replace = "replace" if index == 0 else "append"
			cdf.to_sql(table_name, con=engine, if_exists=replace)
			bar()
	sleep(0.25)
	print('#########################')
	sleep(0.5)
	print("Finish import the data")
	sleep(0.25)
	print('#########################')


app()
