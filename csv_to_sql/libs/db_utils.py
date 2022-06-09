"""
	Resolving the SQL connection staff
"""
from libs.get_config import get_config_yaml
from sqlalchemy.orm import Session
import sqlalchemy

def init_engine(config_file: str) -> sqlalchemy.engine.Engine:
	"""
		Create a engine to connect to the SQL server
	"""
	config_data = get_config_yaml(config_file)
	engine_url = f"{config_data['server']}+pymysql://{config_data['username']}:{config_data['password']}"\
					f"@{config_data['host']}:{config_data['port']}/{config_data['database']}"
	return sqlalchemy.create_engine(engine_url, encoding='utf-8', echo=False)

def init_session(engine: sqlalchemy.engine.Engine) -> Session:
	"""
		Create the session with the engine
	"""
	return Session(engine)
