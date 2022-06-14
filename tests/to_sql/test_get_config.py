from to_sql.libs.get_config import get_config_yaml

def get_config_yaml():
    file = 'to_sql/config/config.yaml'
    expected_config = {
        "server": "mysql",
        "username": "root",
        "password": "aA123456",
        "host": "localhost",
        "port": "3306",
        "database": "csv"
    }
    assert expected_config == get_config_yaml(file)