import yaml

def get_config_yaml(config_file: str) -> dict:
    """Get configuration from file

    Args:
        config_file (str): configuration file path

    Returns:
        dict
    """

    with open(config_file, 'r+') as file:
        _config_data = yaml.load(file, Loader=yaml.FullLoader)
    return _config_data
