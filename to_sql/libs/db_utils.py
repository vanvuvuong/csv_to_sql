import to_sql.libs.logger as Logger
from to_sql.libs.get_config import get_config_yaml
from sqlalchemy.orm import Session
import sqlalchemy

logger = Logger.get_instance()

def init_engine(config_file: str, encoding='utf-8', echo=False) -> sqlalchemy.engine.Engine:
    """Init SQLAlchemy Engine

    Args:
        config_file (str): path of the configuration file
        encoding (str, optional): encoding. Defaults to 'utf-8'.
        echo (bool, optional): whether or not showing the process of SQL Alchemy connection. Defaults to False.

    Returns:
        sqlalchemy.engine.Engine: engine for create connection with SQL server
    """
    config_data = get_config_yaml(config_file)
    engine_url = f"{config_data['server']}+{config_data['sql_adapter']}://{config_data['username']}:{config_data['password']}"\
                    f"@{config_data['host']}:{config_data['port']}/{config_data['database']}"
    engine = sqlalchemy.create_engine(engine_url, encoding=encoding, echo=echo)
    logger.info(engine.connect())
    return engine

def init_session(engine: sqlalchemy.engine.Engine) -> Session:
    """Init SQL session

    Args:
        engine (sqlalchemy.engine.Engine): Create session from engine

    Returns:
        Session: _description_
    """
    return Session(engine)
