from to_sql.libs.db_utils import *
from to_sql.models.models import *


config_file = 'config/config.yaml'
engine = init_engine(config_file)
session = init_session(engine)
csv_file = 'files/sample.csv'
model_properties = init_model_property()
table_name, data = process_data(csv_file=csv_file, delimiter=',', quotechar='"')
example = data[0]
model_properties = attach_new_properties(table_name, example, model_properties)
Model = type("DynamicClass", (Base, ), model_properties)
Base.metadata.create_all(engine)
insert_data = []
for index, row in enumerate(data):
	globals()[f'row_{index}'] = Model()
	for key, value in row.items():
		setattr(globals()[f'row_{index}'], key, value)
	session.add(globals()[f'row_{index}'])
session.commit()
