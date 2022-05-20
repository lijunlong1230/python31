import yaml


def read_yaml(file):
	with open(file,encoding='utf-8') as f:
		ym = yaml.safe_load(f)
		print(ym)
	return ym

def write_yaml(file,data):
	with open(file,'w',encoding='utf-8') as f:
		yaml.dump(data,f)