"""
	Resolving getting configuration staff
"""
import yaml

def get_config_yaml(config_file):

	with open(config_file, 'r+') as file:
		config_data = yaml.load(file, Loader=yaml.FullLoader)
	return config_data['mysql']