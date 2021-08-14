"""
	Use all the libs functions and models to run
"""
from alive_progress.core.progress import alive_bar
from models.models import Base, init_model_property, process_data, attach_new_properties
from libs.db_utils import init_engine, init_session
from time import sleep


def connection(config_file):
	engine = init_engine(config_file)
	session = init_session(engine)
	return engine, session


def read_data(csv_file, delimiter, quotechar):
	table_name, data = process_data(
		csv_file=csv_file, delimiter=delimiter, quotechar=quotechar)
	return table_name, data


def make_model(table_name, sample_data):
	model_properties = init_model_property()
	model_properties = attach_new_properties(table_name, sample_data, model_properties)
	Model = type("DynamicClass", (Base, ), model_properties)
	return Model


def main(engine, session, table_name, data):
	sample_data = data[0]
	Model = make_model(table_name, sample_data)
	Base.metadata.create_all(engine)
	with alive_bar(len(data)) as bar:
		for index, row in enumerate(data):
			globals()[f'row_{index}'] = Model()
			for key, value in row.items():
				setattr(globals()[f'row_{index}'], key, value)
			session.add(globals()[f'row_{index}'])
			if index % 20:
				sleep(0.000015)
			bar()
	sleep(0.25)
	print("###############################")
	sleep(0.25)
	print("Committing the data changing..")
	session.commit()
	sleep(0.25)
	print("###############################")
