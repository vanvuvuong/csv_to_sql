"""
	Resolving getting configuration staff
"""
import yaml

def get_config_yaml(config_file: str):

	with open(config_file, 'r+') as file:
		_config_data = yaml.load(file, Loader=yaml.FullLoader)
	return _config_data['mysql']
