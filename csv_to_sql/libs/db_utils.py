"""
	Resolving the SQL connection staff
"""
from libs.get_config import get_config_yaml
from sqlalchemy.orm import Session
import sqlalchemy
import traceback


def init_engine(config_file: str):
	"""
		Create a engine to connect to the SQL server
	"""
	config_data = get_config_yaml(config_file)
	engine_url = f"mysql+pymysql://{config_data['username']}:{config_data['password']}"\
					f"@{config_data['host']}:{config_data['port']}/{config_data['database']}"
	try:
		return sqlalchemy.create_engine(engine_url, encoding='utf-8', echo=False)
	except Exception as errors:
		print(f'Failed to connect to MySQL: {errors}')
		traceback.print_exc()
		return None


def init_session(engine: sqlalchemy.engine):
	"""
		Create the session of the engine
	"""
	try:
		_session = Session(engine)
		return _session
	except Exception as errors:
		print(f"Failed to init session: {errors}")
		traceback.print_exc()
		return None
