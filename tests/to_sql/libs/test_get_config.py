from to_sql.libs.get_config import get_config_yaml

def get_config_yaml():
    file = 'to_sql/config/config.yaml'
    expected_config = {
        "server": "mysql",
        "mysql_user": "user",
        "mysql_root_password": "password",
        "mysql_host": "localhost",
        "mysql_local_port": "3306",
        "mysql_database": "to_sql"
    }
    print(get_config_yaml(file))
    assert expected_config == get_config_yaml(file)