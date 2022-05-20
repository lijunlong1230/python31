import yaml


def read_yaml(file):
	with open(file,encoding='utf-8') as f:
		conn = yaml.load(f,Loader=yaml.SafeLoader)
	return conn

def write_yaml(file,data):
	with open(file,'w',encoding='utf-8') as f:
		yaml.dump(data,f)