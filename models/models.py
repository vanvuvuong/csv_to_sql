"""
	Mapping the data to the Instance to Alchemy Base Format to import data to the Database
"""
from sqlalchemy.ext.declarative import declarative_base
from libs.process_data import process_data
import sqlalchemy
Base = declarative_base()


# THIS CODE USE THE DYNAMIC CLASS
def init_model_property():
	return {
		"__init__": constructor
	}

def constructor(self, **kwarg):
	for key, value in kwarg:
		self.key = key

def conversion(value, _type):
	try:
		value =	globals()[_type](value)
	except Exception as errors:
		value = str(value)
	finally:
		return value

def attach_new_properties(table_name:str, row:list, model_properties:dict):
	"""
		Convert the JSON data type to the instance property
	"""
	model_properties['__tablename__'] = table_name
	unique_id = True
	for _column in row.keys():
		if 'id' == _column.lower():
			model_properties['ID'] = sqlalchemy.Column('ID', sqlalchemy.BigInteger, 
					autoincrement=True, primary_key=True)
			continue
		elif unique_id:
			model_properties['ID'] = sqlalchemy.Column('ID', sqlalchemy.BigInteger, 
					autoincrement=True, primary_key=True)
			unique_id = False

		globals()[_column] = sqlalchemy.Column(_column, sqlalchemy.Text(collation="utf8mb4_general_ci"),
					nullable=True)
		model_properties[_column] = globals()[_column]
	return model_properties
