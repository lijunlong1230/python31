import requests

from tests.test_login import logger


def visit(
		url=None,method='get',data=None,json=None,params=None,**kwargs
):
	rep = requests.request(url=url,method=method,data=data,json=json,params=params,**kwargs)
	try:
		return rep.json()
	except Exception as e:
		logger.error('返回错误的值')
		return None
