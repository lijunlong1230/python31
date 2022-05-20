from pprint import pprint

import yaml

#读取yaml文件
with open("config.yaml",encoding = 'utf-8') as f:
	pprint(yaml.safe_load(f))

#写入yaml文件
with open("config2.yaml",'w',encoding='utf-8') as f:
	yaml.dump("log:logyaml",f)
