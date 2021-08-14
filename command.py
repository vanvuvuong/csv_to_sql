"""
command
	set the configuration file (user, password, host, database, port)
	insert to sql
	export to sql file
	set the csv file
option
	change the delimiter
	change the quotechar
"""
from typer.params import Argument
from main import connection, read_data, main
import typer
import os

app = typer.Typer()

@app.command("import")
def import_data(file_path: str = Argument(..., help="The path lead to the csv files (normally in the path: `files/sample.csv`)"), delimiter: str = typer.Option(',', "--deli"),
                quotechar: str = typer.Option('"', "--quote")):
	"""
		Importing the data to the SQL server with the CSV files
		\n
		Take a look at the Option seriously before run the code to reduce the unworthy errors
	"""
	if not os.path.isfile('config/config.yaml'):
		error = typer.style("`config/config.yaml`", fg=typer.colors.RED, bg=typer.colors.WHITE)
		typer.echo(f"Missing the configuration. Please check {error} files")
	engine, session = connection('config/config.yaml')
	table_name, data = read_data(file_path, delimiter, quotechar)
	main(engine, session, table_name, data)
	session.close()


@app.command("convert")
def convert_data(file_path: str = Argument("--file"), delimiter: str = typer.Option(',', "--deli"),
                 quotechar: str = typer.Option('"', "--quote")):
	"""
		Convert the CSV data file to the SQL import files
	"""
	pass

app()
