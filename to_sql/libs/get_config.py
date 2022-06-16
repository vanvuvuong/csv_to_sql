import yaml
import os

def get_config_yaml(config_file: str) -> dict:
    """Get configuration from file

    Args:
        config_file (str): configuration file path

    Returns:
        dict
    """
    with open(config_file, 'r+') as file:
        _config_data = yaml.load(file, Loader=yaml.FullLoader)
    for key, value in _config_data.items():
        if not os.environ.get(key):
            continue
        _config_data[key] = os.environ.get(key)
    return _config_data
