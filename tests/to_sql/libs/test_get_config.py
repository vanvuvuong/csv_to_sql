from to_sql.libs.get_config import get_config_yaml

def test_get_config_yaml(benchmark):
    file = 'to_sql/config/config.yaml'
    expected_config = {
        "server": "mysql",
        "sql_adapter": "pymysql",
        "mysql_user": "root",
        "mysql_root_password": "test",
        "mysql_host": "database",
        "mysql_local_port": 3306,
        "mysql_database": "to_sql"
    }
    benchmark(get_config_yaml, file)
    assert expected_config == get_config_yaml(file)